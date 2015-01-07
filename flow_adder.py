from extract_flow import extract_flow
import datetime
from add_flow import add_flow
import time
from time import ctime,time,sleep

def flow_adder():
    print '**********************************************************'
    print '*                                                        *'        
    print '*                  Add the default flows                 *'
    print '*                                                        *'
    print '**********************************************************'

    starttime=time()

    input = open('flowtable.txt', 'r')
    input.readline()
    success_counter=0
    fail_counter=0
    while 1:
        line=input.readline()
        if not line:
                break
        formated_flow=extract_flow(line)

        #if the flow is defaultly inactive, turn off the flow
        if formated_flow['Status']=='1':
            result=add_flow(formated_flow)
            sleep(0.2)
            if result<400:
                success_counter+=1                    
            else:
                fail_counter+=1

        

    print '' 
    print 'Summary'
    print '=========================================================='
    print 'Total number of flow: '+str(success_counter+fail_counter)
    print 'Succeed: '+str(success_counter)
    print 'Failed: '+str(fail_counter)
    print 'For more Info, please check the log.'
    print '----------------------------------------------------------'
    input.close()

    endtime=time()
    print 'Finished in '+'%.2f'%float(endtime-starttime)+' seconds'
    return str(success_counter)+' Primary flow added '+str(18-success_counter)+' failed'
    print '=========================================================='

if __name__ == "__main__":
    flow_adder()
