from flow_finder import flow_finder
from extract_loadbalancer import extract_loadbalancer
import datetime
def loadbalancer_Builder():
	loadbalancers=[]
	input = open('loadbalancertable.txt', 'r')
	input.readline()
	while 1:
		line=input.readline()
		if not line:
				break
		formated_loadbalancer=extract_loadbalancer(line)
		loadbalancers.append(formated_loadbalancer)
	input.close()
	return loadbalancers
