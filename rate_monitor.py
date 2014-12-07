import time
from get_all_ports_statics import get_all_ports_statics
from check_old_switches import check_old_switches
from check_new_switches import check_new_switches
from check_ports_rate import check_ports_rate

time_interval=3

print '==========================================================='
print 'Rate Moniting Started...'

data_old=get_all_ports_statics()
while 1:
	time.sleep(time_interval)
	data_new=get_all_ports_statics()
	result_switch={'Added Port':[],'Deleted Port':[]}
	#check_old_ports(data_old,data_new,result,time_interval)
        print '==========================================================='
        result_switch=check_ports_rate(data_old,data_new,result_switch,time_interval)
        data_old=data_new  
	
	

    #print result_switch
