#
#
"""
    >>>python sleepasandroidtozeo sleep-export.csv
    "export converted to zeostyle-export.csv"

	name: SleepAsAndroid to Zeo Export Converter
	date: 21feb2013 - ver1
	desc: Takes SleepasAndroid export CSV as argument and exports ZEO-style CSV

################
todo:
+ delete ID
+ del TZ
- del Rating
- del Comments
- del Framerate
- move OLD-col4 (SchedT, 0-inclusive) to index[0]
- multiply Hours by 60
- move OLD-col5 (Hours, 0-inc) to index[2]
"""

import sys

SAAINFILE = sys.argv[1]

infile = open(SAAINFILE,'r')
outfile = open("zeostyle-export.csv",'w')

instr = infile.readline()
recordcount = 0
outlist = []

while instr:
	orderedlinelist = []
	linelist = instr.split(",")
	del linelist[0:2]
	del linelist[5:7]
	orderedlinelist.append(linelist.pop(2))
	print orderedlinelist
	orderedlinelist.extend(linelist[:])
	newlinestr = ",".join(orderedlinelist)
	outlist.append(newlinestr)
	instr = infile.readline()

outstr = "\n".join(outlist)

outfile.write(outstr)
infile.close()
outfile.close()

