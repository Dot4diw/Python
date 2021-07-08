#guosy
from itertools import groupby

id_list = []
id_file = open("id.txt", 'r')
ids = id_file.readlines()
for id in ids:
    id_list.append(id.strip())

# Read the fasta file of input.
def readOffasta(fastafile):                                                        
    file = open(fastafile)
    faiter = (x[1] for x in groupby(file, lambda line : line[0] == ">"))
    for header in faiter:
        head = header.__next__()[1:].strip()
        seq = "".join(s.strip() for s in faiter.__next__())
        yield(head,seq)

fasta_content = readOffasta("test.fa")
for line in fasta_content:
    head, seq = line
    seq_head = ">" + line[0] + "\n"
    oneofseq = line[1] + "\n"
    if head in id_list:
        outfile_name = head +".fa"
        output_fasta = open(outfile_name, 'w')
        output_fasta.writelines(seq_head)
        output_fasta.writelines(oneofseq)
        output_fasta.close()


