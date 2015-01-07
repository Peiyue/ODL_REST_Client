import time
from time import ctime
from add_flow import add_flow
from delete_flow import delete_flow
from flow_finder import flow_finder

def redundancy_manager(tailNodeConnector,headNodeConnector,reds,red_status):

    #search if any redundancy rules hit
    for red in reds:
        if tailNodeConnector==red['tailNodeConnector']:
            if headNodeConnector==red['headNodeConnector']:
                if red['depend']!='self':
                    if red_status[red['depend']]=='active':
                        print '[Service Info]'+ctime()
                        print 'Redundancy triggered:',red['redundancy name']
                        
                        for red_d in reds:
                            if red_d['redundancy name']==red['depend']:
                                for flow_add in red['Add flows']:
                                    delete_flow(flow_finder(flow_add))
                                for flow_delete in red['Delete flows']:
                                    add_flow(flow_finder(flow_delete))

                                    
                        for flow_delete in red['Delete flows']:
                            delete_flow(flow_finder(flow_delete))
                        delete_flow(flow_finder(red['Add flows'][0]))
                        for flow_add in red['Add flows']:
                            add_flow(flow_finder(flow_add))
                        red_status[red['redundancy name']]='active'                              
                        break

                
                elif red['depend']=='self':
                    print '[Service Info]'+ctime()
                    print 'Redundancy triggered:',red['redundancy name']
                    for flow_delete in red['Delete flows']:
                        delete_flow(flow_finder(flow_delete))

                    delete_flow(flow_finder(red['Add flows'][0]))

                    for flow_add in red['Add flows']:
                        add_flow(flow_finder(flow_add))
                    red_status[red['redundancy name']]='active'
    return red_status
                    
    
