import requests
import json
from requests.auth import HTTPBasicAuth
from conf import conf
def get_port_statics(switchId):
    #get connection info
    conf=conf()	
    #configure Json
    headers = {'Content-type': 'application/json'}
    #portId='00:00:00:00:00:00:00:02'
    flowUrl = '/controller/nb/v2/statistics/default/port/node/OF/'+switchId
    url = conf['controllerIp'] + flowUrl
    #get flow static
    result=requests.get(url,auth=conf['auth'],headers=headers)
    #print json result
    print result
    #decode json data
    data=result.json()
    #return portStatic
    portStatic{'portId':'','RxPk':'','TxPk'=''}
    portStatic['portId']=data[u'portStatistic'][0][u'nodeConnector'][u'id']
    portStatic['RxPk']=data[u'portStatistic'][0][u'receivePackets']
    portStatic['TxPk']=data[u'portStatistic'][0][u'transmitPackets']
    return portStatic
#len=len(data[u'portStatistic'])
#for i in range(len):
