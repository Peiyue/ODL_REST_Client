import get_all_ports_statics from get_all_ports_statics

while 1:
    data_old=get_all_ports_statics()
    data_new=get_all_ports_statics()
    result_switch={'Added Switch:':[],'Deleted Switch:':[]}
    check_old_switches(data_old,data_new)
    check_new_switches(data_old,data_new)
    print result_switch


def check_old_switches(data_old,data_new,result_switch)
    numofoldswitches=len(data_old['portStatistics'])
    numofnewswitches=len(data_new['portStatistics'])
    for switchindex in range(numofoldswitches)
        switchid=data_old['portStatistics'][switchindex]['node']['id']
        #check if a previous switch exist
        for i in range(numofnewswitches):
            if portid==data_new['portStatistics'][i]['node']['id']:
                           
                break
            else:
                result_switch['Deleted Switch:'].append(switchid)

def check_new_switches(data_old,data_new,result_switch)
    numofoldswitches=len(data_old['portStatistics'])
    numofnewswitches=len(data_new['portStatistics'])
    for switchindex in range(numofnewswitches)
        switchid=data_new['portStatistics'][switchindex]['node']['id']
        #check if a new switch added
        for i in range(numofoldswitches):
            if portid==data_old['portStatistics'][i]['node']['id']:
                break
            else:
                result_switch['Added Switch:'].append((switchid))
