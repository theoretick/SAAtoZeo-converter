#!/usr/bin/python
# -*- coding: UTF-8 -*-
################################################
#   name: SleepAsAndroid to Zeo Export Converter
#   author: Lucas Charles
#   id: 16mar2013 - ver3
#   desc: Takes SleepasAndroid export CSV as argument
#   and exports ZEO-style CSV
################################################
# todo:
# - call dateformat.py SOMEWHERE
# - calculate sleep stages and add them
# - wtf is ZQ?
################################################
"""
    >>>python saa-to-zeo sleep-export.csv
    "export converted to zeostyle-export.csv"
"""
    
def reorder(unordered, parity):
    # - reorders cols
    # - converts saadata to zeodata
    # - adds new cols
    # movecol => where to move existing cols
    # insertcol => columns to insert and where
    # zerocol => columns that init with zero values (rest: null)
    neworder = []
    movecol = [4,5,2,3]
    insertcol = {'ZQ':1,'Time to Z':2}
    zerocol = ['Rise Time', 'Alarm Reason', 'Snooze Time', 'Wake Tone', 'Wake Window', 'Alarm Type']
    newcol = [
        'First Alarm Ring', 'Last Alarm Ring', 'First Snooze Time', 'Last Snooze Time', 'Set Alarm Time',
        'Morning Feel', 'Day Feel 1', 'Day Feel 2', 'Day Feel 3', 'Notes', 'SS Fall Asleep',
        'SS Anticipation', 'SS Tension', 'SS Comfort', 'SS Noise', 'SS Light', 'SS Temperature',
        'SS Familiar', 'SS Bedroom', 'SS Disruption', 'SS Hot Flashes', 'SS Dreams', 'SS Fullness',
        'SS Hunger', 'SS Heartburn', 'SS Caffeine', 'SS Alcohol', 'SS Thirst', 'SS Restroom', 'SS Wind Down',
        'SS Sleepiness', 'SS Exercise', 'SS Time Before Bed', 'SS Conversations', 'SS Activity Level',
        'SS Late Work', 'SSCF 1', 'SSCF 2', 'SSCF 3', 'SSCF 4', 'SSCF 5', 'SSCF 6', 'SSCF 7', 'SSCF 8',
        'SSCF 9', 'SSCF 10', 'SSCF 11', 'SSCF 12', 'SSCF 13', 'SSCF 14', 'SSCF 15', 'SSCF 16', 'SSCF 17',
        'SSCF 18', 'SSCF 19', 'SSCF 20', 'SSCF 21','Sleep Graph', 'Detailed Sleep Graph']
    for x in movecol:
        neworder.append(unordered[x])

    if parity == 1:
        neworder.extend(zerocol + newcol)
    else:
        neworder.extend(['0' for i in zerocol])
        neworder.extend(['' for i in newcol])
        neworder.append(dataconvert(unordered[9:]))
        
    """
        ########## TESTING PRINT STATEMENTS ##########
        print "max: ",parity,max(unordered[9:])
        print "min: ",parity,min(unordered[9:])
    """

    # Inserts new columns and inits blanks after header
    for x in insertcol.keys():
        if parity % 2 == 1:
            neworder.insert(insertcol.get(x),x)
        else:
            neworder.insert(insertcol.get(x),'')
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

def hours2min(hours):
    fnum = float(hours.strip("\""))*60
    return str(int(round(fnum)))

def dataconvert(saadata):
    """
      takes saadata and converts to zeostyle graph
    """
    import copy

    zeodata = copy.deepcopy(saadata)
    datastr = " ".join(zeodata)
    return datastr


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

