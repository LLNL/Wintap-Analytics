## SQL Data Exploration Tools

### duckdb 

DuckDB provides a lightweight interface to databases, with a heavy-duty SQL engine. It is simple to install and use to query your wintap data.

Downloads can be found [here](https://duckdb.org/docs/installation).

Example use of duckdb to load a database file and query it:

```bash
./duckdb
v0.10.1 4a89d97db8
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D .open ACME-workshop-20231109-20231111.db
D select * from process limit 5;
┌──────────────────────┬───────────┬──────────────────────┬──────────────┬─────────────┬────────┬───┬──────────────────┬──────────────────────┬───────────┬──────────────────┬──────────┐
│       pid_hash       │ os_family │       agent_id       │ num_agent_id │  hostname   │ os_pid │ … │ hard_fault_count │ token_elevation_type │ exit_code │ num_process_stop │  dayPK   │
│       varchar        │  varchar  │       varchar        │    int64     │   varchar   │ int32  │   │      int32       │        int32         │   int64   │      double      │  int64   │
├──────────────────────┼───────────┼──────────────────────┼──────────────┼─────────────┼────────┼───┼──────────────────┼──────────────────────┼───────────┼──────────────────┼──────────┤
│ F208A37B8996B18AB5…  │ windows   │ f64cacf9-2653-45f5…  │            1 │ ACME-HH-SRE │   7032 │ … │                0 │                    1 │         0 │              1.0 │ 20240330 │
│ 4AB4CE4656F6A8FE8D…  │ windows   │ 1a71328c-a00b-4e3f…  │            1 │ ACME-HH-CHT │   6300 │ … │                0 │                    1 │         0 │              1.0 │ 20240330 │
│ 41C80B226AB01E9B51…  │ windows   │ 1a71328c-a00b-4e3f…  │            1 │ ACME-HH-CHT │    388 │ … │                  │                      │           │              0.0 │ 20240330 │
│ 4E7BEFF91E5C6945CC…  │ windows   │ 1a71328c-a00b-4e3f…  │            1 │ ACME-HH-CHT │   6208 │ … │                  │                      │           │              0.0 │ 20240330 │
│ FF3DD1BAA84EDF8B93…  │ windows   │ 1a71328c-a00b-4e3f…  │            1 │ ACME-HH-CHT │   1944 │ … │                  │                      │           │              0.0 │ 20240330 │
├──────────────────────┴───────────┴──────────────────────┴──────────────┴─────────────┴────────┴───┴──────────────────┴──────────────────────┴───────────┴──────────────────┴──────────┤
│ 5 rows                                                                                                                                                          44 columns (11 shown) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
D 
```

### dbeaver

DBeaver is an application that can be used to explore databses.  Using it, you can create and iterate on complex SQL queries to explore Wintap data. 

After installation, create a new database connection using the DuckDB driver and point it to the Wintap sample database. Then, from the menu bar, "SQL Editor->New SQL script". This where you enter queries and run them.

More info can be found on the dbeaver website [here](https://dbeaver.io/).
