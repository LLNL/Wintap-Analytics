import fsspec
import s3fs
import os
from dataclasses import dataclass
import logging
from duckdb import CatalogException
from typing import List, ClassVar

import duckdb
import streamlit as st
import wintappy.datautils.rawutil as ru


@dataclass
class Dataset:
    # Class vars
    # Note: if needed in the future, this could be mondified to handle multiple FS types.
    # Couldn't find a common interface or class for filesystems? Seems odd..
    fs: ClassVar[object] = None
    protocol: ClassVar[str] = None
    # Instance vars
    name: str
    path: str
    agg_levels: List[str]
    databases: List[str] = None
    description: str = None
    # Any non-fatal data issues found.
    # TODO: Make one of these at the DB level? For db specific issues?
    warnings: List[str] = None

    @classmethod
    def getfs(cls, path):
        if cls.fs == None:
            logging.debug(f"Guessing filesystem: {path}")
            if path.startswith('/'):
                # Must be local
                cls.protocol="file"
            else:
                # Strip the protocol off and create the FS with that.
                cls.protocol = path.split(':')[0]
            cls.fs = fsspec.filesystem(cls.protocol)
        return cls.fs

    @classmethod
    def from_path(cls, path: str, name: str = None):
        if name == None:
            name = path.split('/')[-1:][0]

        agg_levels = []
        for dir in cls.getfs(path).ls(path):
            if cls.getfs(path).isdir(path):
                agg_levels.append(dir)
        databases = getdbs(path)
        return cls(
            name=name,
            path=path,
            agg_levels=agg_levels,
            databases=databases,
            description="Fix me! Generate one or pull from a metadata file?",
        )

    def getdb(self, dbname):
        # This path is for DuckDB, so add the protocol back in if needed.
        if self.protocol == "s3":
            return f"s3://{dbname}"
        else:
            return dbname


def finddatasets(path):
    myfs = Dataset.getfs(path)
    datasets = {}
    for dir in myfs.ls(path):
        print(f"iterating dir {dir}")
        # Assume every one is a dataset
        if myfs.isdir(dir):
            ds = Dataset.from_path(dir)
            print(f"ds={ds}")
            # For now, only datasets with databases defined are valid.
            if len(ds.databases) > 0:
                print(type(datasets))
                print(type(ds))
                datasets[ds.name] = ds
        else:
            print(f"{dir} did not pass isdir check")
    return datasets

def getdbs(path):
    # Load paths to any db files
    dbfiles = []
#    logging.debug('/'.join(path, "dbhelpers"))

    if Dataset.getfs(path).isdir(f"{path}/dbhelpers"):
        logging.debug("dbhelpers exists")
        for dbpath in Dataset.getfs(path).ls(f"{path}/dbhelpers"):
            print(f"  dpath={dbpath}")
            if dbpath.endswith(".db"):
                dbfiles.append(dbpath)
    else:
        logging.debug("dbhelpers does not exist")
    return dbfiles

def s3(con):
    # Note: DuckDB uses different key names than the cli. 
    #  Also, ENDPOINT can't have the protocol!
    endpoint = os.environ['AWS_ENDPOINT_URL'].split('http://')[1]
    s3info=f'''
        CREATE OR REPLACE SECRET spk16s3 (
            TYPE S3,
            PROVIDER CREDENTIAL_CHAIN,
            URL_STYLE 'path',
            ENDPOINT '{endpoint}',
            USE_SSL '{os.environ['DUCKDB_USE_SSL']}',
            REGION '{os.environ['AWS_DEFAULT_REGION']}',
            KEY_ID '{os.environ['AWS_ACCESS_KEY_ID']}',
            SECRET '{os.environ['AWS_SECRET_ACCESS_KEY']}'
        )
    '''
    print(s3info)
    con.sql(s3info)


def getdbcon(file):
    # Create and attach to a memory instance that will be used for analytic objects
    # Note: Duckdb requires the first database to be read/write.
    con = duckdb.connect(":memory:")
    # List of markdown text for feedback
    msgs = ""
    try:
        # Setup for the connection from DuckDB to S3
        if file.startswith('s3://'):
            s3(con)
        # Attach to the dataset, read_only.
        con.sql(f"attach '{file}' as ds (read_only true)")
        #        msgs=msgs+f"- :white_check_mark: Attached to: {file}\n"
        # Set memory as default db for new objects
        con.sql("use memory")
        # Set the catalog search path to include both databases
        con.sql("SET search_path = 'memory,ds'")
        try:
            # Create analytic views
            logging.debug("Running analytics ddl")
            ru.run_sql_no_args(con, "common/analytics-ddl.sql")
        except ru.InvalidSchema as e:
            # For error
            msgs = msgs + f":warning: analytics-ddl.sql failed: {md_code(e)}\\\n"
        msgs = msgs + f":smile: Database: {file}"
    except duckdb.IOException as ioe:
        st.error(f"Failed to attach to database:\n {ioe}")
        con = None
        msgs = msgs + f":exclamation: Failed to attach to {file}: {md_code(ioe)}\\\n"
    return con, msgs


# For now, caching is performed using session_state.
# @st.cache_resource
def opendb(filename):
    """
    Open the dbfile read-only and create a memory instance that will host the analytic views/tables.
    Use session_state.con to cache the db instance.
    """
    con, msgs = None, None
    if "con" in st.session_state:
        if filename != st.session_state["filename"]:
            # User changed files, re-create db.
            if "con" in st.session_state and st.session_state["con"] != None:
                # Close prior db.
                print("  Closing db")
                st.session_state["con"].close()
            print("  Opening db - new filename")
            con, msgs = getdbcon(filename)
            savecon(con, msgs, filename)
        else:
            # Same db, return the cached con
            con = st.session_state["con"]
            msgs = st.session_state["msgs"]
            logging.debug("Using cached con in session_state")
    else:
        # New connection
        print("  Opening db - init")
        con, msgs = getdbcon(filename)
        savecon(con, msgs, filename)
    return con, msgs


def savecon(con, msgs, filename):
    # Save db con and filename in session_state
    st.session_state["con"] = con
    st.session_state["filename"] = filename
    st.session_state["msgs"] = msgs
    logging.debug("Saved in session_state")


def getcon():
    con = None
    if "con" in st.session_state:
        con = st.session_state.con
    else:
        st.error("No DB defined")
    return con


def md_code(str):
    """
    Wrap the sring in code markdown
    """
    return f"\n```\n{str}\n```\n"


def getsqlstmt(filename, name) -> ru.SqlStmt:
    sqls = ru.loadSqlStatements(filename)
    sql = next(x for x in sqls if x.name == name)
    return sql


# Since this is very specific to data and its display, should it go in the streamlit file?
def getplsdf(con):
    sqlstmt = getsqlstmt("common/process-queries.sql", "process_life_summary")
    plsdf = con.sql(sqlstmt.sql).df().fillna("")
    plsdf.loc[plsdf.index[-1], "process_life_cd"] = "Total"
    #    plsdf.loc[plsdf.index[-1],'pct']=' '
    return plsdf


def get(con, name):
    sqlstmt = getsqlstmt("common/process-queries.sql", name)
    return getonerow(con, sqlstmt.sql)


def getonerow(con, sql: str):
    return con.sql(sql).fetchone()


def getdata(con, sql: str):
    df = None
    try:
        df = con.execute(sql).fetchdf()
    except CatalogException as e:
        logging.warning(
            f"Warning! SQL Failed due to missing object:\n {sql} due to:\n{e}"
        )
    return df
