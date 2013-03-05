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
	if 'Total Z' != hours:
		fnum = float(hours.strip("\""))*60
		return str(int(round(fnum)))
	else:
		return hours

def reorder(unordered):
	# reorders columns to zeo format, adds new ones
	# movecol = where to move existing
	# newcol = new cols and where to add
	neworder = []
	movecol = [4,5,2,3]
	newcol = {'ZQ':1,'Time to Z':2}
	for x in movecol:
		neworder.append(unordered[x])
	# add rest of data cols
	neworder.extend(unordered[9:])
	# add new cols
	for x in newcol.keys():
		neworder.insert(newcol.get(x),x)
	return neworder

def reformat(saaformat):
	# retitles columns, calls hours2min(),
	# and returns string
	title = {'Hours':'Total Z','Sched':'Sleep Date','From':'Start of Night','To':'End of Night'}
	zeoformat = []
	zeoformat.extend(saaformat)

	for index, val in enumerate(zeoformat):
		if val in title.keys():
			zeoformat[index] = title.get(val)

	zeoformat[2] = hours2min(zeoformat[2])
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
	# Splits string into orderlist, sends to reorder() & reformat(),
	# appends processed str, and reads next line to process
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

