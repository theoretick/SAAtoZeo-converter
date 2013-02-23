# 	name: SleepAsAndroid to Zeo Export Converter
#   author: Lucas Charles
#	id: 22feb2013 - ver2
#	desc: Takes SleepasAndroid export CSV as argument and exports ZEO-style CSV
"""
    >>>python sleepasandroidtozeo sleep-export.csv
    "export converted to zeostyle-export.csv"
################
todo:
- multiply Hours by 60
- somehow merge time+data for saa
- re-add extra columns to end?
- calculate sleep stages and add
- wtf is ZQ?
"""

def dateformatter(date):
	pass

def hours2min(hours):
	# for now MUST RUN BEFORE RETITLE OR WONT CATCH NEW TITLE
	if 'Hours' not in hours:
		flnum = float(hours.strip("\""))*60
		return str(int(round(flnum)))
	else:
		return hours

def retitle(title):
	if "From" in title:
		return 'Start of Night'
	elif "To" in title:
		return 'End of Night'
	elif "Hours" == title:
		return "Total Z"
	elif "Sched" == title:
		return "Sleep Date"
	else:
		return title

import sys
from copy import deepcopy

SAAINFILE = sys.argv[1]

infile = open(SAAINFILE,'r')
outfile = open("zeostyle-export.csv",'w')

instr = infile.readline()
outlist = []

while instr:
	orderedline = []
	formatline = []
	linelist = instr.split(",")
	del linelist[0:2]
	del linelist[4:7]
	orderedline.append(linelist.pop(2))
	orderedline.extend(linelist[:])
	formatline.extend(orderedline)
	formatline[3] = hours2min(orderedline[3])
	for i in range(3):
		formatline[i] = retitle(orderedline[i])
	formatline[3] = retitle(formatline[3])
	newlinestr = ",".join(formatline)
	outlist.append(newlinestr)
	instr = infile.readline()

outstr = "\n".join(outlist)

outfile.write(outstr)
infile.close()
outfile.close()

