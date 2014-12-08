def extract_loadbalancer(data):
    length= len(data)
    index=0

    Balancer={'balancerName':'balancer1','switchId':'00:00:00:1','portId':'0','threshhold':10,'type':'max','flows':['','']}
    
    temp=['','','','','','','','','','','','']
    i=0
    while index<length:
            if data[index]!=' ':
                temp[i]=temp[i]+data[index]
            else:
                i=i+1
            index=index+1               
    Balancer['balancerName']=temp[0]
    Balancer['switchId']=temp[1]
    Balancer['portId']=temp[2]
    Balancer['threshhold']=temp[3]
    Balancer['type']=temp[4]
    Balancer['flows'][0]=temp[5]
    Balancer['flows'][1]=temp[6]

    
    return Balancer



