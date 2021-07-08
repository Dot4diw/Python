#! /mnt/x110/guosy/miniconda2/envs/python3/bin/python
#@Author : Dot4diw
#@Time : 4/7/2020
#@Function : Compare the editing type of mirme result with SNP type of dbSNP database.

import os
import time
import argparse


def compareEditingType():
    compareDict={
            "C->A":["G->T","C->A"],"C->G":["G->C","C->G"],"C->U":["G->A","C->T"],
            "G->A":["C->T","G->A"],"G->C":["G->C","C->G"],"G->U":["G->T","C->A"],
            "U->A":["T->A","A->T"],"U->G":["T->G","A->C"],"U->C":["T->C","A->G"],
            "A->U":["A->T","T->A"],"A->G":["A->G","T->C"],"A->C":["A->C","T->G"],
            "C->-":["C->-","T->-","G->-","A->-"],"U->-":["C->-","T->-","G->-","A->-"],
            "G->-":["C->-","T->-","G->-","A->-"],"A->-":["C->-","T->-","G->-","A->-"],
            "-->A":["NA->NA"],
            "-->G":["NA->NA"],
            "-->C":["NA->NA"],
            "-->U":["NA->NA"]
			}
    with open('compare_editing_type_result.txt','w') as resultOutPutFile:
        #resultOutPutFile.writelines("".join(['ME_ID','\t','CHROM','\t',Position,'\t','REF','\t','ALT','\t','Compare-Result','\n']))
        with open('target_dbsnp_overlap.txt','r') as inputFile:
            for line in inputFile:  
                line_list=line.strip().split('\t')
                if(len(line_list) < 7):
                    ME_ID=line_list[0] + '_' + line_list[1] + '_' + line_list[2] + '_' + line_list[3]
                    WT_Nucl = line_list[2].upper()
                    ME_Nucl = line_list[3].upper()
                    ME_Type=WT_Nucl[0] + '->' + ME_Nucl[0]
                    CHROM = "Chr" + line_list[4]
                    Position = 'NA'
                    dbSNP_ID = 'NA'
                    REF = 'NA'
                    ALT = 'NA'
                else:
                    ME_ID=line_list[0] + '_' + line_list[1] + '_' + line_list[2] + '_' + line_list[3]
                    WT_Nucl = line_list[2].upper()
                    ME_Nucl = line_list[3].upper()
                    ME_Type=WT_Nucl[0] + '->' + ME_Nucl[0]
                    CHROM = "Chr" + line_list[4]
                    Position = line_list[5]
                    dbSNP_ID = line_list[6]
                    REF = line_list[7]
                    ALT = line_list[8]
                
                #Generate the SNP_MU list
                SNP_MU=[]
                if ((len(ALT) > 1 and (',' not in ALT)) or len(REF) > 1):
                    ALT="NA"
                    REF="NA"
                    SNP_MU=["NA->NA"]
                else:
                    for i in ALT.split(',') :
                        everyALT=REF[0] + '->' + i
                        SNP_MU.append(everyALT)
                judgement=[]
                for i in SNP_MU:
                    if(i in compareDict[ME_Type]):
                            judgement.append('T')
                    else:
                        judgement.append('F')
                if "T" in judgement:
                    result=ME_ID + '\t' + CHROM + '\t' + Position + '\t' + REF + '\t' + ALT +'\t' +"SNP "+dbSNP_ID
                else:
                    result=ME_ID + '\t' + CHROM + '\t' + Position + '\t' + REF + '\t' + ALT +' \t' + "NA"
            
                print(result)
                resultOutPutFile.writelines(''.join([result,'\n']))
                #print(len(line_list))
                '''
                if len(line_list) > 9 and len(result.strip().split('\t')[5]) == 2:
                    resultOutPutFile.writelines(''.join([result,'\t','NOT_SNP_Douplict_Site','\t','\n']))
                else:
                    resultOutPutFile.writelines(''.join([result,'\n']))
                '''


def checkRepeatIdOfSNP(snp_overlap):
    # Wrap SNPs with the same ME_ID to indicate
    with open ("target_dbsnp_overlap.txt", 'w') as outfile:
        with open (snp_overlap,'r') as infile:
            
            for each_line in infile:
              
                l_list=each_line.strip().split('\t')
                if len(l_list) > 9:    
                    id_list = l_list[:4]
                    t_list = l_list[4:]
                    ME_ID = id_list[0] + '\t' + id_list[1] + '\t' + id_list[2] + '\t' + id_list[3]
                    count = 0
                    string = ''
                    for i in t_list:
                        string = string + i + '\t'
                        count += 1
                        if count % 5 == 0 and count == 5:
                            new_line = ME_ID + '\t' + string
                            outfile.writelines(''.join([new_line,'\n']))
                            string = ''
                        elif count % 5 == 0 and count > 5:
                            new_line = ME_ID + '\t' + string
                            outfile.writelines(''.join([new_line,'\t','Dublict_ID','\n']))
                            string = ''
                        else:
                            pass
                else:
                    #each_line = each_line + '\t' + 'Duplict_ID' + '\n'
                    #outfile.writelines(''.join([each_line.strip(),"\t","Not_Duplict_ID","\n"]))
                    outfile.writelines(''.join([each_line.strip(),"\n"]))
                    #outfile.writelines(''.join([each_line]))
                

def checkEditingLevel(me_percent):
    with open("Check_editing_level_result.txt",'w') as resultOfCheck:
        with open(me_percent,'r') as inputFile:
            count = 0
            for line in inputFile:
                lineList = line.strip().split('\t')
                ME_ID = lineList[0]
                countOf1 = lineList.count('1')
                countOf05 = lineList.count('0.5')
                if (countOf1 > 2 ):
                    result = "Credible"
                    count += 1
                else:
                    result = "No Credible"
                print(ME_ID + '\t' + result)
                resultOfCheck.writelines("".join([ME_ID,'\t',result,'\n']))
            print(count)
    
def main():
    parser = argparse.ArgumentParser(description = '\nThis script is used to screening for SNP sites by compare Mirme result wiht dbSNP type.', add_help = False, usage = '\npython3 @*.py -S [input.snp_overlapfile] -M [input.me_percent] \npython3 @*.py --snp_overlpa [input.snp_overlap] --me_percent [output.me_percent]')
    parser.add_argument('-S', '--snp_overlap', dest='SNP_Overlap', required = True, metavar = '[snp_overlap]', help = 'Input file of SNP overlap generate by awk-update.sh')
    parser.add_argument('-M', '--me_percent', dest='Me_Percent',required = True, metavar = '[ME_Percent]', help = 'Input file of ME_Percent file with ME_ID')
    parser.add_argument('-h', '--help', action = 'help', help = 'Help Information:')
    args = parser.parse_args()
    pwd=os.getcwd()
    os.chdir(pwd)
    checkRepeatIdOfSNP(args.SNP_Overlap)
    compareEditingType()
    checkEditingLevel(args.Me_Percent)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('Running time: %s Seconds' % (end_time - start_time))
