#!/usr/bin/python

import urllib
import sys
import time
#import subprocess
from apcaccess import status as apc

#from subprocess import check_output
#out = subprocess.check_output(["apcaccess"])

ThingSpeakURL = "https://api.thingspeak.com/update?api_key=HN8U6AUCC50NL75P"
ThingSpeakResponse = -1
#TestMode = 0
TestMode = int(sys.argv[1])
ProgramLogFileName = "/home/pi/apc/apc.log"

#spl = [ele.split(":",1)for ele in out.splitlines()]
#ups = {k.strip():v.strip() for k,v in spl}
ups = apc.parse(apc.get(),True)

#ups['LINEV'] = ups['LINEV'].strip(' Volts')
#ups['LOADPCT'] = ups['LOADPCT'].strip(' Percent')
#ups['BCHARGE'] = ups['BCHARGE'].strip(' Percent')
#ups['TIMELEFT'] = ups['TIMELEFT'].strip(' Minutes')
#ups['BATTV'] = ups['BATTV'].strip(' Volts')

if TestMode == 1:
	print "Status            : ", ups['STATUS']
	print "Input Voltage     : ", ups['LINEV']
	print "Load %            : ", ups['LOADPCT']
	print "Battery Charge    : ", ups['BCHARGE']
	print "Runtime Left      : ", ups['TIMELEFT']
	print "Battery Voltage   : ", ups['BATTV']

if ups['STATUS'] == "ONLINE":
	Field1 = "0"
else:
	Field1 = "1"
Field2 = ups['LINEV']
Field3 = ups['LOADPCT']
Field4 = ups['TIMELEFT']
Field5 = ups['BCHARGE']
Field6 = ups['BATTV']

ThingSpeakURL = ThingSpeakURL + "&field1=" + Field1 + "&field2=" + Field2 + "&field3=" + Field3 + "&field4=" + Field4 + "&field5=" + Field5 + "&field6=" + Field6

if TestMode == 0:
	ThingSpeakResponse = urllib.urlopen(ThingSpeakURL).read()

if TestMode == 1:
	print ThingSpeakURL

ProgramLogFile = open(ProgramLogFileName,"a")
ProgramLogFile.write (time.asctime() + " -----Program start-----\n")
ProgramLogFile.write (time.asctime() + " TestMode: " + str(TestMode) + "\n")
ProgramLogFile.write (time.asctime() + " ThingSpeakURL: " + ThingSpeakURL + "\n")
ProgramLogFile.write (time.asctime() + " ThingSpeakResponse: " + str(ThingSpeakResponse) + "\n")
ProgramLogFile.write (time.asctime() + " -----Program finish-----\n")
ProgramLogFile.close()
