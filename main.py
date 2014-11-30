from extract_flow import extract_flow
from add_flow import add_flow

input = open('flowtable.txt', 'r')
input.readline()
while 1:
    line=input.readline()
    if not line:
            break
    formated_flow=extract_flow(line)
    print formated_flow
    add_flow(formated_flow)
    if formated_flow.['status']=='0'
        switch_flow(formated_flow)
    
    
input.close()
