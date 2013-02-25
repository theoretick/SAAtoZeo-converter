################################################
#	name: SleepAsAndroid to Zeo Export Converter
#	author: Lucas Charles
#	id: 22feb2013 - ver2
#	desc: Takes SleepasAndroid export CSV as argument
#	and exports ZEO-style CSV
################################################
# todo:
# - init empty zeo data columns
# - somehow merge 2-row DATA (time+data) for saa
# - re-add extra columns to end?
# - calculate sleep stages and add them
# - wtf is ZQ?
################################################
"""
    >>>python sleepasandroidtozeo sleep-export.csv
    "export converted to zeostyle-export.csv"
"""

def dateformatter(date):
	pass

def hours2min(hours):
	# for now MUST RUN BEFORE retitle or wont catch new col title
	if 'Hours' not in hours:
		flnum = float(hours.strip("\""))*60
		return str(int(round(flnum)))
	else:
		return hours

def retitle(title):
	# change this to tuple/dictionary lookup
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

def reorder(unordered):
	order = []
	seq = [4,2,3,5]
	for x in seq:
		order.append(unordered[x])
	order.extend(unordered[9:])
	return order

def reformat(saaformat):
	# envokes hours2min(), retitles() columns, and returns string

	zeoformat = []
	zeoformat.extend(saaformat)
	zeoformat[3] = hours2min(saaformat[3])
	for i in xrange(3):
		zeoformat[i] = retitle(saaformat[i])
	zeoformat[3] = retitle(zeoformat[3])
	return ",".join(zeoformat)

import string
import sys

SAAINFILE = sys.argv[1]
outlist = []
outname = 'zeostyle-export.csv'

infile = open(SAAINFILE,'r')
outfile = open(outname,'w')
instr = infile.readline()

while instr:
	# Splits string into reinitialized orderlist, sends to reorder() and
	# reformat() then appends processed str and reads next line to process
	orderedline = []

	linelist = instr.split(",")
	orderedline = reorder(linelist)
	newlinestr = reformat(orderedline)
	outlist.append(newlinestr)
	instr = infile.readline()

outstr = "\n".join(outlist)
outfile.write(outstr)

print "Done. exported to %s" % outname

infile.close()
outfile.close()

