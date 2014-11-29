import requests
import json
from requests.auth import HTTPBasicAuth
def add_port_statics():
	#Connection confi
	controllerIp = 'http://http://192.168.80.128:8080'
	ODL_user='admin'
	ODL_passwd = 'admin'
	auth = HTTPBasicAuth(ODL_user,ODL_passwd)
	
	headers = {'Content-type': 'application/json'}
	flowUrl = '/controller/nb/v2/statistics/default/port/node/OF/00:00:00:00:00:00:00:02'
	url = controllerIp + flowUrl
	#get flow
	result=requests.get(url,auth=auth,headers=headers)
	
	
	
	print static
	print result
	return static
#Reference:https://jenkins.opendaylight.org/controller/job/controlller-merge-hydrogen-stable/lastSuccessfulBuild/artifact/opendaylight/northbound/flowprogrammer/target/site/wsdocs/resource_FlowProgrammerNorthbound.html
#Reference:http://net-ed.blogspot.se/2013/11/using-python-rest-api-to-manage-flow.html
