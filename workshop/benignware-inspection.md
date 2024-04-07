# Extracting and inpsecting specific activity

In this particular dataset, a researcher used the well known Volt-Typhoon[^1] attack as a model to inject malicious behaviour into the data set. As we walk thru, we'll pull that out to highlight what Wintap captures about a few specific events in this attack.

## Label Summary

The enrichment phase of Wintap data processing labels data from several sources. Here, we'll focus on manually created labels that identify the specific objects in the data that were part of the simulated attack. The manual labels were created by reviewing the data after collect with a variety of queries to identify the specific actions performed with malicious intent. The researcher that performed the attack was involved and guided the identification.

### Labels_Graph_Nodes: the core of the manual labels

The *Labels_Graph_Nodes* table is the primary place to start with manual labels. Its structure is:

| Column      | Description |
|-------------|-------------|
| filename    | Source of the annotations. Typical format of this file networkx JSON |
| node_type   | Wintap object type: Process/Network/File/Host |
| id          | Unique ID for the object |
| annotation  | Text description supplied by the person labelling data |
| label       | A simple text description from the object to give context, e.g., name, 5-tuple, etc. |

A subset of the NTDIS labels:

|            filename             |   node_type   |                id                |      annotation        |                         label                          |
|---------------------------------|---------------|----------------------------------|-------------------------|---------------------------------------------------------|
| labels/networkx/Volt-NTDIS.json | File          | c38b0190eab37cfcfd2e6a19e7e30f96 | Why written to Mcaffee? | c:\windows\temp\mcafee_logs\active directory\ntds.dit   |
| labels/networkx/Volt-NTDIS.json | File          | d480a9effc4c04175f8ca93aafb69b52 |                         | \device\harddiskvolumeshadowcopy2\windows\ntds\ntds.dit |
| labels/networkx/Volt-NTDIS.json | File          | ef40299a9ee7bc39fb974b3ef28bd23c | Shadow Copy of NTDS.DIT | c:\windows\temp\pro\active directory\ntds.dit           |
| labels/networkx/Volt-NTDIS.json | File          | fc59755b2cb407b8ce52bce0c794f0df |                         | \device\harddiskvolumeshadowcopy4\windows\ntds\ntds.dit |
| labels/networkx/Volt-NTDIS.json | FiveTupleConn | 19374D179E9D7D652ED318305ECFC4C0 |                         | TCP:172.31.37.19:63619                                  |
| labels/networkx/Volt-NTDIS.json | FiveTupleConn | 948A22142C76123B378AD4798B071B00 |                         | TCP:172.31.34.133:49669                                 |
| labels/networkx/Volt-NTDIS.json | FiveTupleConn | F6A1A412FE8988B22F0CD1295B7117C0 |                         | TCP:172.31.37.19:62435                                  |
| labels/networkx/Volt-NTDIS.json | Host          | ACME-DC1                         |                         | ACME-DC1                                                |
| labels/networkx/Volt-NTDIS.json | Host          | ACME-HH-HGC                      |                         | ACME-HH-HGC                                             |
| labels/networkx/Volt-NTDIS.json | Process       | 035841364F1C65CC93967F0D1497EC2E |                         | cmd.exe                                                 |
| labels/networkx/Volt-NTDIS.json | Process       | 056B6DB3CE71093B5197E5A52FC078DE |                         | arp.exe                                                 |
| labels/networkx/Volt-NTDIS.json | Process       | 088C475DF85D8791EA6A0394462D8905 |                         | sshd.exe                                                |


### Example of a small set of activity surrounding "Shadow Copy of NTDIS"
This is a bespoke query intended to tease out a bit of context surrounding the act of leverging shadow copy to get a copy of the NTDIS file. The import thing to note is how we can start to build up a graph of the process, file and network activity.

```
select * from (
  select p.first_seen,node_type, p.os_pid , p.parent_os_pid, annotation, concat_ws(' ',p.process_name, p.args) as label
  from labels_graph_nodes l
  join process p on l.id=p.pid_hash
  where l.filename ilike '%volt-nt%'
  union all
  select f.first_seen,node_type, substr(id,1,4)||'...', p.os_pid, annotation, label
  from labels_graph_nodes l
  join process_file f on l.id=f.file_id
  join process p on f.pid_hash=p.pid_hash
  where l.filename ilike '%volt-nt%'
  union all
  select n.first_seen,node_type, substr(id,1,4)||'...', p.os_pid, annotation, label
  from labels_graph_nodes l
  join process_net_conn n on l.id=n.conn_id
  join process p on n.pid_hash=p.pid_hash
  where l.filename ilike '%volt-nt%'
  )
  where cast(first_seen as date) >= date '2023-11-10'
  order by first_seen
  ;
```

|          first_seen           | node_type | os_pid  | parent_os_pid |       annotation        |                          label                          |
|-------------------------------|-----------|---------|---------------|-------------------------|---------------------------------------------------------|
| 2023-11-10 08:51:42.973623-07 | Process   | 10356   | 9400          |                         | ntdsutil.exe                                            |
| 2023-11-10 10:28:29.086381-07 | Process   | 8028    | 4356          |                         | userinit.exe                                            |
| 2023-11-10 10:28:29.183597-07 | Process   | 8256    | 8028          |                         | explorer.exe                                            |
| 2023-11-10 10:28:54.010032-07 | Process   | 12216   | 8256          |                         | powershell.exe                                          |
| 2023-11-10 10:51:00.487506-07 | Process   | 10188   | 12216         |                         | ntdsutil.exe                                            |
| 2023-11-10 10:51:45.165683-07 | File      | fc59... | 848           |                         | \device\harddiskvolumeshadowcopy4\windows\ntds\ntds.dit |
| 2023-11-10 10:51:46.121412-07 | File      | ef40... | 10188         | Shadow Copy of NTDS.DIT | c:\windows\temp\pro\active directory\ntds.dit           |

_Note that liberties were taken to reduce the data output for purpose of keeping this example small_


[^1]: https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_PRC_State_Sponsored_Cyber_Living_off_the_Land_v1.1.PDF
