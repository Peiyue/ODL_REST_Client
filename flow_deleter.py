from extract_flow import extract_flow
import datetime
from add_flow import add_flow
from switch_flow import switch_flow
from delete_flow import delete_flow
from time import ctime,time,sleep

def flow_deleter():
    print '**********************************************************'
    print '*                                                        *'        
    print '*                  Delete ALL flowx(except D0~D6)        *'
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
        result=delete_flow(formated_flow)
        if result<400:
            success_counter+=1                    
        else:
            fail_counter+=1

        

        
    print '' 
    print 'Summary'
    print '=========================================================='
    
    print 'Total number of deleted flows: '+str(success_counter+fail_counter)
    print 'Succeed: '+str(success_counter)
    print 'Failed: '+str(fail_counter)
    print 'For more Info, please check the log.'
    input.close()
    print '----------------------------------------------------------'
    endtime=time()
    print 'Finished in '+'%.2f'%float(endtime-starttime)+'seconds'
    return str(success_counter)+' flows '+ 'deleted.'

if __name__ == "__main__":
    flow_deleter()

