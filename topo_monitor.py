import time
from time import ctime
from check_topo import check_topo
from get_topology import get_topology
from redundancy_Builder import redundancy_Builder
from get_switch_name import get_switch_name

def topo_monitor():
    
    time_interval=0.2
    print '**********************************************************'
    print '*                                                        *'        
    print '*     Topolodgy Detection and Redundancy Service         *'
    print '*                                                        *'
    print '**********************************************************'
    
    reds=redundancy_Builder()
    numoflb=len(reds)
    red_status={}
    for red in reds:
        red_status[red['redundancy name']]='inactive'


    print '[Service Info]'+ctime()   
    print str(numoflb)+' Redundancy rules Loaded!'

    data_orig=get_topology()
    data_old=get_topology()
    numoflinks=len(data_orig['edgeProperties'])

    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print '[Service Info]'+ctime()  
    print '>Here are the '+str(numoflinks),' links detected in the ODL'

    for link_index_old in range(numoflinks):
        s1=data_orig['edgeProperties'][link_index_old]['edge']['tailNodeConnector']['node']['id'] #switch ID
        p1=data_orig['edgeProperties'][link_index_old]['edge']['tailNodeConnector']['id'] #Port ID
        s2=data_orig['edgeProperties'][link_index_old]['edge']['headNodeConnector']['node']['id'] #switch ID
        p2=data_orig['edgeProperties'][link_index_old]['edge']['headNodeConnector']['id'] #Port ID
        print '[Link'+str(link_index_old+1)+'] '+get_switch_name(s1),' port ',p1,' connected to ',get_switch_name(s2),' port ',p2
    
    while 1:
        time.sleep(time_interval)
        data_new=get_topology()
        result_topo_deleted={}
        red_status=check_topo(data_orig,data_old,data_new,result_topo_deleted,reds,red_status)
        data_old=data_new

    #print result_switch
if __name__ == "__main__":
    topo_monitor()

