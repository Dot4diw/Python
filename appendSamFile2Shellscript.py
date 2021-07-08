#######################################################################
# -*- coding:utf-8 -*-
# /bin/usr/python
# @Author : dot4diw
# @Build Time :  Saturday February 29,2020
# @Function : Aplend the sam file to the Applend-the-sam.file.sh file.
#######################################################################
"""
import sys

class Logger(object):
    def __init__(self, fileName = "Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileName, "a")
        
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        
    def flush(self):
        pass



sys.stdout = Logger("D:\\Python\\appendSF2Script.sh")
"""

import sys
import os

id_array = []
filepath = os.getcwd()
inputfile = filepath + '/ID'
outputfile = filepath + '/appendSF2Script.sh'

standard_output = sys.stdout
sys.stdout = open(outputfile ,"w+")
                  
with open(inputfile,'r') as f:
    for line in f.readlines():
        id_array.append(line.strip())

for i in range(len(id_array)):
    if i == (len(id_array) - 1):
        break
    else:
        print("java jsmallrna8.ncrna.AppendSplitSAM -i %s -I %s " % (id_array[i],id_array[i+1]))
        
sys.stdout.close()
sys.stdout = standard_output


                  
