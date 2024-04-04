-- Simple queries that summarize important aspects of a dataset. These are useful to quickly understand overall dataset scope.

-- Host Summary
select hostname, count(distinct process_name) uniq_processes, count(*) processes,count(distinct username) uniq_users from process group by all order by all;

