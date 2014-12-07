#data structure
#flowUrl = '/controller/nb/v2/statistics/default/port

data['portStatistics'][0]['node']['id']
data['portStatistics'][0]['portStatistic'][0]['nodeConnector']['node'] #node Info
data['portStatistics'][0]['portStatistic'][0]['nodeConnector']['id'] #port ID
data['portStatistics'][0]['portStatistic'][0]['receiveBytes']
data['portStatistics'][0]['portStatistic'][0]['transmitBytes']
data['portStatistics'][0]['portStatistic'][0]['receivePackets']
data['portStatistics'][0]['portStatistic'][0]['transmitPackets']

len(data['portStatistics'])#number of switch
len(data['portStatistics'][0]['portStatistic'])#number of ports of a switch

data1
data2

def check_old_switches(data_old,data_new)
    numofoldswitches=len(data_old['portStatistics'])
    numofnewswitches=len(data_new['portStatistics'])
    for switchindex in range(numofoldswitches)
        switchid=data_old['portStatistics'][switchindex]['node']['id']
        #check if a previous switch exist
        for i in range(numofnewswitches):
            if portid==data_new['portStatistics'][i]['node']['id']:
                flag='switch keeps'             
                break
            else:
                flag='switch '+str(switchid)+'deleted'

def check_new_switches(data_old,data_new)
    numofoldswitches=len(data_old['portStatistics'])
    numofnewswitches=len(data_new['portStatistics'])
    for switchindex in range(numofnewswitches)
        switchid=data_new['portStatistics'][switchindex]['node']['id']
        #check if a new switch added
        for i in range(numofoldswitches):
            if portid==data_old['portStatistics'][i]['node']['id']:
                break
            else:
                flag='switch '+str(switchid)+'added'

				
				

				
				
				
				

def check_old_ports(data_old,data_new)
    #go through every old switch
	for switchindex_new in range(numofnewswitches)
        
		#find the switch id of a given switch
		switchid_old=data_old['portStatistics'][switchindex_new]['node']['id']
		#find the corresponding switch index in the new data
		switch_index_new=find_switch(switchid_old,data_new)
		
        
		#find the num of ports of a specific old switch
		numofoldports=len(data_olddata['portStatistics'][switchindex_old]['portStatistic'])
		
		#go through every port of a specific old switch
		for portindex in range(numofoldports)
            #find the port Id of a given port index
			portid=data_old['portStatistics'][switchid]['portStatistic'][portindex]['nodeConnector']['id']
			#check if the port exist
			numofnewports=len(data_newdata['portStatistics'][switch_index_new]['portStatistic'])
			check_deleted_port(portid,data_new,switch_index_new,result)
			
			
			
			
def switch_index_new=find_switch(switchid_old,data_new):
		numofswitchs_old=len(data['portStatistics'])
		for oldswitchindex in rang(numofswitchs_old)
			if switchid_old=data_new['portStatistics'][oldswitchindex]['node']['id']
				return oldswitchindex
	      
def result=check_deleted_port(switchid_old,portid,data_new,numofnewports,switch_index_new,result):

	for i in range(numofnewports):
		if portid==data_new['portStatistics'][switch_index_new]['portStatistic'][i]['nodeConnector']['id']:
			break
		else:
			result['Deleted Port'].append(str(switchid_old)+':'+portid)

								
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					

def check_new_ports(data_old,data_new)
    for switchindex in range(numofnewswitches)
        numofoldports=len(data_olddata['portStatistics'][switchindex]['portStatistic'])


        
        numofnewports=len(data_newdata['portStatistics'][0]['portStatistic'])



        for portindex in range(numofnewports)
            portid=data_old['portStatistics'][0]['portStatistic'][portindex]['nodeConnector']['id']
        #check if a previous switch exist
            for i in range(numofoldports):
                if portid==data_new['portStatistics'][0]['portStatistic'][i]['nodeConnector']['id']:
                    flag='port keeps'             
                    break
                else:
                    flag='switch '+str(switchid)+'deleted'

	
					

