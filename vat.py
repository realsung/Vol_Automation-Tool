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
	f = open("analysis.txt")
	for line in f.readlines():
		if(line.find("Suggested")!=-1):
			line = line.split(":")[1]
			line = line.split(",")[0]
			line = line.strip()
			print("[*] System Profile : " + line)

			return line

parser = OptionParser('''python vap.py -f [FILE]''')
parser.add_option("-f","--file",type="string",dest="FILE",help="write report to FILE")
parser.add_option("-o","--object",type="string",dest="object",help="write report to ADDRESS")
(option,args) = parser.parse_args()

file = option.FILE

if option == None:
	print(parser.usage)
	exit()


if option.object == None:
	os.system("echo 1.imageinfo ================================== > analysis.txt")
	os.system("vol.py -f " + file + " imageinfo >> analysis.txt")
	info = "--profile="
	info += getSystemInfo()
	os.system("echo >> analysis.txt")

