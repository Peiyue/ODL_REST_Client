import time
from rate_Builder import rate_Builder
import sys
from get_all_ports_statics import get_all_ports_statics
from check_old_switches import check_old_switches
from check_new_switches import check_new_switches
from check_ports_rate_spg import check_ports_rate_spg



#default settings
def rate_monitor_spg():
        mode='all'
        time_interval=0.5
        data_old=get_all_ports_statics()
        time.sleep(time_interval)
        data_new=get_all_ports_statics()
        result_switch={'Added Port':[],'Deleted Port':[]}
        result_rate=[]
        #check_old_ports(data_old,data_new,result,time_interval)
        print 'Check Rate'
        result_rate=check_ports_rate_spg(data_old,data_new,result_switch,time_interval,mode,result_rate)
        data_old=data_new
        return result_rate
