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
			if datarate<Balancer['threshhold']:
				if flow_1['status']==0:
					switch_flow(flow_1)
					switch_flow(flow_2)
					print 'Loadbalancer--'+Balancer['balancerName']+'--triggered'
			#else:
			#	switch_flow(flow_2)
			#	switch_flow(flow_1)

	elif  Balancer['type']=='max':
		if datarate>Balancer['threshhold']:
			#if flow_1['status']==0:
				switch_flow(flow_1)
				switch_flow(flow_2)
				print 'Loadbalancer--'+Balancer['balancerName']+'--triggered'
			#else:
			#	switch_flow(flow_2)
			#	switch_flow(flow_1)
                                
