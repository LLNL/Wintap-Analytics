# DuckDB Command Line Cheat Sheat

* DuckDB Docs: https://duckdb.org/docs/
* CLI: https://duckdb.org/docs/api/cli/overview
* SQL: https://duckdb.org/docs/sql/introduction

## Starting
Open database, read-only
```
duckdb ACME-workshop-20231109-20231111.db -readonly
```

## Running and editing queries

* As SQL is often multi-line, execution is triggered by a semi-colon at the end of the statement or on its own line:
```sql
select count(*) from process;

select count(*) from process
;
```

* Navigate through history with arrow keys

## Useful configuration settings
Set maximum rows displayed, default is 40
```sql
.maxrows 200
```

There is no good way to display a very wide row as there is no ability to do horizontal scrolling. So, the things you can do are:

Set wider than terminal, although it'll just wrap within the terminal. The default is 0 for terminal width.
```sql
.maxwidth 200
.maxwidth 0
```

Switch to display each column on its own line. Works well for view very few rows.
```sql
.mode line
```

Switch back to the default box layout.
```sql
.mode duckbox
```
