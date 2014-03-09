import sys, filecmp, getopt

"""
This Script is used to find the difference between two files with the below details:
	1. Confirms the status of the differences
	2. Lists the common lines between two files
	3. Lists the lines unique to file1
	4. Lists the lines unique to file2
"""

def usage():
	usage_string = """
		This Script is used to find the difference between two files.
		USAGE: fileCompare.py <file1> <file2>
		"""
	print usage_string

if sys.argv[1:] == []:
	usage()
	sys.exit()
else:	
	file_a = sys.argv[1]
	file_b = sys.argv[2]

file_ah = open(file_a, 'r+w')
lines_a = file_ah.readlines()
file_ah.close()
file_bh = open(file_b, 'r+w')
lines_b = file_bh.readlines()
file_bh.close()

common = []
only_in_a = []
only_in_b = []

if filecmp.cmp(file_a, file_b) is False:
	print "Status: Files differ"
	for i in lines_a:
		if i in lines_b:
			common.append(i.strip("\r\n"))
	for i in lines_a:
		if i not in lines_b:
			only_in_a.append(i.strip("\r\n"))
	for i in lines_b:
		if i not in lines_a:
			only_in_b.append(i.strip("\r\n"))
else:
	print "Status: Files are identical"

if len(common) != 0:
	print "Common lines between %s and %s are:" %(file_a, file_b)
	for lines in common:
		print lines
if len(only_in_a) != 0:
	print "Lines unique to %s" %file_a
	for lines in only_in_a:
		print lines
if len(only_in_b) != 0:
	print "Lines unique to %s" %file_b
	for lines in only_in_b:
		print lines
