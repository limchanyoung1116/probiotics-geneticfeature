'''
f1 = open("./ST26fna/k10/consolidated/consolidated.fasta","r")
f2 = open("./ST26fna/k13/consolidated/consolidated.fasta","r")
f3 = open("./ST26fna/k16/consolidated/consolidated.fasta","r")
f4 = open("./ST26fna/k19/consolidated/consolidated.fasta","r")
f5 = open("./ST26fna/k22/consolidated/consolidated.fasta","r")
f6 = open("./ST26fna/k25/consolidated/consolidated.fasta","r")
f7 = open("./ST26fna/k28/consolidated/consolidated.fasta","r")

ff = open("ST26fnagrp.csv","w")

g1 = f1.read().split(">")
g2 = f2.read().split(">")
g3 = f3.read().split(">")
g4 = f4.read().split(">")
g5 = f5.read().split(">")
g6 = f6.read().split(">")
g7 = f7.read().split(">")

ff.write("neptune seq length/score graph by kmer\n")
for i in range(1,8):
    ff.write("k = {0}\n".format(7+i*3))
    l = len(globals()["g{}".format(i)])
    G = globals()["g{}".format(i)]
    ff.write(",length,score\n")
    print(l)
    if l>1:    
        for j in range(1,l):
            n = G[j].index("score")
            o = G[j].index("len")
            p = G[j].index("in")
            q = G[j].index("ref")
            ff.write("{0},{1},{2}\n".format(G[j][0:n-1],G[j][n:p-1].replace("score=",""),G[j][o:q-1].replace("len=","")))
    ff.write("\n")
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
ff.close()
'''

f1 = open("./ST26cds/k10/consolidated/consolidated.fasta","r")
f2 = open("./ST26cds/k13/consolidated/consolidated.fasta","r")
f3 = open("./ST26cds/k16/consolidated/consolidated.fasta","r")
f4 = open("./ST26cds/k19/consolidated/consolidated.fasta","r")
f5 = open("./ST26cds/k22/consolidated/consolidated.fasta","r")
f6 = open("./ST26cds/k25/consolidated/consolidated.fasta","r")
f7 = open("./ST26cds/k28/consolidated/consolidated.fasta","r")

ff = open("ST26cdsgrp.csv","w")

g1 = f1.read().split(">")
g2 = f2.read().split(">")
g3 = f3.read().split(">")
g4 = f4.read().split(">")
g5 = f5.read().split(">")
g6 = f6.read().split(">")
g7 = f7.read().split(">")

ff.write("neptune seq length/score graph by kmer\n")
for i in range(1,8):
    ff.write("k = {0}\n".format(7+i*3))
    l = len(globals()["g{}".format(i)])
    G = globals()["g{}".format(i)]
    ff.write(",length,score\n")
    print(l)
    if l>1:
        for j in range(1,l):
            n = G[j].index("score")
            o = G[j].index("len")
            p = G[j].index("in")
            q = G[j].index("ref")
            ff.write("{0},{1},{2}\n".format(G[j][0:n-1],G[j][n:p-1].replace("score=",""),G[j][o:q-1].replace("len=","")))
    ff.write("\n")
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()

