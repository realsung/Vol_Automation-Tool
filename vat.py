# volatility Automation Script Project
# -*- coding: UTF-8 -*-
# 2018/11/05 START
# How to Use?
# $ python vat.py -f [FILE]
# v1.0

import os
import sys
from optparse import OptionParser 
if(len(sys.argv) <= 1): # 인자 값이 1이상이여야 한다.
	print("HELP : python vat.py -h 또는 --help")
	exit()

parser = OptionParser('''python vat.py -f [FILE]''')
parser.add_option("-f","--file",type="string",dest="FILE",help="write report to FILE")
(option,args) = parser.parse_args()

file = option.FILE

if option == None:
	print(parser.usage)
	exit()

if option.FILE:
	print os.system("vol.py -f " + file + " imageinfo > " + file + "_imageinfo.txt")
	# print os.system("vol.py -f " + file + " pstree > " + file + "_pstree.txt")
	# print os.system("vol.py -f " + file + " netscan > " + file + "_netscan.txt")
	# print os.system("vol.py -f " + file + " mfsparser > " + file + "_mfsparser.txt")
	# print os.system("vol.py -f " + file + " filescan > " + file + "_filescan.txt")