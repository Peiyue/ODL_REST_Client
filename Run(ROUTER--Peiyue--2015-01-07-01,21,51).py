from flow_adder import flow_adder
from topo_monitor import topo_monitor
from loadbalancer_monitor import loadbalancer_monitor
import thread
import sys

redundancy='no'
loadbalancer='no'
allservice='no'

if len(sys.argv)<3:
    for arg in range(len(sys.argv)):
            if sys.argv[arg]=='-r':
                redundancy='yes'
                
            elif sys.argv[arg]=='-l':
                loadbalancer='yes'

            elif sys.argv[arg]=='-a':
                allservice='yes'


    flow_adder

    if allservice=='yes':
        topo_monitor()
        loadbalancer_monitor,())
    elif redundancy=='yes':
        topo_monitor()
    elif loadbalancer=='yes':
        loadbalancer_monitor()
    else:
        topo_monitor()
else:
    print '[ERROR]:Only one argument allowed'
    print '-r Start redundancy service'
    print '-l Start loadbalancer service'
    print '-a Start redundancy service and loadbalancer service'
                




