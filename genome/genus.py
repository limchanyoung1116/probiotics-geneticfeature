f = open("nodes.dmp","r")

line = f.readlines()

nline = len(line)
species = list()
genus = ['\t2759736\t', '\t2742598\t', '\t2767842\t', '\t2767887\t', '\t1357\t', '\t1578\t', '\t1678\t', '\t1350\t']
genusstr = ['\t1301\t']
strepto = list()

# Streptococcus와 다른 8genus의 NCBI taxid를 담은 리스트 생성

g = open("spicesid2.txt","w")

for x in range(0, nline):
    num = line[x]
    spid = num.split("|")
    nnum = len(spid)
    for y in range(0, nnum-1):
        if spid[y] in genus :
            speid = spid[y-1].replace('\t','')
            species.append(speid)
        if spid[y] in genusstr :
            strepid = spid[y-1].replace('\t','')
            strepto.append(strepid)

# 계통 정보를 담고 있는 nodes.dmp 파일에서, Streptococcus와 8genus의 하위 종들의
# NCBI taxid를 읽어와 리스트에 저장

nspecies = len(species)
nstrepto = len(strepto)

subsp = list()
strsub = list()

for x in range(0, nline):
    num = line[x]
    subid = num.replace("\t","").split("|")
    nnum = len(subid)
    for y in range(0, nnum-1):
        if subid[y] in species and y != 0:
            subsp.append(subid[y-1])
        elif subid[y] in strepto and y != 0:
            strsub.append(subid[y-1])

# 8genus에 속하는 species들의 taxid list로 node.dmp에서 subspecies id를 찾고
# 이를 빈 리스트에 더함

a = len(species)
b = len(subsp)
c = len(strepto)
d = len(strsub)

for x in range(0,c):
    g.write(strepto[x])
    g.write("\n")
for x in range(0,d):
    g.write(strsub[x])
    g.write("\n")

g.write("-"*10)

for x in range(0,a):
    g.write(species[x])
    g.write("\n")
for x in range(0,b):
    g.write(subsp[x])
    g.write("\n")

g.write("_"*20+"\n")

subsubsp = list()
strsubsub = list()

for x in range(0, nline):
    num = line[x]
    subsubid = num.replace("\t","").replace("\n","").split("|")
    nnum = len(subsubid)
    if subsubid[1] in subsp:
        subsubsp.append(subsubid[0])
    elif subsubid[1] in strsub:
        strsubsub.append(subsubid[0])

A = len(subsubsp)
B = len(strsubsub)

# subspecies들에 속하는 다른 subspecies들의 id를 list에 기록

for x in range(0,A):
    g.write(subsubsp[x]+"\n")
g.write("_"*20+"\n")
for x in range(0,B):
    g.write(strsubsub[x]+"\n")

f.close()
g.close()

#리스트들에 담긴 id를 spiciesid2.txt에 전부 기록.
#Streptococcus는 representative genome만을 다운받아야 하므로 ---와 ___으로 구분
