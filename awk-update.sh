#!/usr/bin/bash
# Dot4diw
#README
#Input files of shell script: All_20180418.vcf Compare-NSCLC-to-SNP.txt Compare-NSCLC-to-SNP.txt(pyhton script)

for i in `seq 1 22` X
do
    awk '$1=="'$i'"{print $1"\t"$2"\t"$3"\t"$4"\t"$5}' All_20180418.vcf > chr"$i".txt
    #grep -w "chr"$i Check-SNP.txt | cut -f 5 > tmp.pos
    grep -w "chr"$i Compare-NSCLC-to-SNP.txt | awk '{print $1"\t"$6}' > tmp.pos

    ODL_IFS=$IFS
    IFS=$'\n'
    for s in `cat tmp.pos`
    do
        id=`echo $s | awk '{print $1}'`
        position=`echo $s | awk '{print $2}'`
        echo -n -e "$id\t" >> overlap.txt
        snpinfo=`grep -w $position "chr"$i".txt"`
        if [ -z "$snpinfo" ]
        then
            echo "NA" >> overlap.txt
        else
            echo $snpinfo >> overlap.txt
        fi

    done
    IFS=$OLD_IFS
done
sed -i.bak 's/_/\t/g' overlap.txt && sed 's/ /\t/g' overlap.txt >> snp_overlap.txt
python3 compareEditingTypeOfMirmeAnddbSNP-Unix.py -S snp_overlap -M ME_Percent_By_ID.txt

#rm tmp.pos
