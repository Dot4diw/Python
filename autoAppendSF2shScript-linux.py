# -*- coding:utf-8 -*-
# /bin/usr/python
# @Author : dot4diw
# @Build time : Saturday 3/2020
# @Function : Auto Applent the sam file name to the Applend-the-sam.filter.sh shell script

import os
import sys
import argparse

# Define a class of output redirection.
class RedirectStdout():
	def __init__(self):
		self.content = ''
		self.standard_output = sys.stdout
		self.fileObj = None

	def write(self, outStr):
		self.content += outStr

	def toConsole(self):
		sys.stdout = self.standard_output

	def toFile(self, file):
		self.fileObj = open(file, 'a+')
		sys.stdout = self.fileObj

	def restore(self):
		self.content = ''
		if self.fileObj.closed != True:
			self.fileObj.close()
		sys.stdout = self.standard_output

def Generatescript(inputfile):
	id_arry = []
	with open(inputfile, 'r') as f:
		for line in f.readlines():
			id_arry.append(line.strip())

	for i in range(len(id_arry)):
		if i == len(id_arry) - 1:
			break
		else:
			print("java jsmallrna8.ncrna.AppendSplitSAM -i %s -I %s " % (id_arry[i],id_arry[i+1]))

# Define the main function and get the arguments of python script.
def main():
	parser = argparse.ArgumentParser
	parser = argparse.ArgumentParser(description = " Append the split sam file name to the java sccript and combine to shell script.", add_help = False, usage = '\npython autoAppendSF2shScript.py -i [inputfile] -o [outputfile]\npython autoAppendSF2shScript.py --input [inputfile] --output [outputfile]')
	parser.add_argument('-i', '--input', type = str, default = None, help = "The input file of script." )
	parser.add_argument('-o', '--output', type = str, default = "appendSplitsam.sh", help = "The output file of the script.")
	parser.add_argument('-h', '--help', action = 'help', help = 'Help Information:')

	args = parser.parse_args()
	redirObj = RedirectStdout()
	redirObj.toFile(args.output)
	Generatescript(args.input)
	redirObj.restore()

if __name__ == "__main__":
	main()


