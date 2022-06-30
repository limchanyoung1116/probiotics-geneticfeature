f = open("subsubspeciesURL.txt","r")
from datetime import datetime
import time

now = datetime.now()
print(now)

lin = f.readlines()
nlin = len(lin)
URL = list()

for i in range(0,nlin):
    x = lin[i].split("\t")
    if x[6] == '1308' or x[4] == 'representative genome':
        URL.append(lin[i])

nURL = len(URL)
URL2 = ['' for i in range (nURL)]
name = ['' for i in range (nURL)]
speid = ['' for i in range (nURL)]
subid = [''for i in range (nURL)]

for i in range(0,nURL):
    a = URL[i].split("\t")
    name[i] = a[0]+"\t"+str(i)+"\t"+a[5]+"\t"+a[7]+"\t"+a[8]
    b = a[19].index("GCF_")
    URL2[i] = str(a[19])+"/"+a[19][b:]+"_"
    speid[i] = int(a[6])+10000000
    subid[i] = int(a[5])+10000000

print(URL2)

import wget, tarfile
import os

g = open("spedictionary.txt","w")
g.write("GCFid\t\tnumber\ttaxnum\tspeciesname\t\tstrain\n")

for i in range(0,nURL):
    g.write(str(name[i])+"\n")

for i in range(0,nURL):

    aa = str(111327+i)[1:]+"_ST_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]

    wget.download(URL2[i]+"cds_from_genomic.fna.gz", out= '/home/cylim/projects/lacto/seqfiles/cds_genomic_fna/N'+aa+"_genomic_fna.fna.gz")
    wget.download(URL2[i]+"genomic.fna.gz", out='/home/cylim/projects/lacto/seqfiles/fna/N'+aa+'_fna.fna.gz')
    wget.download(URL2[i]+"protein.faa.gz", out='/home/cylim/projects/lacto/seqfiles/faa/N'+aa+'_faa.gz')
    wget.download(URL2[i]+"rna_from_genomic.fna.gz", out='/home/cylim/projects/lacto/seqfiles/rna_genomic_fna/N'+aa+'_genomic_faa.faa.gz')
    wget.download(URL2[i]+"translated_cds.faa.gz", out='/home/cylim/projects/lacto/seqfiles/tln_cds_faa/N'+aa+'_cds_faa.faa.gz')
    wget.download(URL2[i]+"genomic.gff.gz", out='/home/cylim/projects/lacto/seqfiles/genomic_gff/N'+aa+'_genomic_gff.gff.gz')

now = datetime.now()
print(now)

# 처음에 누락된 subspecies의 subspecies들의 genome file을 다운로드받고
# dictionaly 파일에 번호 매기기
