#!/usr/bin/python3

#@author: dot4diw

import os
import time
import pandas as pd

path = os.getcwd()
os.chdir(path)
dirs = os.listdir(path) 

def get_srr_id():
    outid_file =  open("srr_index_id.txt", 'w')
    with open("path.txt", 'r') as infile:
        for line in infile:
            line_list = line.strip().split("/")
            formatList = list({}.fromkeys(line_list).keys())
            for list_str in formatList:
                if "SRR" in list_str:
                    srr_id = list_str.split("_")[0] + "\t" + line
                    outid_file.write(srr_id)
                else:
                    pass
    outid_file.close()

srrid_list = []
def get_tmp_file():
    path_index = open("srr_index_id.txt",'r') 
    for line in path_index:
        line_list = line.strip().split("\t")
        srrid_list.append(line_list[0])

        tmp_filename = line_list[0] + "_A-to-I.tmp"
        result_path = line_list[1]
        tmp_file = open(tmp_filename, 'w')
        with open(result_path, 'r') as re_file:
            for each_line in re_file:
                content_list = each_line.strip().split("\t")
                tmp_content = content_list[0] + "," + content_list[1] + "," + content_list[2] + "\t" + content_list[3] + "," +  content_list[4] + "," + content_list[5] + "," + content_list[6] + "\n"
                tmp_file.write(tmp_content)

        tmp_file.close()
    path_index.close()                

def merge_result():
    data_list = []
    header = "Chr\tLocation(0base)\tLocation(1base)"

    header_out = open("combine_result_header.txt", 'w')
    for tmp in srrid_list:
        infile = tmp.strip() + "_A-to-I.tmp"
        header = header + "\t" + tmp.strip() + "_Type\t" + tmp.strip() + "_Supporting-info\t" + tmp.strip() + "_Strand\t" + tmp.strip() + "AD:DP"
        df_tmp = pd.read_table(infile, sep='\t',header=None,index_col=0)
        data_list.append(df_tmp)

    print (header)
    header_out.write(header + "\n" )
    header_out.close()
    df = pd.concat(data_list, sort=False, axis=1)
    df.to_csv('PD_Sprint-Summary-new.txt', sep='\t', header=None, na_rep='NA,NA,NA,NA')

def convert_to_table():
    os.system("sed 's/,/\t/g' PD_Sprint-Summary-new.txt > PD_SPRINT_Combine")
    os.system("cat combine_result_header.txt PD_SPRINT_Combine > PD_Sprint_Combine.result")

def main():
    get_srr_id()
    get_tmp_file()
    merge_result()
    convert_to_table()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("Total running time Run : %d s" % (end_time -start_time))

