#!/usr/bin/python
# -*- coding: UTF-8 -*-
################################################
#   name: SleepAsAndroid to Zeo Export Converter
#   author: Lucas Charles
#   id: 4mar2013 - ver2.5
#   desc: Takes SleepasAndroid export CSV as argument
#   and exports ZEO-style CSV
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
    fnum = float(hours.strip("\""))*60
    return str(int(round(fnum)))
    
def reorder(unordered, parity):
    # reorders columns to zeoformat & adds new
    # movecol = where to move existing cols
    # newcol = new cols and where to add
    neworder = []
    movecol = [4,5,2,3]
    newcol = {'ZQ':1,'Time to Z':2}
    for x in movecol:
        neworder.append(unordered[x])

    neworder.extend(unordered[9:])

    for x in newcol.keys():
        if parity % 2 == 1:
            neworder.insert(newcol.get(x),x)
        else:
            neworder.insert(newcol.get(x),'')
    return neworder

def reformat(saaformat, parity):
    # retitles columns, calls hours2min(),
    # and returns string
    title = {'Hours':'Total Z','Sched':'Sleep Date','From':'Start of Night','To':'End of Night'}
    zeoformat = []
    zeoformat.extend(saaformat)

    for index, val in enumerate(zeoformat):
        if val in title.keys():
            zeoformat[index] = title.get(val)
    if parity > 1:
        zeoformat[2] = hours2min(zeoformat[2])
    return ",".join(zeoformat)

import string
import sys

########## Init variables
SAAINFILE = sys.argv[1]
outlist = []
outname = 'zeostyle-export.csv'
oddcounter = 0

##########
infile = open(SAAINFILE)
outfile = open(outname,'w')
instr = infile.readline()

while instr:
    # Splits string into list, send to reorder() & reformat(),
    # appends processed str, and reads next line to process
    oddcounter += 1

    if  (oddcounter % 2 == 0) or (oddcounter == 1):
        orderedlineA = []
        listA = instr.split(",")
        orderedlineA = reorder(listA, oddcounter)
        newlinestr = reformat(orderedlineA, oddcounter)
        outlist.append(newlinestr)
    instr = infile.readline()

outstr = "\n".join(outlist)
outfile.write(outstr)

print "Done. exported to {}".format(outname)

infile.close()
outfile.close()

