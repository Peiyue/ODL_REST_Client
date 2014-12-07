from get_all_ports_statics import get_all_ports_statics
from check_old_switches import check_old_switches
from check_new_switches import check_new_switches

while 1:
    data_old=get_all_ports_statics()
    data_new=get_all_ports_statics()
    result_switch={'Added Switch:':[],'Deleted Switch:':[]}
    result_switch=check_old_switches(data_old,data_new,result_switch)
    result_switch=check_new_switches(data_old,data_new,result_switch)
    print result_switch
