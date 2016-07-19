#!/usr/bin/python


import os, datetime, sys, subprocess

isz = ['620', 'HD', 'HDSD']
#isz = ['620', 'HD', 'HDSD']
mons = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']



for y in xrange(len(years)):
	for i in xrange(len(mons)):
		for j in xrange(len(isz)):
			cmd = 'python tavgDriver.py '+years[y]+mons[i]+' '+isz[j]
			subprocess.call(cmd, shell=True)

for y in xrange(len(years)):
	for i in xrange(len(mons)):
		for j in xrange(len(isz)):
			cmd = 'python precipDriver.py '+years[y]+mons[i]+' '+isz[j]
			subprocess.call(cmd, shell=True)
