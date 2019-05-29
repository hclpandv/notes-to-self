## mysql cluster solution

#### Requirements:

* Required db has write intensive operations
* HA and Loadbalance required to cater large number of requests
* VM Instance and related resources to be optimized

#### Assumptions:

* Solution should be open source and self managed

#### Possible Solution(s)

**1) Single Master - multi slave | mysql master-slave replication** 

* Read operations can be catered seperately to balance load
* 2-3 slave nodes can be configured as read replicas
* if master goes down, one of the slaves has to be promoted as new master 

![image](https://user-images.githubusercontent.com/13016162/58405981-4437ee80-8086-11e9-9add-9f4e2195e337.png)

* ISUES/LIMITATIONS:  
a) Replication is asynchronous, may result in data loss  
b) slave-lag will impact data consistancy    
c) Identify and manualy promote most up-to-date slave      

**2) Master-Backup Master - multi slave | mysql master-slave replication**

* Here the redundant backup master can be promoted as new master when master goes down 
* Slave nodes will only be used as read replicas

![image](https://user-images.githubusercontent.com/13016162/58406035-616cbd00-8086-11e9-92bd-99de3ff35524.png)

* ISUES/LIMITATIONS:  
a) Semi-sync replication between master and backup master has a performance impact   
b) When master goes down, backup master needs to be promoted as new master  
c) slave-lag will impact data consistancy    
d) Configuration is complex and error prone   

**3) Multiple database nodes in a Galera cluster[Recommended Solution]**

* Here nodes will be kept in a galera cluster for HA
* Reverse proxy to be used to balance the load on galera nodes
* all nodes will be used for read and write requests
  
![image](https://user-images.githubusercontent.com/13016162/58466408-4158fe80-8157-11e9-9510-bb3a07a303fa.png)

* ISUES/LIMITATIONS:  
a) Application should be modified to work around the [Galera Cluster limitations](http://galeracluster.com/documentation-webpages/limitations.html)   
b) Performance of a galera cluster depends on distance between nodes. (performance decreases if nodes are far from each other)  
c) Transaction size impacts performance (large transactions should be divided into smaller chunks to support galera)   
```sql
# a 500,000 rows table
mysql> UPDATE mydb.settings SET success = 1;
```
vs
```bash
(bash)$ for i in {1..500}; do \
mysql -uuser -ppassword -e "UPDATE mydb.settings SET success = 1 WHERE success != 1 LIMIT 1000"; \
sleep 2; \
done
```

###### Reasons to pick Galera Cluster over MySQL replication:

* A high availability solution with synchronous replication, failover and resynchronization.
* Ability to safely write to multiple masters.
* All servers have up-to-date data (no slave lag)
* Automatic Node provisioning.
* Data consistency automatically managed (and guaranteed) across databases.
* New database nodes easily introduced and synced.
* Failures or inconsistencies automatically detected.
* In general, more advanced and robust high availability features.

