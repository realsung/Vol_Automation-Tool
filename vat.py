# volatility Automation Script Project
# -*- coding: UTF-8 -*-
# 2018/11/05 START
# How to Use?
# $ python vat.py -f [FILE]

import os
import sys
from optparse import OptionParser 

def getSystemInfo():
	f = open("Analysis.txt")
	for line in f.readlines():
		if(line.find("Suggested")!=-1):
			line = line.split(":")[1]
			line = line.split(",")[0]
			line = line.strip()
			print "[*] System Profile : " + line
			return line

def getSysRegistryInfo():
	f = open("Analysis.txt")
	for line in f.readlines():
		if(line.find("\\REGISTRY\\MACHINE\\SYSTEM")!=-1):
			line = line.split(" ")[0]
			line = line.strip()
			return line

def memoryAnalysis():
	parser = OptionParser('''python vap.py -f [FILE]''')
	parser.add_option("-f","--file",type="string",dest="FILE",help="write report to FILE")
	(option,args) = parser.parse_args()
	
	file = option.FILE

 	if option == None:
		print(parser.usage)
		exit()
	else:
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

		#hivelist
		os.system("echo 6.hivescan >> Analysis.txt")
		os.system("vol.py -f " + file + " hivelist " + profile + " >> Analysis.txt")
		os.system("echo >> Analysis.txt")
		os.system("echo >> Analysis.txt")

		regkey = getSysRegistryInfo()

		#printkey
		#컴퓨터 이름 출력
		os.system("echo 7.Significant Registry  >> Analysis.txt")
		os.system("vol.py -f " + file + " printkey -o " + regkey + " -K \\ControlSet001\\\\Control\\\\ComputerName\\\\ActiveComputerName " + profile + " >> Analysis.txt")
		os.system("echo >> Analysis.txt")
		os.system("echo >> Analysis.txt")

if __name__ == '__main__':
	if(len(sys.argv) <= 1): # 인자 값이 1이상
		print("HELP : python vap.py -h 또는 --help")
		exit()
	else:
		memoryAnalysis()
