# Simple SQL Queries with Wintap

The data model for Wintap is process centric. With that in mind, lets see what tables exist and how to get some high-level information from them.

## A few DuckDB basics
List all tables
```sql
show all tables;
```

Use a query to get tables and row counts
```sql
select table_name, estimated_size, column_count from duckdb_tables order by all;
```

Display columns and simple statistics about a single table
```sql
summarize process_net_conn;
```

## Getting started with Wintap Data
The process_uber_summary table has every process execution, along with summarized information about file, registry, network, dll's. It also has labels based on hits against Mitre/SIGMA rules and common living off the land (LolBAS[^1]) commands. Finally, there are labels for entities that were manually marked as being known bad from activities injected during the colllection.


### How many processes across the hosts? And lets gets some additional features about events and labels.
```sql
select hostname, 
  count(distinct process_name) uniq_processes,
  count(*) total_processes,
  sum(reg_reads) reg_reads,
  sum(reg_writes) reg_writes,
  sum(read_events) file_reads,
  sum(write_events) file_writes,
  sum(net_total_events) net_total_events,
  sum(net_total_size) net_total_size,
  sum(tcp_accept_count) tcp_accept_events,
  sum(tcp_connect_count) tcp_connect_events,
  sum(dll_num_uniq_files) dll_files,
  sum(total_sigma_hits) total_sigma_hits,
  sum(label_num_hits) label_num_hits,
  count(distinct label_source) uniq_label_source,
  sum(lolbas_num_rows) lolbas_hits,
  sum(mitre_num_rows) mitre_hits
from process_uber_summary
group by all 
order by all
;
```

### Summary by Process name
```sql
select process_name, count(distinct hostname) num_hosts, count(distinct user_name) num_users, count(*) num_executions
from process group by all order by all
;
```

### Processes with Multiple MD5's
```sql
select process_name, count(distinct file_md5) uniq_md5 from process group by all having uniq_md5>1;
```

### MD5s with Multiple Names
```sql
select file_md5, process_name, hostname, user_name, count(*) from process where file_md5='E7A6B1F51EFB405287A8048CFA4690F4' group by all order by all
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
select
    -- Slice the list to exclude the child process
	ptree_list_tuples[-1:][1]['process_name'] path_root,
	count(distinct ptree_list_tuples[-1:][1]['pid_hash']) uniq_root_pid_hash,
	median(level) median_path_depth,
	max(level) max_path_depth,
	count(*) num_process
from
	process_path
group by all
order by all
;
```

### Paths relative to the executable, or, how many different ways is an executable spawned?
```sql
select
	p.process_name,
	ptree_list_tuples[2:2][1]['process_name'] parent,
	ptree_list_tuples[3:3][1]['process_name'] grand_parent,
	ptree_list_tuples[4:4][1]['process_name'] great_grand_parent,
    max(p.level) max_depth,
    count(distinct hostname) uniq_hosts,
	count(*) num_executions
from process_path p
group by all
order by process_name, parent, grand_parent, great_grand_parent
```

### Processes using a certain file/port/ip

_Ouch!_ This dataset has no file activity!
```sql
select process_name, protocol, remote_ip_addr, remote_port, count(*)
from process_net_conn
where remote_port=22
group by all
order by all
```

### Potentially interesting inter-host communication
Let's look for network connections between hosts that we have instrumented. the goal is to look for interesting cases where we can confirm the processes responsible for each end of the connection.

In the Wintap data model, we create a key for network 5-tuples "conn_id" (a hash of local ip/port -> remote ip/port, protocol). In this definition, local/remote are relative to the host recording the data. As an example, that means for a given connection, this would be the data:

```sql
SELECT hostname, process_name, protocol, local_ip_addr, local_port, remote_ip_addr, remote_port
from process_net_conn
where conn_id='F6A1A412FE8988B22F0CD1295B7117C0'
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
	count(distinct l.local_port) num_local_ports,
	count(distinct l.remote_port) num_remote_ports,
	mode(l.local_port) common_local_port,
	mode(l.remote_port) common_remote_port,
	r.hostname,
	r.process_name,
	count(*) num_rows,
	first(l.conn_id) example_conn_id
from
	process_net_conn l
join process_net_conn r on
	l.conn_id = r.conn_id
	and l.hostname <> r.hostname
where l.process_name not in ('lsass.exe','svchost.exe')
and r.process_name not in ('lsass.exe','svchost.exe')
and l.local_port != 53
and l.remote_port != 53
group by all
order by l.process_name
;
```

Notice the filter conditions to reduce "noisy" processes and ports. It is subjective as to what is considered noisy or irrelevant.

# Resources
[^1]: https://github.com/LOLBAS-Project/LOLBAS
