ODL_REST_Client

===Install===
git clone git://github.com/Peiyue/ODL_REST_Client
===Configure===
Open conf.py to set the IP,Username,Password of your OpenDaylight
===Functions===
1)flow_adder.py
  add flow from flowtable.txt to the ODL
  use the flowtable.txt to set the flows
2)swtich_monitor.py
  moniting the status of the swtiches(added or removed )
3)rate_monitor.py
  get the datarate of the ports
  Usage: python rate_monitor.py [-m mode] [-t time]
  argument -t time the time interval of rate monitor in seconds,default value is 3
	 -m mode set the mode
       	         'all' print monitor all the ports,default
                 'customer' monitor the rate of ports specified in ratetable.txt
4)loadbalancer.py
  loadbalancer function
  use the loadbalancertalbe.txt to configure
5)topo_monitor.py
  link redundancy
  print the topology
  print info when link changes

