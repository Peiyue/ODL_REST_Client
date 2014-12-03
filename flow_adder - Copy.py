from extract_flow import extract_flow
import datetime

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

