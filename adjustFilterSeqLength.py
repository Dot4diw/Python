#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@dot4diw/
#@adjust the fastq file length of seq and filter the seq length/
#@18/12/2020

import os
import time 
import argparse

def adjust_filter_seq(infastq, outfastq, targetlength, minlength, maxlength):
    with open(outfastq, 'w') as outfile:
        with open(infastq, 'r') as infile:
            for line in infile:
                try:
                    headinfo = line
                    sequence = infile.__next__().strip()
                    comment = infile.__next__()
                    quality = infile.__next__()
                except:
                    break

                seqlength = len(sequence)
                if ( int(minlength) <= seqlength <= int(maxlength) ):
                    
                    if ( seqlength == 100 ):
                        headinfo_split = headinfo.split(" ")
                        headinfo_af = headinfo_split[0] + " " + headinfo_split[1] + " " + "length="+targetlength+"\n"
                        sequence_af = sequence[0:int(targetlength)] + "\n"
                        comment_split = comment.split(" ")
                        comment_af = comment_split[0] + " " + comment_split[1] + " " + "length="+targetlength+"\n"
                        quality_af = quality[0:int(targetlength)] + "\n"

                        outfile.write(headinfo_af)
                        outfile.write(sequence_af)
                        outfile.write(comment_af)
                        outfile.write(quality_af)

                    elif ( seqlength == 99 ):
                        headinfo_split = headinfo.split(" ")
                        headinfo_af = headinfo_split[0] + " " + headinfo_split[1] + " " + "length="+targetlength+"\n" 
                        sequence_af = sequence[0:int(targetlength)] + "\n"
                        comment_split = comment.split(" ")
                        comment_af = comment_split[0] + " " + comment_split[1] + " " + "length="+targetlength+"\n"
                        quality_af = quality[0:int(targetlength)] + "\n"
                        
                        outfile.write(headinfo_af)
                        outfile.write(sequence_af)
                        outfile.write(comment_af)
                        outfile.write(quality_af)
                        
                    elif ( seqlength == int(targetlength) ):
                        outfile.write(headinfo)
                        outfile.write(sequence + "\n")
                        outfile.write(comment)
                        outfile.write(quality)
                    
                    else:
                        pass
                else:
                    pass


def main():
    parser = argparse.ArgumentParser(description = '\nThis script is used to adjust and filter the *.fastq files reads by length', add_help = False, usage = '\npython3 filterLength.py -i [input.fastq] -m [minLenght] -M [maxLength] -o [output.fastq] \n')
    parser.add_argument('-i', '--input', dest = 'inputfile', required = True, metavar = '[input.fastq]', help = 'Input file in fastq format.')
    parser.add_argument('-o', '--output', dest = 'outputfile', required = True, metavar = '[output.fastq]', help = 'Output file in fastq format.')
    parser.add_argument('-l', '--length', dest = 'target_length', required = True, metavar = 'targetLength', help = 'The target length of reads.')
    parser.add_argument('-m', '--min', dest = 'min_length', required = True, metavar = '[minLength]', help = 'Input the minLength of reads.')
    parser.add_argument('-M', '--max' ,dest = 'max_length', required = True, metavar = '[maxLength]',help = 'Input the maxLength of reads.')
    parser.add_argument('-h', '--help', action = 'help', help = 'Help Information:')
    args = parser.parse_args()
    
    pwd = os.getcwd()
    os.chdir(pwd)
    adjust_filter_seq(args.inputfile, args.outputfile, args.target_length, args.min_length, args.max_length)
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('Runnign time : %s Seconds' % ( end_time - start_time))
    
