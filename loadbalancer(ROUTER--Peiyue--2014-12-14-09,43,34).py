from switch_flow import switch_flow
from flow_finder import flow_finder

def loadbalancer(datarate,Balancer):
	#Balancer['balancerName']
	#Balancer['switchId']
	#Balancer['portId']
	#Balancer['threshhold']
	#Balancer['type']
	#Balancer['flows']
        flow_1=flow_finder(Balancer['flows'][0])
        flow_2=flow_finder(Balancer['flows'][1])
	print 'Loadbalancer--'+Balancer['balancerName']+'--checking'
	if  Balancer['type']=='min':
		if datarate<float(Balancer['threshhold']):
                        print 1
        elif  Balancer['type']=='max':
                if datarate>float(Balancer['threshhold']):
                        print 2
                        
