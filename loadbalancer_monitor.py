import time
from time import ctime
from get_all_ports_statics import get_all_ports_statics
from check_old_switches import check_old_switches
from check_new_switches import check_new_switches
from check_ports_rate_lb_new import check_ports_rate_lb
from loadbalancer_Builder import loadbalancer_Builder
from loadbalancer import loadbalancer

def loadbalancer_monitor():
        time_interval=0.5

        print '**********************************************************'
        print '*                                                        *'
        print '*                  Layer 2 Load Balancer                 *'
        print '*                                                        *'
        print '**********************************************************'



        loadbalancers=loadbalancer_Builder()
        print loadbalancers
        print '*******************************************'
        numoflb=len(loadbalancers)
        print '[Service Info]'+ctime()
        print str(numoflb)+' rules Loaded!'

        print '[Service Info]'+ctime()
        print 'LoadBalancer working now!'


        data_old=get_all_ports_statics()
        while 1:
                time.sleep(time_interval)
                data_new=get_all_ports_statics()
                result_switch={'Added Port':[],'Deleted Port':[]}
                #check_old_ports(data_old,data_new,result,time_interval)
                result_switch=check_ports_rate_lb(data_old,data_new,result_switch,time_interval,loadbalancers)
                data_old=data_new
       
if __name__ == "__main__":
        loadbalancer_monitor()
