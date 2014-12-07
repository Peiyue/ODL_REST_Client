def switch_index_new=find_switch(switchid_old,data_new):
		numofswitchs_old=len(data['portStatistics'])
		for oldswitchindex in rang(numofswitchs_old)
			if switchid_old=data_new['portStatistics'][oldswitchindex]['node']['id']
				return oldswitchindex
				break
		return 'switch removed'