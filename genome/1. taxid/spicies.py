f = open("spicesid2.txt","r")
g = open("assembly_summary.txt","r")
h = open("spiciesURL1.txt","w")
F = open("subsubspeciesURL.txt","w")
spe = f.readlines()
nspe = len(spe)
who = g.readlines()
nwho = len(who)

for j in range(0,nspe):
    if "-----" in spe[j]:
        a = j
        break
    for i in range(0,nwho):
        spe[j] = spe[j].replace("\n","")
        if spe[j] in who[i]:
            spiid = who[i].split("\t")
            nspiid = len(spiid)
            print(nspiid)
            for k in range(0,nspiid-1):
                if spiid[k] == spe[j] and spiid[k+1].isdigit() == True:
                    h.write(who[i])

h.write("-"*200+"\n")

# spiciesid2에서---- 위에 있는 Streptococcus에 속하는  id만을 가져오고
# assembly_summary에서 해당되는 genome들의 URL과 정보들을 가져오고 spiciesURL1에 쓰기

for j in range(a+1,nspe):
    for i in range(0,nwho):
        spe[j] = spe[j].replace("\n","")
        if spe[j] in who[i]:기
            spiid = who[i].split("\t")
            nspiid = len(spiid)
            print(nspiid)
            for k in range(0,nspiid-1):
                if spiid[k] == spe[j] and spiid[k+1].isdigit() == True:
                    h.write(who[i])

# 다른 8속에 속하는 id들을 가져오고 assembly_summary에서 genome들 정보들을 가져오기
#이를 Streptococcus와 ----으로 구분하여 spiciesURL1에 쓰기

for j in range(0,nspe):
    if "____"in spe[j]:
        b = j
        break

for j in range(b+1,nspe):
    if "____"in spe[j]:
        c = j
        break
    for i in range(2,nwho):
        spe[j] = spe[j].replace("\n","")
        subid = who[i].split("\t")
        if subid[5] == spe[j]:
            F.write(who[i])

F.write("_"*100+"\n")

for j in range(c+1,nspe):
    for i in range(2,nwho):
        spe[j] = spe[j].replace("\n","")
        stsubid = who[i].split("\t")
        if stsubid[5] == spe[j]:
            F.write(who[i])

# subspecies의 subspecies에 속하는 genome들의 정보를 가져오고, Streptococcus의
# subsubsp들을 ___으로 구분하며 spiciesURL1에 쓰


f.close()
g.close()
h.close()
F.close()
