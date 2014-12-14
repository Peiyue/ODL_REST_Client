from switch_flow import switch_flow
from flow_finder import flow_finder
from add_flow import add_flow
from delete_flow import delete_flow

def loadbalancer(datarate,Balancer):
        if  Balancer['type']=='min':
                if datarate<float(Balancer['threshhold']):
                        for flow_delete in red['Delete flows']:
                            delete_flow(flow_finder(flow_delete))
                        for flow_add in red['Add flows']:
                            add_flow(flow_finder(flow_add))
                        return 'used'
                else:
                        return ''
        elif  Balancer['type']=='max':
                if datarate>float(Balancer['threshhold']):
                        for flow_delete in red['Delete flows']:
                                delete_flow(flow_finder(flow_delete))
                        for flow_add in red['Add flows']:
                                add_flow(flow_finder(flow_add))
                        return 'used'
                else:
                        return ''
                        
