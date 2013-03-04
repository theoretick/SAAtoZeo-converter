#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    >>>datetimeformatter("09. 11. 2012 03:30")
    11/09/2012 03:30
"""

def datetimeformatter(date):
	pass #DONT USE TILL FIXED
	zdatelist = []
	datelist = date.split()
	for i, element in enumerate(datelist):
		datelist[i](element.strip('.'))
	zdatelist = datelist.pop([1])
	if len(datelist[2]) < 5:
		datelist[2] = '0'+datelist[2]
	zdatelist.extend = datelist[:]
	zyearstr = '\/'.join(zdatelist[0:3])
	zdatestr = zyearstr + str(zdatelist[3])
	return zdatestr

def dateformatter(date):
	pass