import time
from get_all_ports_statics import get_all_ports_statics
from check_old_switches import check_old_switches
from check_new_switches import check_new_switches

data_old=get_all_ports_statics()
print '==========================================================='
print 'Rate Moniting Started...'
print '===================Datarate Record==================='

while 1:
	time_interval=3
	time.sleep(time_interval)
    data_new=get_all_ports_statics()
    result_switch={'Added Switch:':[],'Deleted Switch:':[]}
	#check_old_ports(data_old,data_new,result,time_interval)
    result_switch=check_old_ports(data_old,data_new,result_switch,time_interval)
    data_old=data_new  
	
	

    #print result_switch
