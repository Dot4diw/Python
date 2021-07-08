# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : dot4diw
# @Build time : 3/2020
# @Function : Extract specific sequences from the genome based on blast information
# @Note : Please use the python3 to run the script.


# Import the python-module.

from itertools import groupby
import time 
import sys
import os
import argparse

# Get the arguments of script.
parser = argparse.ArgumentParser
parser = argparse.ArgumentParser(description = '\nThis script is used to intercept sequences at specific locations in the genome. An additional list file containing the intercepted sequence information is required.', add_help = False, usage = '\npython3 seq_select.py -i [input.fasta] -o [output.fasta] -l [list]\npython3 seq_select.py --input [input.fasta] --output [output.fasta] --list [list]')
parser.add_argument('-i', '--input', metavar = '[input.fasta]', help = 'Input file in fasta format',)
parser.add_argument('-o', '--output', metavar = '[output.fasta]', help = 'Output file in fasta format.')
parser.add_argument('-b', '--blast', metavar = '[input.blast]', help = 'Input file of that records the new sequence name, the original sequence ID where the sequence is located, the sequence start position, the sequence end position, and the positive (+) and negative (-) chains, separated by tabs')
parser.add_argument('-h', '--help', action = 'help', help = 'Help Information:')
args = parser.parse_args()

# Read and write the fasta txt.
def read_and_write_fasta():
	with open(args.output, 'w') as output_fasta_content:
		with open (args.blast, 'r') as blastfile:
			fasta_content = readOffasta(args.input)
			for line in fasta_content:
				head, seq = line
				seq_head = ">"+ line[0]
				oneofseq = line[1]
				for line_blast in blastfile:
					inFor_blast=getlistOfblast(line_blast)# Need to return querry_id, seq_id, start_position, end_position, seq_type. 

					if inFor_blast[4] == 'reverser' and inFor_blast[1] == seq_head.split('>')[1]:
						reverse_complementary_seq = get_reverse_seq(oneofseq)# Need to return reverse_seq
						extract_seq = extract_fasta(reverse_complementary_seq,inFor_blast[2],inFor_blast[3]) # Need to return extrac fasta seq
						inFor_blast_start_position = str(inFor_blast[2])
						inFor_blast_end_position = str(inFor_blast[3])
						output_fasta_content.writelines(''.join([seq_head, ' ', inFor_blast[0], ' ', inFor_blast_start_position, ' ', inFor_blast_end_position,'\n', extract_seq, '\n']))
					elif inFor_blast[4] == 'forward' and inFor_blast[1] == seq_head.split('>')[1]:
						extract_seq = extract_fasta(oneofseq,inFor_blast[2],inFor_blast[3]) # Need to return extrac fasta seq
						inFor_blast_start_position = str(inFor_blast[2])
						inFor_blast_end_position = str(inFor_blast[3])
						output_fasta_content.writelines(''.join([seq_head, ' ', inFor_blast[0], ' ', inFor_blast_start_position, ' ', inFor_blast_end_position,'\n', extract_seq, '\n']))
					else:
						pass




# Read the fasta file of input.
def readOffasta(fastafile):
	file = open(fastafile)
	faiter = (x[1] for x in groupby(file, lambda line : line[0] == ">"))
	for header in faiter:
		head = header.__next__()[1:].strip()
		seq = "".join(s.strip() for s in faiter.__next__())
		yield(head,seq)

# Get the information from blast file
def getlistOfblast(line):
	line_list = line.strip().split('\t') 
	qurry_id = line_list[0]
	seq_id = line_list[1]
	start_position = int(line_list[8])
	end_position = int(line_list[9])
	if start_position <= end_position:
		seq_type = 'forward'
	else:
		seq_type = 'reverse'
		temp_position = start_position
		start_position = end_position
		end_position = temp_position
	return qurry_id,seq_id,start_position,end_position,seq_type


# Get the reverse complementary sequence
def get_reverse_seq(original_seq):
	base_complementary_pairing_dic = {'A':'T', 'C':'G', 'T':'A', 'G':'C', 'a':'t', 'c':'g', 't':'a', 'g':'c'}
	rev_Original_seq = list(reversed(original_seq))
	reverse_complementary_seq_list = []
	for key in rev_Original_seq:
		reverse_complementary_seq_list.append(base_complementary_pairing_dic[key])
	reverse_complementary_seq = "".join(reverse_complementary_seq_list)
	return reverse_complementary_seq

	
# Specific target sequences are extracted from the sequence of the genome file according to the blast file.
def extract_fasta(sequence,start_position,end_position):
	extract_seq_list = []
	sequence_list = list(sequence)
	for i in range(start_position - 1 , end_position):
		extract_seq_list.append(sequence_list[i])

	extract_seq = "".join(extract_seq_list)
	return extract_seq

def main():
	read_and_write_fasta()

if __name__ == '__main__':
	start_time = time.time()
	main()
	end_time = time.time()
	print('Running time: %s Seconds' % (end_time - start_time))

