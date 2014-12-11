import time
from time import ctime
from check_topo import check_topo
from check_topo import check_topo
from get_topology import get_topology
from check_topo import check_topo
from loadbalancer import loadbalancer


time_interval=1

print '==========================================================='
print ctime(),'Topology Monitor started'
print '========================Log================================'

data_old=get_topology()


numoflinks=len(data_old['edgeProperties'])

print str(numoflinks),'links detected'

for link_index_old in range(numoflinks):
    s1=data_old['edgeProperties'][link_index_old]['edge']['tailNodeConnector']['node']['id'] #switch ID
    p1=data_old['edgeProperties'][link_index_old]['edge']['tailNodeConnector']['id'] #Port ID
    s2=data_old['edgeProperties'][link_index_old]['edge']['headNodeConnector']['node']['id'] #switch ID
    p2=data_old['edgeProperties'][link_index_old]['edge']['headNodeConnector']['id'] #Port ID
    print' Switch ',s1,' port ',p1,' connected to ',' Switch ',s2,' port ',p2

while 1:
	time.sleep(time_interval)
	data_new=get_topology()
	result_topo_deleted={'headNodeConnector':[],'hn port':[],'tailNodeConnector':[],'tn port':[]}
	result_topo_added={'headNodeConnector':[],'hn port':[],'tailNodeConnector':[],'tn port':[]}
        result_switch=check_topo(data_old,data_new,result_topo_deleted)
        data_old=data_new

#print result_switch
