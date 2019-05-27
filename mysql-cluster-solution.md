## mysql cluster solution

#### Requirements:

* Required db has write intensive opertions
* HA and Loadbalance required to cater large number of requests
* VM Instance and related resources to be optimized

#### Possible Solution(s)

###### 1) Single Master - multi slave | mysql master-slave replication 

* Read operations can be catered seperately to balance load
* 2-3 slave nodes can be configured as read replicas
* During master fail-over, one of the slaves has to configured to become master 

![image](https://user-images.githubusercontent.com/13016162/58405981-4437ee80-8086-11e9-9add-9f4e2195e337.png)

* ISUES/LIMITATIONS:  
a) aa  
b) bb  
c) cc  

###### 2) Master-Backup Master - multi slave | mysql master-slave replication

* Here we can have a redundant backup master which can be used duing master fail-over
* Slave nodes will only be used as read replicas

![image](https://user-images.githubusercontent.com/13016162/58406035-616cbd00-8086-11e9-92bd-99de3ff35524.png)

* ISUES/LIMITATIONS:  
a) aa   
b) bb  
c) cc  

###### 3) Galera clustered master - multi slave | galera & mysql replication hybrid

* Here master can be clustered using galera to avoid fail-over
* slaves can be used as read replicas to provide further load balance between READ/WRITE
* we could use only galera cluster if we do not want to seperate read operations since the load is already balanced within the cluster.

![image](https://user-images.githubusercontent.com/13016162/58406087-7d705e80-8086-11e9-8514-4829b1a6c791.png)

* ISUES/LIMITATIONS:  
a) aa   
b) bb  
c) cc  
