# volatility Automation Script Project
# -*- coding: UTF-8 -*-
# 2018/11/05 START
# How to Use?
# $ python vat.py -f [FILE]

import os
import sys
import string
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
			print "[*] SYSTEM Registry Virtual Adress : " + line
			return line

def getSoftRegistryInfo():
	f = open("Analysis.txt")
	for line in f.readlines():
		if(line.find("\\SystemRoot\\System32\\Config\\SOFTWARE")!=-1):
			line = line.split(" ")[0]
			line = line.strip()
			print "[*] SOFTWARE Registry Virtual Adress : " + line
			return line

def lastExitRegistryInfo():
	f = open("Analysis.txt")
	info = ""
	for line in f.readlines():
		if(line.find("Last updated:")!=-1):
			info += line.split()[2]
			info += " "
			info += line.split()[3]
			info += " "
			info += line.split()[4]
			print "[*] Computer Last ShutdownTime : " + info
			return info

# def changeTimeInfo():
# 	time = lastExitRegistryInfo()
# 	nt_timestamp = struct.unpack("<Q", unhexlify(time))[0]
# 	epoch = datetime(1601, 1, 1, 0, 0, 0)
# 	nt_datetime = epoch + timedelta(microseconds=nt_timestamp / 10)
# 	print(nt_datetime.strftime("%c"))
# 	#return nt_datetime.strftime("%c")

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

		sysRegkey = getSysRegistryInfo()

		#printkey
		#컴퓨터 이름 출력
		os.system("echo [*]컴퓨터 이름 >> Analysis.txt")
		os.system("vol.py -f " + file + " printkey -o " + sysRegkey + " -K \\ControlSet001\\\\Control\\\\ComputerName\\\\ActiveComputerName " + profile + " >> Analysis.txt")
		os.system("echo >> Analysis.txt")
		os.system("echo >> Analysis.txt")

		os.system("echo [*]시스템 종료 시간 >> Analysis.txt")
		os.system("vol.py -f " + file + " printkey -o " + sysRegkey + " -K \\ControlSet001\\\\Control\\\\Windows " + profile + " >>Analysis.txt")
		os.system("echo >> Analysis.txt")
		os.system("echo >> Analysis.txt")

		lastExitRegistryInfo()

		softRegkey = getSoftRegistryInfo()

		os.system("echo Registry2 >> Analysis.txt")
		os.system("vol.py -f " + file + " printkey -o " + softRegkey + " -K \\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Windows Search " + profile + " >> Analysis.txt")
		os.system("echo >> Analysis.txt")
		os.system("echo >> Analysis.txt")

if __name__ == '__main__':                                        
	rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	print(' __  __             ___                 __              ___              __                      ')
	print('/\ \/\ \           /\_ \               /\ \__    __    /\_ \      __    /\ \__                   ')
	print('\ \ \ \ \    ___   \//\ \       __     \ \ ,_\  /\_\   \//\ \    /\_\   \ \ ,_\   __  __         ')
	print(' \ \ \ \ \  / __`\   \ \ \    /"'"__`\    \ \ \/  \/\ \    \ \ \   \/\ \   \ \ \/  /\ \/\ \      ")
	print('  \ \ \_/ \/\ \L\ \   \_\ \_ /\ \L\.\_   \ \ \_  \ \ \    \_\ \_  \ \ \   \ \ \_ \ \ \_\ \       ')
	print('   \ `\___/\ \____/   /\____\\\ \__/.\_\   \ \__\  \ \_\   /\____\  \ \_\   \ \__\ \/`____ \     ')
	print('    `\/__/  \/___/    \/____/ \/__/\/_/    \/__/   \/_/   \/____/   \/_/    \/__/  `/___/> \     ')
	print('                                                                                      /\___/     ')
	print('                                                                                      \/__/      ')
	print('\t\t     ____                                            ')
	print('\t\t    /\  _`\                                          ')
	print('\t\t    \ \ \L\ \   __      _ __    ____     __    _ __  ')
	print('\t\t     \ \ ,__/ /"'"__`\   /\`'__\ /',__\  /'__`\ /\`'__\\")
	print('\t\t      \ \ \/ /\ \L\.\_ \ \ \/ /\__, `\/\  __/ \ \ \/ ')
	print('\t\t       \ \_\ \ \__/.\_\ \ \_\ \/\____/\ \____\ \ \_\ ')
	print('\t\t        \/_/  \/__/\/_/  \/_/  \/___/  \/____/  \/_/ ')
	print('')
	text = str("")

	if(len(sys.argv) <= 1): # 인자 값이 1이상
		print("HELP : python vap.py -h 또는 --help")
		exit()
	else:
		memoryAnalysis()
