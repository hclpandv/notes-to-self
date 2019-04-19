You have to first determine what the issue is ; if it's PHP, MySQL, I/O, load, memory, CPU, kernel, etc.  
sar logs the systems metrics; you'll have to catch it in the act.  
You can configure atop to do process accounting which definitely helps.  

### To determine if it's I/O

Use tools such as iotop and atop to see what the disk usage is; these tools will also tell you what is causing the IO. Generally, if iowait is sustained over 10% this could be the issue.

sar logs disk IO; so you can run sar -d to see it (look at %util column).

### To determine if it's load

Use tools such as htop, top, uptime; again tie this to the process running and find out more details about what the process is doing. Note that this reports the load on the scheduler; it doesn't reflect the CPU usage.

### To determine if it's a CPU

sar once again comes in to save the day; you can see this information with sar -P ALL. You can also use mpstat -P ALL for real-time data. Generally, the CPU is only an issue if all the CPU's are at 100%; 80%+ means they're being utilized (but not necessarily saturated).

### To determine if it's the Memory (VM)

You'll want to use vmstat; vmstat -S M 1 and observe the swap, io, and system columns. Obviously a high amount of swapping can impact performance. There is also the system section; a high amount of interrupts can also do the same.

### To determine if it's interrupts

You can use vmstat -S M 1. Unfortunately, it's hard to tell if interrupts are the issue if your system doesn't have a baseline on what is normal. A high amount of interrupts (which are caused from hardware requiring action from the kernel) will bring the system to a crawl. Failing NIC's are notorious for doing this.

### To determine if it's the kernel

This is trickier but generally requires strace, perf, or sysdig tools. One such tool is perf top. strace with a summary (-c) is nice but it doesn't break it down relative to the system resources (so the data that is provided is only speculation); it's ideal to use perf top to come to the conclusion that it's the kernel. You can also use stap (SystemTap) if your machine supports it. I should also note that  strace will impact performance; you should use sysdig if the system is at all important.

### To determine if it's MySQL/PHP

You basically have to follow what I posted above (perf for example can provide information on what command is causing high kernel time, iotop, atop, htop can provide information relative to system resources on what is using them); basically, you're using the above tools to determine what is causing the load.

Once you've determined it to be MySQL

It could be a query that you're running (so you'll want to use EXPLAIN on that query in MySQL). You'll also need to make sure that your database is optimized and that the queries you're executing are optimized. You'll also have to make sure that the table engine you're using is ideal for what you're doing (I've seen many large tables that MyISAM when they should be InnoDB). If you've determined that none of the above are the issue and still suspect MySQL you may want to archive data in the affected tables to reduce access (table scans) to that table. You may also want to verify constraint consistency, enable cache buffering, and ensure indexes are optimal.

A good tool to help in this process is mytop; but all the information that mytop provides is easily accessible in the mysql client. Some useful statements to run:

SHOW FULL PROCESSLIST\G to get a complete list of currently executing SQL statements as well as their status to the server.
SHOW ENGINE INNODB STATUS\G (InnoDB only)
EXPLAIN EXTENDED <QUERY> to explain a query that you see MySQL executing.
SHOW GLOBAL STATUS\G for a server-wide status
Once you've determined it to be PHP

You can use tools to profile your PHP code (such as xdebug) and then open the generated profile in KCacheGrind to see a performance analysis of the profiled PHP code.

---
######### If you find it's none of these you may just need to upgrade your server.
