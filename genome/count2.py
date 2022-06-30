f = open("19pro.txt","r")
g = f.readlines()
l = len(g)
ff = open("count.txt","a")
f1 = open("nodes.dmp","r")
g1 = f1.readlines()
l1 = len(g1)
f2 = open("spiciesURL.txt","r", encoding='UTF-8')
g2 = f2.readlines()
l2 = len(g2)
F = 0

spename = list()
speid = list()

for i in range(0,l):
    A = g[i].replace("\n","").split("\t")
    if len(A)>1:
        spename.append(A[0])
        speid.append(A[1])

lspe = len(speid)
subid = list()
subsubid = list()
print(speid)

for k in range(0,l2):
    C = g2[k].split("\t")
    if len(C)>4:
        globals()['D{}'.format(k)] = C[5]
        globals()['E{}'.format(k)] = C[6]
    else :
        globals()['D{}'.format(k)] = ''
        globals()['E{}'.format(k)] = ''

for i in range(0,lspe):
    for j in range(0,l1):
        B = g1[j].replace("\t","").split("|")
        if len(B)>5 and B[1] == speid[i]:
            subid.append(B[0])
    l3 = len(subid)
    print(subid)
    for y in range(0,l2):
        if str(globals()['D{}'.format(y)]) in subid or str(globals()['E{}'.format(y)])==str(speid[i]) or str(globals()['D{}'.format(y)])==str(speid[i]):
            F += 1
    subid = list()
    ff.write('\n')
    ff.write(spename[i])
    ff.write('\t')
    ff.write(str(F))
    F = 0

f.close()
f1.close()
ff.close()
f2.close()

#19종의probiotics들의 taxid가 쓰인 파일을 읽어오고, 이를 dictionaly에서 세어
#각probiotics  species별로 몇 번씩 등장하는지 count
