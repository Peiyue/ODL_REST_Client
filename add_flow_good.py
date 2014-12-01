import requests
import json
from requests.auth import HTTPBasicAuth
from conf import conf
def add_flow(flow):
	#get connection info
        controllerIp='http://127.0.0.1:8080'
        ODL_user='admin'
        ODL_password='admin'
        auth = HTTPBasicAuth(ODL_user,ODL_password)
                   
	#Json confi
	data ={"installInHw":"true", "name":'', "node": {"id":"", "type":"OF"}, "ingressPort":"2", "etherType": "0x800", "protocol": "6", "tpDst": "80", "priority":"65535", "actions":[""]}
        data['name']=flow['flowName']
        data['node']['id']=flow['switchId']
        data['ingressPort']=flow['inComingPort']
	data['actions'][0]=flow['actions']
	
	headers = {'Content-type': 'application/json'}
	flowUrl = '/controller/nb/v2/flowprogrammer/default/node/OF/'+flow['switchId']+'/staticFlow/'+flow['flowName']
	url =controllerIp+flowUrl
	#Put flow
	result=requests.put(url,auth=auth,headers=headers,data=json.dumps(data))
        #Print result
	print result
#Reference:https://jenkins.opendaylight.org/controller/job/controlller-merge-hydrogen-stable/lastSuccessfulBuild/artifact/opendaylight/northbound/flowprogrammer/target/site/wsdocs/resource_FlowProgrammerNorthbound.html
#Reference:http://net-ed.blogspot.se/2013/11/using-python-rest-api-to-manage-flow.html
