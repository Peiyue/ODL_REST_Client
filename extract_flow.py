def extract_flow(data):
    length= len(data)
    index=0
    flow={'flowName':'','wwitchId':'','inComingPort':'','actions':'','outPutPort':''}
    temp=['','','','','','','','','','','','']
    i=0
    while index<length:
            if data[index]!=' ':
                temp[i]=temp[i]+data[index]
            else:
                i=i+1
            index=index+1               
    print temp
    flow['flowName']=temp[0]
    flow['switchId']=temp[1]
    flow['inComingPort']=temp[2]
    flow['actions']=temp[3]
    flow['outPutPort']=temp[4]
    return flow
