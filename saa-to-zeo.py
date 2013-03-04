#!/usr/bin/python
# -*- coding: UTF-8 -*-
################################################
#	name: SleepAsAndroid to Zeo Export Converter
#	author: Lucas Charles
#	id: 4mar2013 - ver2.5
#	desc: Takes SleepasAndroid export CSV as argument
#	and exports ZEO-style CSV
################################################
# todo:
# - init empty zeo data columns
# - call dateformat.py SOMEWHERE
# - somehow merge 2-row DATA for saa
# - calculate sleep stages and add them
# - wtf is ZQ?
# possibletodo:
# - re-add extra columns to end?
################################################
"""
    >>>python sleepasandroidtozeo sleep-export.csv
    "export converted to zeostyle-export.csv"
"""

def hours2min(hours):
	# for now MUST run before retitle or wont catch new col title
	# scans column, if not 'hours', convert to minutes
	if 'Hours' != hours:
		fnum = float(hours.strip("\""))*60
		return str(int(round(fnum)))
	else:
		return hours

def retitle(title):
	# change this to tuple/dictionary lookup
	if "From" == title:
		return 'Start of Night'
	elif "To" == title:
		return 'End of Night'
	elif "Hours" == title:
		return "Total Z"
	elif "Sched" == title:
		return "Sleep Date"
	else:
		return title

def reorder(unordered):
	order = []
	seq = [4,5,2,3]
	for x in seq:
		order.append(unordered[x])
	order.extend(unordered[9:])
	order.insert(1,"ZQ")
	return order

def reformat(saaformat):
	# envokes hours2min(), retitles() columns, 
	# and returns string
	zeoformat = []
	zeoformat.extend(saaformat)
	zeoformat[2] = hours2min(saaformat[2])
	for i in xrange(11):
		if i != 2:	#so hours2min doesn't get overwritten for now
			zeoformat[i] = retitle(saaformat[i])
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
	# Splits string into orderlist, sends to reorder() and
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

