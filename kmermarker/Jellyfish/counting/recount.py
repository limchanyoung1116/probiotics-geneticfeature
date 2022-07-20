import os
from datetime import datetime

'''
for i in range(20,26):
   os.system('jellyfish count -m 24 -o {0} -s 100M -t 16 -C {1}'.format('reoutput'+str(i)+'.jf','output'+str(i)+'.fa'))

for i in range(20,26):
    os.system('jellyfish merge reoutput20.jf reoutput21.jf reoutput22.jf reoutput23.jf reoutput24.jf reoutput25.jf -o result.jf')

os.system('jellyfish dump result.jf > result.fa)
'''
print(datetime.now().time())

f0 = open('result.fa','r')
f1 = open('resultt.fa','w')
g0 = f0.readlines()
l0 = len(g0)

for i in range(0,l0):
    if i%2 == 0 and '6' in g0[i]:
        f1.write(">1\n"+g0[i+1])

f0.close()
f1.close()

print(datetime.now().time())

# recount <Jellyfish_count S.thermophilus 6 genome output>
# merge to result.jf and dump to result.fa