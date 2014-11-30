import requests
import json
from requests.auth import HTTPBasicAuth
from conf import conf
from get_port_statics import get_port_statics
from flow_switch import flwo_switch

port1=Balancer['switchId_1']
port2=Balancer['switchId_2']
port1_TxPk=get_port_statics(port1)
port2_TxPk=get_port_statics(port2)

if port2_TxPk-port1_TxPk>10
length=len(Balancer['rules'])
for i in range(length-1)

    flow_1=Balancer['rules'][0][0]
    flow_2=Balancer['rules'][0][1]

    if flow_1['status']==0:
        switch_flow(flow_1)
        switch_flow(flow_2)
    else:
        switch_flow(flow_2)
        switch_flow(flow_1)
