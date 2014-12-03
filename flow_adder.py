from extract_flow import extract_flow
import datetime
from add_flow import add_flow
print 'Reading flow conf and assign flow...'
print '=========================================='

starttime=datetime.datetime.now()

input = open('flowtable.txt', 'r')
input.readline()
success_counter=0
fail_counter=0
while 1:
    line=input.readline()
    if not line:
            break
    formated_flow=extract_flow(line)
    print formated_flow
    result=add_flow(formated_flow)
    if result<400:
        success_counter+=1
    else:
        fail_counter+=1
print 'Flow assign done!'
print '=========================================='
print 'Total number of flow: '+str(success_counter+fail_counter)
print 'Succeed: '+str(success_counter)
print 'Failed: '+str(fail_counter)
print 'For more Info, please check the log.'
input.close()

endtime=datetime.datetime.now()
print 'Finished in '+str((endtime-starttime).seconds)+'seconds'

