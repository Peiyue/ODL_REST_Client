from switch_flow import switch_flow
from flow_finder import flow_finder

from add_flow import add_flow
from time import ctime

from delete_flow import delete_flow

def loadbalancer(datarate,Balancer,chain):
        if  Balancer['type']=='min':
                if datarate<float(Balancer['threshhold']):
                        for flow_delete in Balancer['Delete flows']:
                            delete_flow(flow_finder(flow_delete))
                        for flow_add in Balancer['Add flows']:
                            add_flow(flow_finder(flow_add))
                        return 'used'
                else:
                        return ''
        elif  Balancer['type']=='max':
                if datarate>float(Balancer['threshhold']):

                        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
                        print '[LB Info]'+ctime()
                        print 'Load balancer triggered:'+' Chain- '+chain+' Rule- '+Balancer['balancerName']

                        for flow_delete in Balancer['Delete flows']:
                                delete_flow(flow_finder(flow_delete))

                        for flow_add in Balancer['Add flows']:
                                add_flow(flow_finder(flow_add))


                        return 'used'
                else:
                        return ''
                        
