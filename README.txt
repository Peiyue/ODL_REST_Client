ODL_REST_Client

===Install===
git clone git://github.com/Peiyue/ODL_REST_Client
===Configure===
1.Open conf.py to set the IP,Username,Password of your OpenDaylight
2.Open flowtable.text to see up the flows
===Run===
#add flow from flowtable.txt to the ODL
python flow_adder.py
#swtich monitor
python switch_monitor.py
#get the datarate of all the ports
python rate_monitor.py
#a demo program to show get the statistics of a port
python get_port_statics_demo.py
