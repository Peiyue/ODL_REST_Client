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
    for switchindex in range(numofnewswitches)
        numofoldports=len(data_olddata['portStatistics'][switchindex]['portStatistic'])

        
        numofnewports=len(data_newdata['portStatistics'][0]['portStatistic'])



        for portindex in range(numofoldswitches)
            portid=data_old['portStatistics'][0]['portStatistic'][portindex]['nodeConnector']['id']
            #check if a previous switch exist
            for i in range(numofnewswitches):
                if portid==data_new['portStatistics'][0]['portStatistic'][i]['nodeConnector']['id']:
                    flag='port keeps'             
                    break
                else:
                    flag='switch '+str(switchid)+'deleted'



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



