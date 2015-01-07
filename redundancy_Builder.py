from flow_finder import flow_finder
from time import ctime
from extract_redundancy import extract_redundancy
import datetime
def redundancy_Builder():
        redundancy=[]
	print '[Redundancy Builder]'+ctime()
        print 'Start to read the redundancy configuration file.'
        input = open('redundancytable.txt', 'r')
        input.readline()
        while 1:
                line=input.readline()
                if not line:
                        break
                formated_redundancy=extract_redundancy(line)
                redundancy.append(formated_redundancy)
        input.close()
        return redundancy
