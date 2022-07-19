f1 = open("k19inter.gff","r")
f2 = open("k22inter.gff","r")
f3 = open("k25inter.gff","r")
g1 = f1.readlines()
g2 = f2.readlines()
g3 = f3.readlines()
l1 = len(g1)
l2 = len(g2)
l3 = len(g3)

ff = open("gene.txt","w")

ff.write("start\tend\tgene\n")
ff.write("k=19\n")

start = list()
end = list()
name = list()


for i in range(0,l1):
    g1s = g1[i].split("\t")
    if "gene" in g1s[2]:
        start.append(g1s[3])
        end.append(g1s[4])
        k = g1[i].index("ID")
        a = ''
        for j in range(k,k+30):
            if g1[i][j] != ";":
                a = a + g1[i][j]
            else :
                break
        name.append(a)

x = len(start)

for i in range(0,x-1):
    if name[i] == name[i+1]:
        start[i+1] = start[i]
    elif name[i] != name[i+1]:
        ff.write(start[i]+"\t"+end[i]+"\t"+name[i]+"\n")
ff.write(start[x-1]+"\t"+end[x-1]+"\t"+name[x-1]+"\n")


ff.write("k=22\n")
start = list()
end = list()
name = list()


for i in range(0,l2):
    g1s = g2[i].split("\t")
    if "gene" in g1s[2]:
        start.append(g1s[3])
        end.append(g1s[4])
        k = g2[i].index("ID")
        a = ''
        for j in range(k,k+30):
            if g2[i][j] != ";":
                a = a + g2[i][j]
            else :
                break
        name.append(a)

x = len(start)

for i in range(0,x-1):
    if name[i] == name[i+1]:
        start[i+1] = start[i]
    elif name[i] != name[i+1]:
        ff.write(start[i]+"\t"+end[i]+"\t"+name[i]+"\n")
ff.write(start[x-1]+"\t"+end[x-1]+"\t"+name[x-1]+"\n")


ff.write("k=25\n")
start = list()
end = list()
name = list()


for i in range(0,l3):
    g1s = g3[i].split("\t")
    if "gene" in g1s[2]:
        start.append(g1s[3])
        end.append(g1s[4])
        k = g3[i].index("ID")
        a = ''
        for j in range(k,k+30):
            if g3[i][j] != ";":
                a = a + g3[i][j]
            else :
                break
        name.append(a)

x = len(start)

for i in range(0,x-1):
    if name[i] == name[i+1]:
        start[i+1] = start[i]
    elif name[i] != name[i+1]:
        ff.write(start[i]+"\t"+end[i]+"\t"+name[i]+"\n")
ff.write(start[x-1]+"\t"+end[x-1]+"\t"+name[x-1])

