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

import sys

SAAINFILE = sys.argv[1]

infile = open(SAAINFILE,'r')
outfile = open("zeostyle-export.csv",'w')

instr = infile.readline()
outlist = []

while instr:
	orderedlinelist = []
	linelist = instr.split(",")
	del linelist[0:2]
	del linelist[4:7]
	orderedlinelist.append(linelist.pop(2))
	orderedlinelist.extend(linelist[:])
 	if "Hours" not in orderedlinelist[3]:
 		orderedlinelist[3] = str(int(round(float(orderedlinelist[3].strip("\""))*60)))
	newlinestr = ",".join(orderedlinelist)
	outlist.append(newlinestr)
	instr = infile.readline()

outstr = "\n".join(outlist)

outfile.write(outstr)
infile.close()
outfile.close()

