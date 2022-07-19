f = open("gene.txt","r")
g = f.readlines()
l = len(g)
f2 = open("cluster.txt","w")

for i in range(0,l):
    if g[i] == "k=19\n":
        a = i
    elif g[i] == "k=22\n":
        b = i
    elif g[i] == "k=25\n":
        c = i

start19 = [0 for i in range(b-a-2)]
print("cluster_interval : ")
inter = input()

for i in range(a+1,b):
    A = g[i].split("\t")
    globals()['aa{}'.format(i)] = A[0]
    globals()['bb{}'.format(i)] = A[1]

for i in range(b+1,c):
    B = g[i].split("\t")
    globals()['cc{}'.format(i)] = B[0]
    globals()['dd{}'.format(i)] = B[1]

for i in range(c+1,l):
    C = g[i].split("\t")
    globals()['ee{}'.format(i)] = C[0]
    globals()['ff{}'.format(i)] = C[1]

x = 0

for i in range(a+2,b-1):
    if int(globals()['bb{}'.format(i-1)]) + int(inter) >= int(globals()['aa{}'.format(i)]): 
        g[i] = str(g[i]).replace("\n","\tcluster\n")

for i in range(a+1,b-1):
    if "cluster\n" not in g[i] and "cluster\n" in g[i+1]:
        g[i] = str(g[i]).replace("\n","\tcluster{0}\n".format(x))
        x = x+1


y = 0

for i in range(b+2,c-1):
    if int(globals()['dd{}'.format(i-1)]) + int(inter) >= int(globals()['cc{}'.format(i)]):
        g[i] = str(g[i]).replace("\n","\tcluster\n")

for i in range(b+1,c-1):
    if "cluster\n" not in g[i] and "cluster\n" in g[i+1]:
        g[i] = str(g[i]).replace("\n","\tcluster{0}\n".format(y))
        y = y+1

z = 0

for i in range(c+2,l):
    if int(globals()['ff{}'.format(i-1)]) + int(inter) >= int(globals()['ee{}'.format(i)]):
        g[i] = str(g[i]).replace("\n","\tcluster\n")

for i in range(c+1,l-1):
    if "cluster\n" not in g[i] and "cluster\n" in g[i+1]:
        g[i] = str(g[i]).replace("\n","\tcluster{0}\n".format(z))
        z = z+1

for i in range(0,l):
    f2.write(g[i])
