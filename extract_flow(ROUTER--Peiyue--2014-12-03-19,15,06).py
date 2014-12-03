def extract_flow(data):
    length= len(data)
    index=0
    flow={'flowName':'','wwitchId':'','inComingPort':'','actions':['']}
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
    flow['actions'][0]=temp[3]
    if len(temp)>4:      
        for j in range(i-3):
            print flow['actions']
            flow['actions'].append(temp[j+3])
    return flow
