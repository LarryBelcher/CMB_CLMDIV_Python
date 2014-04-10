#!/usr/bin/python


import os, sys, time, subprocess


###Check the avg temp file
cmd = 'curl ftp://ftp.ncdc.noaa.gov/pub/data/cirs/climdiv/ | grep tmpcdv'
proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
serverfilename = out.split()[8]
fileurl = 'ftp://ftp.ncdc.noaa.gov/pub/data/cirs/climdiv/'+serverfilename
serverfiledate = int(out.split('-')[9])

cmd = 'ls ./Data/*tmpcdv*'
proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
localfilename = out
clientfiledate = int(out.split('-')[3])

if(serverfiledate != clientfiledate):
	cmd = 'rm '+localfilename
	os.system(cmd)
	cmd = 'wget '+fileurl
	os.system(cmd)
	cmd = 'mv '+serverfilename+' ./Data/'
	os.system(cmd)
	
	
###Check the avg temp file
cmd = 'curl ftp://ftp.ncdc.noaa.gov/pub/data/cirs/climdiv/ | grep pcpndv'
proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
serverfilename = out.split()[8]
fileurl = 'ftp://ftp.ncdc.noaa.gov/pub/data/cirs/climdiv/'+serverfilename
serverfiledate = int(out.split('-')[9])

cmd = 'ls ./Data/*pcpndv*'
proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
localfilename = out
clientfiledate = int(out.split('-')[3])

if(serverfiledate != clientfiledate):
	cmd = 'rm '+localfilename
	os.system(cmd)
	cmd = 'wget '+fileurl
	os.system(cmd)
	cmd = 'mv '+serverfilename+' ./Data/'
	os.system(cmd)