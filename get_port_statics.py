import requests
import json
from requests.auth import HTTPBasicAuth
from conf import conf
#get connection info
conf=conf()	
#configure Json
headers = {'Content-type': 'application/json'}
flowUrl = '/controller/nb/v2/statistics/default/port/node/OF/00:00:00:00:00:00:00:02'
url = conf['controllerIp'] + flowUrl
#get flow static
result=requests.get(url,auth=conf['auth'],headers=headers)
print result
data=result.json()
print data
#Reference:https://jenkins.opendaylight.org/controller/job/controlller-merge-hydrogen-stable/lastSuccessfulBuild/artifact/opendaylight/northbound/flowprogrammer/target/site/wsdocs/resource_FlowProgrammerNorthbound.html
#Reference:http://net-ed.blogspot.se/2013/11/using-python-rest-api-to-manage-flow.html
