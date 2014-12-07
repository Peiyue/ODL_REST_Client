def check_old_switches(data_old,data_new,result_switch):
    numofoldswitches=len(data_old['portStatistics'])
    numofnewswitches=len(data_new['portStatistics'])
    for switchindex in range(numofoldswitches):
        switchid=data_old['portStatistics'][switchindex]['node']['id']
        #check if a previous switch exist
        for i in range(numofnewswitches):
            if switchid==data_new['portStatistics'][i]['node']['id']:
                           
                break
            else:
                result_switch['Deleted Switch:'].append(switchid)
    return result_switch
