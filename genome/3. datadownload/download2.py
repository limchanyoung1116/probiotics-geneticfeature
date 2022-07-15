f = open("8genusURL_aa.txt","r")
from datetime import datetime
import time

now = datetime.now()
print(now)

lin = f.readlines()
nlin = len(lin)
URL = ['' for i in range(nlin)]
URL2 = ['' for i in range(nlin)]
name = ['' for i in range(nlin)]
speid = ['' for i in range (nlin)]
subid = [''for i in range (nlin)]

for i in range(0,nlin):
    a = lin[i].index("https://")
    b = len(lin[i])
    for j in range(a,b):
        c = lin[i][a:b].index("\t")
        URL[i] = lin[i][a:a+c]
    d = lin[i].split("\t")
    name[i] = d[0]+"\t"+str(i+283)+"\t"+d[5]+"\t"+d[7]+"\t"+d[8]+"\n"
    speid[i] = int(d[6])+10000000
    subid[i] = int(d[5])+10000000


for i in range(0,nlin):
    a = URL[i].index("GCF_")
    nURL = len(URL[i])
    URL2[i] = URL[i][a:nURL]
    URL[i] = URL[i]+'/'+URL2[i]+'_'


import wget, tarfile
import os

g = open("spedictionary.txt","a")


h = open("nodes.dmp","r")
H = h.readlines()
nH = len(H)
    
genus = ['2759736', '2742598', '2767842', '2767887', '1357', '1578', '1678', '1350']

class genusfinder:
    def species(self,first,second,third,forth):
        self.first = first
        self.second = second
        if self.first == self.second:
            third.append(str(forth))

Lac1 = list()       #2759736
Lim2 = list()       #2742598
Lac3 = list()       #2767842
Lig4 = list()       #2767887
Lac5 = list()       #1357
Lac6 = list()       #1578
Bif7 = list()       #1678
Ent8 = list()       #1350

for i in range(0,nH):
    gen = H[i].replace("\t","").split("|")
    LC = genusfinder()
    LC.species('2759736',str(gen[1]),Lac1,gen[0])
    LS = genusfinder()
    LS.species('2742598',str(gen[1]),Lim2,gen[0])
    LP = genusfinder()
    LP.species('2767842',str(gen[1]),Lac3,gen[0])
    LG = genusfinder()
    LG.species('2767887',str(gen[1]),Lig4,gen[0])
    LT = genusfinder()
    LT.species('1357',str(gen[1]),Lac5,gen[0])
    LB = genusfinder()
    LB.species('1578',str(gen[1]),Lac6,gen[0])
    BF = genusfinder()
    BF.species('1678',str(gen[1]),Bif7,gen[0])
    ET = genusfinder()
    ET.species('1350',str(gen[1]),Ent8,gen[0])

length = [len(Lac1),len(Lim2),len(Lac3),len(Lig4),len(Lac5),len(Lac6),len(Bif7),len(Ent8)]

ALac1 = list()       #2759736
ALim2 = list()       #2742598
ALac3 = list()       #2767842
ALig4 = list()       #2767887
ALac5 = list()       #1357
ALac6 = list()       #1578
ABif7 = list()       #1678
AEnt8 = list()       #1350


for i in range(0,nH):
    gen = H[i].replace("\t","").split("|")
    for j in range(0,int(length[0])):
        LC = genusfinder()
        LC.species(str(Lac1[j]),str(gen[1]),ALac1,gen[0])
    for j in range(0,int(length[1])):
        LS = genusfinder()
        LS.species(str(Lim2[j]),str(gen[1]),ALim2,gen[0])
    for j in range(0,int(length[2])):
        LP = genusfinder()
        LP.species(str(Lac3[j]),str(gen[1]),ALac3,gen[0])
    for j in range(0,int(length[3])):
        LG = genusfinder()
        LG.species(str(Lig4[j]),str(gen[1]),ALig4,gen[0])
    for j in range(0,int(length[4])):
        LT = genusfinder()
        LT.species(str(Lac5[j]),str(gen[1]),ALac5,gen[0])
    for j in range(0,int(length[5])):
        LB = genusfinder()
        LB.species(str(Lac6[j]),str(gen[1]),ALac6,gen[0])
    for j in range(0,int(length[6])):
        BF = genusfinder()
        BF.species(str(Bif7[j]),str(gen[1]),ABif7,gen[0])
    for j in range(0,int(length[7])):
        ET = genusfinder()
        ET.species(str(Ent8[j]),str(gen[1]),AEnt8,gen[0])

Lac1 = Lac1 + ALac1
Lim2 = Lim2 + ALim2
Lac3 = Lac3 + ALac3
Lig4 = Lig4 + ALig4
Lac5 = Lac5 + ALac5
Lac6 = Lac6 + ALac6
Bif7 = Bif7 + ABif7
Ent8 = Ent8 + AEnt8


for i in range(0,nlin):
    if str(subid[i]-10000000) in Lac1:
        aa = str(100000+i+8283)[1:]+"_LC_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Lim2:
        aa = str(100000+i+8283)[1:]+"_LS_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Lac3:
        aa = str(100000+i+8283)[1:]+"_LP_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Lig4:
        aa = str(100000+i+8283)[1:]+"_LG_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Lac5:
        aa = str(100000+i+8283)[1:]+"_LT_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Lac6:
        aa = str(100000+i+8283)[1:]+"_LB_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Bif7:
        aa = str(100000+i+8283)[1:]+"_BF_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]
    elif str(subid[i]-10000000) in Ent8:
        aa = str(100000+i+8283)[1:]+"_ET_s"+str(speid[i])[1:]+"_u"+str(subid[i])[1:]

    wget.download(URL[i]+"assembly_report.txt", out= '/home/cylim/projects/lacto/seqfiles/report_txt/N'+aa+"_report.txt")

    wget.download(URL[i]+"cds_from_genomic.fna.gz", out= '/home/cylim/projects/lacto/seqfiles/cds_genomic_fna/N'+aa+"_genomic_fna.fna.gz")
    wget.download(URL[i]+"genomic.fna.gz", out='/home/cylim/projects/lacto/seqfiles/fna/N'+aa+'_fna.fna.gz')
    wget.download(URL[i]+"protein.faa.gz", out='/home/cylim/projects/lacto/seqfiles/faa/N'+aa+'_faa.gz')
    wget.download(URL[i]+"rna_from_genomic.fna.gz", out='/home/cylim/projects/lacto/seqfiles/rna_genomic_fna/N'+aa+'_genomic_faa.faa.gz')
    wget.download(URL[i]+"translated_cds.faa.gz", out='/home/cylim/projects/lacto/seqfiles/tln_cds_faa/N'+aa+'_cds_faa.faa.gz')
    wget.download(URL[i]+"genomic.gff.gz", out='/home/cylim/projects/lacto/seqfiles/genomic_gff/N'+aa+'_genomic_gff.gff.gz')


now = datetime.now()
print(now)


# aa 4000개, ab 4000개, ac 약3000개로 나뉜 8genus의 URL을 읽고,
# fna, faa, 등등 7가지 파일을 다운로드받으면서 dictionaly에 번호를 매긴다.
# aa, ab, ac를 바꿀 때 283, 4283, 8283으로 숫자를 바꾸고 여는 파일만 
# aa ab ac로 바꿔주면 된다.
