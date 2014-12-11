import time
from time import ctime
from add_flow import add_flow
from delete_flow import delete_flow


red[0]={'redundancy name':'red1','headNodeConnector':'','tailNodeConnector':'','Delete flows':[],'Add flows':[]}

def redundancy_manager(tailNodeConnector,headNodeConnector,reds):

    #search if any redundancy rules hit
    for red in reds:
        if tailNodeConnector=red['tailNodeConnector']
            if headNodeConnector=red['headNodeConnector']
                print 'redundancy activated:',red['redundancy name']
                for flow_add in red['Add_flows']
                    add_flow(flow_add)
                for flow_delete in red['Delete flows']
                    delete_flow(flow_delete)
    
