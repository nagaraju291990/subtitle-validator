#Processing a srt file for subtitle text extraction
#pip3 install pysrt

import re
import sys
import pysrt

#validator
def validateSRT(filename):
	flag = 1
	no_of_langs = 1
	file = open(filename,"r")
	file_content = file.read()
	file_content = re.sub(r'\n\n','\nSUBTITLE\n', file_content)
	#print(file_content)
	lines = file_content.split("\n")
	line_no = 1
	i = 0
	for l in lines:
		if(line_no == i + 1):
			if(re.match(r'^\d+$', l)):
				flag1 = 1
			else:
				print("Number format mismatch at line:", line_no, l)
				flag = 0

		if(line_no == i + 2):
			if(re.match(r'^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$', l)) :
				flag1 = 1
			else:
				print("Timestamp format mismatch at line:", line_no, l)
				flag = 0

		if(line_no == i + 3 and line_no != len(lines)):
			if(l):
				flag1 = 1
			else:
				print("Text format mismatch at line:", line_no, i)
				flag = 0

		if(line_no == i + 4 and line_no != len(lines)):
			if(l == "SUBTITLE"):
				i = i + 4
				flag1 = 1
			elif(l):
				i = i + 5
			else:
				print("Text format mismatch at line:", line_no, i)
				flag = 0		

		line_no = line_no + 1
	if(flag == 1):
		print( "Validated", "File Format is Okay")
	file.close()

inputfile = sys.argv[1]

validateSRT(inputfile)
