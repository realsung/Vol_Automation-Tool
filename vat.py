# volatility Automation Script Project
# -*- coding: UTF-8 -*-
# 2018/11/05 START
# How to Use?
# $ python vat.py -f [FILE]

import os
import sys
import urllib
from optparse import OptionParser 

parser = OptionParser('''python vat.py -f [FILE]\npython vat.py -f [FILE] -o [Object]''')
parser.add_option("-f","--file",type="string",dest="FILE",help="write report to FILE")
parser.add_option("-o","--object",type="string",dest="object",help="write Address")
(option,args) = parser.parse_args()
	
file = option.FILE

if(len(sys.argv) <= 1): # 인자 값이 1이상
	print("HELP : python vat.py -h 또는 --help")
	exit()

if option == None:
	print(parser.usage)
	exit(0)

def getSystemInfo():
	f = open("Analysis.txt")
	for line in f.readlines():
		if(line.find("Suggested")!=-1):
			line = line.split(":")[1]
			line = line.split(",")[0]
			line = line.strip()
			print "[*] System Profile : " + line
			return line

def getMalInfo(procName):
    f = open("Analysis.txt.txt")
    list1 = []
    for line in f.readlines():
        if(line.find("Process")!=-1):
            if(line.find("explorer.exe")!=-1):
                line = line.split(":")
                pid = line[2].split(" ")[1]
                addr = line[3].strip()
                list1.append([pbid, addr])
    return list1

def getProcInfo(obj):
    f = open("Analysis.txt.txt")
    for line in f.readlines():
        if(line.find(obj)!=-1):
            line = line.split(" ")[1]
            line = line.strip()
            print "[*] Process Name of Obejct : " + line
            return line


if option.object == None:
	# imageinfo
	os.system("echo 1.imageinfo >> Analysis.txt")
	os.system("vol.py -f " + file + " imageinfo >> Analysis.txt")
	profile = "--profile="
	profile += getSystemInfo()
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")

	# psxview
	os.system("echo 2.psxview >> Analysis.txt")
	os.system("vol.py -f " + file + " psxview " + profile + " >> Analysis.txt")
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")

	# pstree
	os.system("echo 3.pstree >> Analysis.txt")
	os.system("vol.py -f " + file + " pstree " + profile + " >> Analysis.txt")
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")

	#netscan
	os.system("echo 4.netscan >> Analysis.txt")
	os.system("vol.py -f " + file + " netscan " + profile + " >> Analysis.txt")
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")
else:
	obj = option.object
	profile = "--profile="
	profile += getSystemInfo
	procName = getProcInfo(obj)
	malfindInfo = getMalInfo(procName)

	filename = obj + ".txt"

	os.system("echo object = " + obj + " > " + filename)
	os.system("echo 1.mftparser >> " + filename)
	os.system("vol.py -f " + file + " mftparser "+ profile + " | grep -i " + procName[:5] + " >> " + filename)
	os.system("echo >> " + filename)
	os.system("echo >> " + filename)

	os.system("echo 2.dlllist >> " + filename)
	os.system("vol.py -f " + file + " dlllist -o " + obj + " " + profile + " >> " + filename)
	os.system("echo >> " + filename)
	os.system("echo >> " + filename)

	os.system("echo 3.dlldump with malfind >> " + filename)
	if (malfindInfo != ()):
	     for list1 in malfindInfo:
	        os.system("vol.py -f " + vmem + " dlldump -p " + list1[0] + " -b  " + list1[1] + " " + info + " --dump-dir=./ >> " + filename )

		os.system("vol.py -f " + vmem + " procdump -D ./ -o " + obj + " " + info + " >> " + filename)
	os.system("echo >> " + filename)
	os.system("echo >> " + filename)

	os.system("echo 3.strings  >> " + filename)
	os.system("strings *.exe >> " + filename)
	os.system("echo >> " + filename)
	os.system("echo >> " + filename)

	urllib.urlopen("http://www.virustotal.com")
