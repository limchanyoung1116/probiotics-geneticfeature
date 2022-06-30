f = open("nodes.dmp","r")
g = open("spiciesURL.txt","r")
h = open("count.txt","w")

genus = ['\t1578\t', '\t2759736\t', '\t2742598\t', '\t2767842\t', '\t2767887\t', '\t1357\t', '\t1301\t', '\t1678\t', '\t1350\t']
line = f.readlines()
nline = len(line)
Lactobacillusspi = list()
Lacticaseibacillusspi = list()
Limosilactobacillusspi = list()
Lactiplantibacillusspi = list()
Ligilactobacillusspi = list()
Lactococcusspi = list()
Streptococcusspi = list()
Bifidobacteriumspi = list()
Enterococcusspi = list()

a = []
for x in range(0, nline):
    num = line[x]
    spid = num.split("|")
    nnum = len(spid)
    for y in range(0, nnum-1):
        if spid[y] == genus[0]:
            speid = spid[y-1]
            Lactobacillusspi.append(speid)
        elif spid[y] == genus[1]:
            speid = spid[y-1]
            Lacticaseibacillusspi.append(speid)
        elif spid[y] == genus[2]:
            speid = spid[y-1]
            Limosilactobacillusspi.append(speid)
        elif spid[y] == genus[3]:
            speid = spid[y-1]
            Lactiplantibacillusspi.append(speid)
        elif spid[y] == genus[4]:
            speid = spid[y-1]
            Ligilactobacillusspi.append(speid)
        elif spid[y] == genus[5]:
            speid = spid[y-1]
            Lactococcusspi.append(speid)
        elif spid[y] == genus[6]:
            speid = spid[y-1]
            Streptococcusspi.append(speid)
        elif spid[y] == genus[7]:
            speid = spid[y-1]
            Bifidobacteriumspi.append(speid)
        elif spid[y] == genus[8]:
            speid = spid[y-1]
            Enterococcusspi.append(speid)

lin = g.readlines()
nlin = len(lin)
n1 = len(Lactobacillusspi)
n2 = len(Lacticaseibacillusspi)
n3 = len(Limosilactobacillusspi)
n4 = len(Lactiplantibacillusspi)
n5 = len(Ligilactobacillusspi)
n6 = len(Lactococcusspi)
n7 = len(Streptococcusspi)
n8 = len(Bifidobacteriumspi)
n9 = len(Enterococcusspi)

Lactosubs1 = list()
Lactisubs2 = list()
Limossubs3 = list()
Lactisubs4 = list()
Ligilsubs5 = list()
Lactosubs6 = list()
Strepsubs7 = list()
Bifidsubs8 = list()
Entersubs9 = list()

for x in range(0, nline):
    num = line[x]
    spid = num.replace("\t","").split("|")
    nnum = len(spid)
    if str(spid[1])+'\t' in Lactobacillusspi:
        speid = spid[0]
        Lactosubs1.append(speid)
    elif str(spid[1])+'\t' in Lacticaseibacillusspi:
        speid = spid[0]
        Lactisubs2.append(speid)
    elif str(spid[1])+'\t' in Limosilactobacillusspi:
        speid = spid[0]
        Limossubs3.append(speid)
    elif str(spid[1])+'\t' in Lactiplantibacillusspi:
        speid = spid[0]
        Lactisubs4.append(speid)
    elif str(spid[1])+'\t' in Ligilactobacillusspi:
        speid = spid[0]
        Ligilsubs5.append(speid)
    elif str(spid[1])+'\t' in Lactococcusspi:
        speid = spid[0]
        Lactosubs6.append(speid)
    elif str(spid[1])+'\t' in Streptococcusspi:
        speid = spid[0]
        Strepsubs7.append(speid)
    elif str(spid[1])+'\t' in Bifidobacteriumspi:
        speid = spid[0]
        Bifidsubs8.append(speid)
    elif str(spid[1])+'\t' in Enterococcusspi:
        speid = spid[0]
        Entersubs9.append(speid)

print(Lactisubs2)

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
cx = 0

for x in range(0,nlin):
    a = lin[x].split("\t")
    na = len(a)
    if na > 1:
        if str(a[6])+'\t' in Lactobacillusspi or str(a[5]) in Lactosubs1 or str(a[6]) in Lactosubs1:    
            c1 += 1
        elif str(a[6])+'\t' in Lacticaseibacillusspi or str(a[5]) in Lactisubs2 or str(a[6]) in Lactisubs2:    
            c2 += 1
        elif str(a[6])+'\t' in Limosilactobacillusspi or str(a[5]) in Limossubs3 or str(a[6]) in Limossubs3:    
            c3 += 1
        elif str(a[6])+'\t' in Lactiplantibacillusspi or str(a[5]) in Lactisubs4 or str(a[6]) in Lactisubs4:    
            c4 += 1
        elif str(a[6])+'\t' in Ligilactobacillusspi or str(a[5]) in Ligilsubs5 or str(a[6]) in Ligilsubs5:    
            c5 += 1
        elif str(a[6])+'\t' in Lactococcusspi or str(a[5]) in Lactosubs6 or str(a[6]) in Lactosubs6:    
            c6 += 1
        elif str(a[6])+'\t' in Streptococcusspi or str(a[5]) in Strepsubs7 or str(a[6]) in Strepsubs7:    
            c7 += 1
        elif str(a[6])+'\t' in Bifidobacteriumspi or str(a[5]) in Bifidsubs8 or str(a[6]) in Bifidsubs8:    
            c8 += 1
        elif str(a[6])+'\t' in Enterococcusspi or str(a[5]) in Entersubs9 or str(a[6]) in Entersubs9:    
            c9 += 1
        else :
            '''print(str(a[5])+'/  '+str(a[6])+'/')'''
            cx += 1
            
h.write("Genus\t\tn of Genomes\n")
h.write("Lactobacillus\t\t")
h.write(str(c1)+"\n")
h.write("Lacticaseibacillus\t")
h.write(str(c2)+"\n")
h.write("Limosilactobacillus\t")
h.write(str(c3)+"\n")
h.write("Lactiplantibacillus\t")
h.write(str(c4)+"\n")
h.write("Ligilactobacillus\t")
h.write(str(c5)+"\n")
h.write("Lactococcus\t\t")
h.write(str(c6)+"\n")
h.write("Streptococcus\t\t")
h.write(str(c7)+"\n")
h.write("Bifidobacterium\t\t")
h.write(str(c8)+"\n")
h.write("Enterococcus\t\t")
h.write(str(c9)+"\n")
h.write("None\t\t\t")
h.write(str(cx)+"\n")
h.write("sum\t\t\t")
h.write(str(c1+c2+c3+c4+c5+c6+c7+c8+c9))

#9개의 genus에 대해 각각의 genome 숫자를 count.txt에 기록.
#이전에 다운받을때속을 구분하지 않고  한번에 뭉뚱그려 다운받았기 때문에
#속을 구분하기 위해 nodes.dmp에서 다시 읽어옴
