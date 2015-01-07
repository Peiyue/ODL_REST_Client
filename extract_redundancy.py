def extract_redundancy(data):
    length= len(data)
    index=0

    redundancy={'redundancy name':'red1','headNodeConnector':'','tailNodeConnector':'','Delete flows':[],'Add flows':[]}
    
    temp=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    i=0
    while index<length:
            if data[index]!=' ':
                temp[i]=temp[i]+data[index]
            else:
                i=i+1
            index=index+1               
    redundancy['redundancy name']=temp[0]
    redundancy['depend']=temp[1]
    redundancy['headNodeConnector']=temp[2]
    redundancy['tailNodeConnector']=temp[3]
    redundancy['Add flows'].append(temp[5])
   
    for index_temp in range(6,i):
        if temp[index_temp]!='DELETE':
            redundancy['Add flows'].append(temp[index_temp])
        elif temp[index_temp]=='DELETE':
            break
    for index_temp_d in range (index_temp+1,i):
        redundancy['Delete flows'].append(temp[index_temp_d])
    return redundancy



