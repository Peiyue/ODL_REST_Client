def extract_flow(data):
    length= len(data)
    index=0
    flow={'flowName':'','switchId':'','inComingPort':'','actions':['']}
    temp=['','','','','','','','','','','','']
    i=0
    while index<length:
            if data[index]!=' ':
                temp[i]=temp[i]+data[index]
            else:
                i=i+1
            index=index+1               
    flow['flowName']=temp[0]
    flow['switchId']=temp[1]
    flow['inComingPort']=temp[2]
    flow['actions'][0]=temp[3]
    if i>3:      
        for j in range(i-3):
            flow['actions'].append(temp[j+3])           
    return flow
