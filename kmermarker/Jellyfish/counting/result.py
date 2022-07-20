import os
from datetime import datetime
'''
os.system("bash retest2_1.sh")'''
os.system("jellyfish count -m 24 -s 100M -t 16 -o resultt.jf -C output20.fa")

for i in range(0,20):
    os.system("jellyfish merge resultt.jf outputx2_{}.jf -o resulttt.jf".format(i))
    os.system("jellyfish dump resulttt.jf > resulttt.fa")
    f = open("resulttt.fa","r")
    g = f.readlines()
    l = len(g)
    f1 = open("resultttt.fa","w")
    for i in range (0,l):
        if i%2 == 0 and '1' in g[i]:
            f1.write(str(g[i])+str(g[i+1]))
    f.close()
    os.system("rm resulttt.fa resulttt.jf resultt.jf")
    os.system("jellyfish count -m 24 -s 100M -t 16 -o resultt.jf -C resultttt.fa")
    f1.close()
    os.system("rm resultttt.fa")

# output 20 is S.thermophilus
# find k-mer present in S.thermophilus and absent in other 20 Streptococcus
