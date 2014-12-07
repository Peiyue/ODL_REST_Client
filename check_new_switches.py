def check_new_switches(data_old,data_new,result_switch):
    numofoldswitches=len(data_old['portStatistics'])
    numofnewswitches=len(data_new['portStatistics'])
    for switchindex in range(numofnewswitches):
        switchid=data_new['portStatistics'][switchindex]['node']['id']
        #check if a new switch added
        for i in range(numofoldswitches):
            if switchid==data_old['portStatistics'][i]['node']['id']:
                break
        result_switch['Added Switch:'].append((switchid))
    return result_switch
