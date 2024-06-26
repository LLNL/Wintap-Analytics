"""
Functions for creating graph data structures from wintap sql results
Note: this is incomplete and being re-written from the pandas version in deprecated/wintapgraph-pandas.py
"""

import duckdb
import networkx as nx
from jinja2 import Template

# Filter to selected processes to use as seeds for the graph to build
# Note: some processes are missing ProcessName, at least. These are likely cases where we only have TERM

# Display a summary of seed processes. Its ok if this result too broad. At this point, better to have a few false positives than miss one.
# Your mission: visually inspect and see if it seems right for the current data set.

search_sql = """
select * from process
{%- for x in names -%}
    {% if loop.first %}
    where
    {% else %}
    or 
    {% endif %}
    process_name like '%{{ x }}%'
{%- endfor -%}
"""


def search_process_name_in(con, names):
    sql = Template(search_sql).render(names=names)
    print(sql)
    return con.sql(sql)


def add_proc_node_for(g, processes: duckdb.DuckDBPyRelation):
    print(f"Adding {processes.count('*').fetchone()[0]} process nodes")
    cols = processes.columns
    for row in processes.fetchall():
        add_node(
            g,
            row[cols.index("pid_hash")],
            "process",
            f"{row[cols.index('process_name')]}\n ({row[cols.index('os_pid')]})",
        )


def add_parents(g, con, seeds):
    # Get all parents by leveraging the pre-built list of PID_HASHes in ptree_list.
    parents_sql = f"""
select * from process where pid_hash in 
(
select unnest(ptree_list[2:]) pid_hash from process_path
where pid_hash in ({seeds.select('pid_hash').sql_query()})
)
order by process_started desc
    """

    parents = con.sql(parents_sql)
    add_proc_node_for(g, parents)
    add_parent_child(g, seeds)
    add_parent_child(g, parents)


def add_parent_child(g, processes):
    """
    Add parent-child edges and nodes for each process passed to the graph.
    """
    cols = processes.columns
    for row in processes.fetchall():
        if row[cols.index("pid_hash")] and row[cols.index("parent_pid_hash")]:
            g.add_edge(
                row[cols.index("pid_hash")],
                row[cols.index("parent_pid_hash")],
                type="parent",
            )


def add_node(graph, idx, nodetype, label, attributes={}):
    """
    Add a node with the given properties.
    This is to ensure all nodes have minimal common attributes
    """
    graph.add_node(idx, label=label, type=nodetype)
    # TODO: Figure out the pythonic way to do this.
    # Now set the other attributes.
    nx.set_node_attributes(graph, {idx: attributes})
    return graph


def add_network_activity(con, netg, max_pnc=100, add_ip_nodes=True):
    """
    Add all network activity from processNetConnDF to the graph for the given set of pid_hashes
    TODO: Implement skip/add group node if more than maxPNC/pid_hash
    """
    ignore_list = ["svchost.exe", "ntoskrnl.exe"]
    new_pid_hashes = []
    pid_list = ", ".join(["'{}'".format(id) for id in netg.nodes()])
    pnc_result = con.sql(
        f"select * from process_net_conn where pid_hash in ({pid_list})"
    )

    cols = pnc_result.columns
    print(f"Adding {pnc_result.count('*').fetchone()[0]} network edges")
    for row in pnc_result.fetchall():
        add_node(
            netg,
            row[cols.index("conn_id")],
            "pnc",
            row[cols.index("local_ip_addr")] + "->" + row[cols.index("remote_ip_addr")],
        )
        netg.add_edge(row[cols.index("pid_hash")], row[cols.index("conn_id")])
        if add_ip_nodes:
            add_node(
                netg,
                row[cols.index("local_ip_addr")],
                "ip",
                row[cols.index("local_ip_addr")],
            )
            add_node(
                netg,
                row[cols.index("remote_ip_addr")],
                "ip",
                row[cols.index("remote_ip_addr")],
            )
            netg.add_edge(row[cols.index("conn_id")], row[cols.index("local_ip_addr")])
            netg.add_edge(row[cols.index("conn_id")], row[cols.index("remote_ip_addr")])


def build_graph(con, process_name_seeds, name=None):
    if not name:
        name = f"Process Graph from {','.join(process_name_seeds)}"

    seed_processes = search_process_name_in(con, process_name_seeds)

    netg = nx.Graph(name=name)
    add_proc_node_for(netg, seed_processes)
    add_network_activity(con, netg)
    add_parents(netg, con, seed_processes)
    return netg, seed_processes
