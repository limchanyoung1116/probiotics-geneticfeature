# /home/cylim/projects/lacto/jellyfish/jelly_faa_file

import glob

A = []
B = '0001308'
C = []

for i in range(0, 180):
    A.append('N' + str(100000 + i)[1:] + '_')

for i in range(0, 180):
    file = glob.glob('/home/cylim/projects/lacto/jellyfish/jelly_faa_files/{}*.fna'.format(A[i]))
    if B not in file[0]:
        C.append(str(file[0]))

c = len(C)

import os

for i in range(0,c):
    os.system('jellyfish count -m 24 -o {0} -s 100M -t 16 -C {1}'.format('output'+str(i)+'.jf',C[i]))

for i in range(0,c):
    os.system('jellyfish dump {0} > {1}'.format('output'+str(i)+'.jf','output'+str(i)+'.fa'))

# glob N00001 ~ N000180 20 non thermophilus Streptococcus and do Jellyfish