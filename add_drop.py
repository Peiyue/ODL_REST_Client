import requests
import time
from time import ctime
import json
from requests.auth import HTTPBasicAuth
from conf import conf
#from error_decoder import error_decoder

conf=conf()
def add_drop():
        print '**********************************************************'
        print '*                                                        *'        
        print '*                  Disable Flooding                      *'
        print '*                                                        *'
        print '**********************************************************'
        data0={"installInHw":"true", "name":'D1', "node": {"id":"00:00:86:22:ec:a7:9b:4f", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}
        data1={"installInHw":"true", "name":'D1', "node": {"id":"00:00:00:00:00:00:00:01", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}
        data2={"installInHw":"true", "name":'D2', "node": {"id":"00:00:00:00:00:00:00:02", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}
        data3={"installInHw":"true", "name":'D3', "node": {"id":"00:00:00:00:00:00:00:03", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}
        data4={"installInHw":"true", "name":'D4', "node": {"id":"00:00:00:00:00:00:00:04", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}
        data5={"installInHw":"true", "name":'D5', "node": {"id":"00:00:00:00:00:00:00:05", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}
        data6={"installInHw":"true", "name":'D6', "node": {"id":"00:00:00:00:00:00:00:06", "type":"OF"}, "etherType": "0x800","priority":"655", "actions":["DROP"]}

        data=[data1,data2,data3,data4,data5,data6]
        for flow in data:
                time.sleep(0.5)

                headers = {'Content-type': 'application/json'}
                flowUrl = '/controller/nb/v2/flowprogrammer/default/node/OF/'+flow['node']['id']+'/staticFlow/'+flow['name']
                url =conf['controllerIp']+flowUrl
                result=requests.put(url,auth=conf['auth'],headers=headers,data=json.dumps(flow))
                print '[Flow Info]'+ctime()+' Code: '+str(result.status_code)
	
if __name__ == "__main__":
    add_drop()
