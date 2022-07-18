import os
import glob

F = glob.glob("./STgff/N*")
L = len(F)

for i in range(0,L):
    f1 = open(F[i],"r")
    f2 = open("./STfna/"+F[i][8:-15]+"fna.fna","r")
    g1 = f1.read()
    g2 = f2.read()
    f3 = open("./STgffna/"+F[i][8:],"w")
    f3.write(g1)
    f3.write("##FASTA\n")
    f3.write(g2)
