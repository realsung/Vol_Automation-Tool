# volatility Automation Script Project
# -*- coding: UTF-8 -*-
# 2018/11/05 START
# How to Use?
# $ python vap.py -f [FILE]

import os
import sys
from optparse import OptionParser 
if(len(sys.argv) <= 1): # 인자 값이 1이상
	print("HELP : python vap.py -h 또는 --help")
	exit()

def getSystemInfo():
	f = open("Analysis.txt")
	for line in f.readlines():
		if(line.find("Suggested")!=-1):
			line = line.split(":")[1]
			line = line.split(",")[0]
			line = line.strip()
			print "[*] System Profile : " + line

			return line

parser = OptionParser('''python vap.py -f [FILE]''')
parser.add_option("-f","--file",type="string",dest="FILE",help="write report to FILE")
(option,args) = parser.parse_args()

file = option.FILE

if option == None:
	print(parser.usage)
	exit()

if option != None:

	# imageinfo
	os.system("echo 1.imageinfo ================================== > Analysis.txt")
	os.system("vol.py -f " + file + " imageinfo >> Analysis.txt")
	profile = "--profile="
	profile += getSystemInfo()
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")

	# psxview
	os.system("echo 2.psxview ================================== >> Analysis.txt")
	os.system("vol.py -f " + file + " psxview " + profile + " >> Analysis.txt")
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")

	# pstree
	os.system("echo 3.pstree ===================================== >> Analysis.txt")
	os.system("vol.py -f " + file + " pstree " + profile + " >> Analysis.txt")
	os.system("echo >> Analysis.txt")
	os.system("echo >> Analysis.txt")
	
