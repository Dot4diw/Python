#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author : dot4diw
# @Filename : filterLengthOfreads-unix.py
# @Time : 3/2020
# @Function : Filter the reads length of *fastq files.


import time
import argparse

parser = argparse.ArgumentParser(description = '\nThis script is used to filter the *.fastq files reads by length', add_help = False, usage = '\npython3 filterLength.py -i [input.fastq] -m [minLenght] -M [maxLength] -o [output.fastq] \n')
parser.add_argument('-i', '--input', metavar = '[input.fastq]', help = 'Input file in fastq format.')
parser.add_argument('-o', '--output', metavar = '[output.fastq]', help = 'Output file in fastq format.')
parser.add_argument('-m', '--min', metavar = '[minLenght]', help = 'Input the minLength of reads.')
parser.add_argument('-M', '--max' ,metavar = '[maxLength]',help = 'Input the maxLength of reads.')
parser.add_argument('-h', '--help', action = 'help', help = 'Help Information:')
args = parser.parse_args()

def filterReads():
	with open(args.output, 'w') as output_fastq:
		with open(args.input,'r') as input_fastq:
			for line in input_fastq:
				try:
					headinfo = line
					sequence = input_fastq.__next__()
					comment = input_fastq.__next__()
					quality = input_fastq.__next__()
				except  StopIteration:
					break
				if ( int(args.min) <= len(sequence)<= int(args.max)):
					output_fastq.write(headinfo)
					output_fastq.write(sequence)
					output_fastq.write(comment)
					output_fastq.write(quality)
					
				else:
					pass

def main():
    filterReads()

if __name__ == '__main__':
	start_time = time.time()
	main()
	end_time = time.time()
	print('Running time: %s Seconds' % (end_time - start_time))
