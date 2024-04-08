# Simple SQL Queries with Wintap

The data model for Wintap is process centric. With that in mind, lets see what tables exist and how to get some high-level information from them.

## A few DuckDB basics
List all tables
```sql
show all tables;
```

Use a query to get tables and row counts
```sql
SELECT
    table_name,
    estimated_size,
    column_count
FROM duckdb_tables ORDER BY ALL;
```

Display columns and simple statistics about a single table
```sql
summarize process_net_conn;
```

## Getting started with Wintap Data
The process_uber_summary table has every process execution, along with summarized information about file, registry, network, dll's. It also has labels based on hits against Mitre/SIGMA rules and common living off the land (LolBAS[^1]) commands. Finally, there are labels for entities that were manually marked as being known bad from activities injected during the colllection.


### How many processes across the hosts? And lets gets some additional features about events and labels.
```sql
SELECT
    hostname,
    count(DISTINCT process_name) AS uniq_processes,
    count(*) AS total_processes,
    sum(reg_reads) AS reg_reads,
    sum(reg_writes) AS reg_writes,
    sum(read_events) AS file_reads,
    sum(write_events) AS file_writes,
    sum(net_total_events) AS net_total_events,
    sum(net_total_size) AS net_total_size,
    sum(tcp_accept_count) AS tcp_accept_events,
    sum(tcp_connect_count) AS tcp_connect_events,
    sum(dll_num_uniq_files) AS dll_files,
    sum(total_sigma_hits) AS total_sigma_hits,
    sum(label_num_hits) AS label_num_hits,
    count(DISTINCT label_source) AS uniq_label_source,
    sum(lolbas_num_rows) AS lolbas_hits,
    sum(mitre_num_rows) AS mitre_hits
FROM process_uber_summary
GROUP BY ALL
ORDER BY ALL
;
```

### Summary by Process name
```sql
SELECT
    process_name,
    count(DISTINCT hostname) AS num_hosts,
    count(DISTINCT user_name) AS num_users,
    count(*) AS num_executions
FROM process GROUP BY ALL ORDER BY ALL
;
```

### Processes with Multiple MD5's
```sql
SELECT
    process_name,
    count(DISTINCT file_md5) AS uniq_md5
FROM process
GROUP BY ALL
HAVING uniq_md5 > 1;
```

### MD5s with Multiple Names
```sql
SELECT
    file_md5,
    process_name,
    hostname,
    user_name,
    count(*)
FROM process
WHERE file_md5 = 'E7A6B1F51EFB405287A8048CFA4690F4'
GROUP BY ALL
ORDER BY ALL
;
```


### Process Paths
Process paths are defined here as up to the root process. We're still experimenting with what data structure is the most useful, so for now, there are several and are in the PROCESS_PATH table:

* ptree (string): process names delimited with "->"
    * Example: ```=cmd.exe->explorer.exe->userinit.exe->winlogon.exe->smss.exe->smss.exe->ntoskrnl.exe```
* ptree_list([pid_hash]): a list of pid_hashes, from child to root
    * Example: ```['D608DE1B627B24B99FD3877CB7BD478C', ... ,'7ED3EF53920BF003FC33D83EC7116FFB','2F3F91E18F2D9B5A36552A9DDCBF0E4C']```
* ptree_list_tuple([pid_hash, process_name]): a list of tuples that include the pid_hash and process name
    * Example: ```[{'pid_hash': D608DE1B627B24B99FD3877CB7BD478C, 'process_name': cmd.exe}, {'pid_hash': AE8D851F89DE572F205A0B15C34E5E4E, 'process_name': explorer.exe}, ...```


### What are the roots of processes? They *should* all be ntoskrnl.exe
```sql
SELECT
    -- Slice the list to exclude the child process
    ptree_list_tuples[-1:][1]['process_name'] AS path_root,
    count(DISTINCT ptree_list_tuples[-1:][1]['pid_hash']) AS uniq_root_pid_hash,
    median(level) AS median_path_depth,
    max(level) AS max_path_depth,
    count(*) AS num_process
FROM
    process_path
GROUP BY ALL
ORDER BY ALL
;
```

### Paths relative to the executable, or, how many different ways is an executable spawned?
```sql
SELECT
    p.process_name,
    p.ptree_list_tuples[2:2][1]['process_name'] AS parent,
    p.ptree_list_tuples[3:3][1]['process_name'] AS grand_parent,
    p.ptree_list_tuples[4:4][1]['process_name'] AS great_grand_parent,
    max(p.level) AS max_depth,
    count(DISTINCT p.hostname) AS uniq_hosts,
    count(*) AS num_executions
FROM process_path AS p
GROUP BY ALL
ORDER BY p.process_name, parent, grand_parent, great_grand_parent
;
```

### Processes using a certain file/port/ip

_Ouch!_ This dataset has no file activity!
```sql
SELECT
    process_name,
    protocol,
    remote_ip_addr,
    remote_port,
    count(*)
FROM process_net_conn
WHERE remote_port = 22
GROUP BY ALL
ORDER BY ALL
;
```

### Potentially interesting inter-host communication
Let's look for network connections between hosts that we have instrumented. the goal is to look for interesting cases where we can confirm the processes responsible for each end of the connection.

In the Wintap data model, we create a key for network 5-tuples "conn_id" (a hash of local ip/port -> remote ip/port, protocol). In this definition, local/remote are relative to the host recording the data. As an example, that means for a given connection, this would be the data:

```sql
SELECT
    hostname,
    process_name,
    protocol,
    local_ip_addr,
    local_port,
    remote_ip_addr,
    remote_port
FROM process_net_conn
WHERE conn_id = 'F6A1A412FE8988B22F0CD1295B7117C0'
;
```

|Hostname|process_name|protocol|local_ip_addr|local_port|remote_ip_addr|remote_port|
|--------|------------|--------|-------------|----------|--------------|-----------|
|ACME-HH-HGC|ssh.exe|TCP|172.31.37.19|62435|172.31.34.133|22|
|ACME-DC1|sshd.exe|TCP|172.31.34.133|22|172.31.37.19|62435|

So now the goal is to join those 2 rows into a single row representing process->network->process. And that gets done with:
```sql
SELECT
    l.hostname,
    l.process_name,
    l.protocol,
    l.local_ip_addr,
    l.remote_ip_addr,
    r.hostname,
    r.process_name,
    count(DISTINCT l.local_port) AS num_local_ports,
    count(DISTINCT l.remote_port) AS num_remote_ports,
    mode(l.local_port) AS common_local_port,
    mode(l.remote_port) AS common_remote_port,
    count(*) AS num_rows,
    first(l.conn_id) AS example_conn_id
FROM
    process_net_conn AS l
INNER JOIN process_net_conn AS r
    ON
        l.conn_id = r.conn_id
        AND l.hostname <> r.hostname
WHERE
    l.process_name NOT IN ('lsass.exe', 'svchost.exe')
    AND r.process_name NOT IN ('lsass.exe', 'svchost.exe')
    AND l.local_port <> 53
    AND l.remote_port <> 53
GROUP BY ALL
ORDER BY l.process_name
;
```

Notice the filter conditions to reduce "noisy" processes and ports. It is subjective as to what is considered noisy or irrelevant.

# Resources
[^1]: https://github.com/LOLBAS-Project/LOLBAS
