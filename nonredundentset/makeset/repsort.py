import os

class sort:
    def read(self, file, genus):
        f = open(file, "r")
        g = f.readlines()
        l = len(g)
        name = list()
        for i in range(1,l):
            A = str(g[i]).replace('"','').split(',')
            name.append(A[1])
        sort().move(name, genus)

    def move(self, rep, genus):
        ln = len(rep)
        for i in range(0, ln):
            os.system("cp /espeon/analysis1/cylim/seqfiles/fna/{0}.fna /espeon/analysis1/cylim/seqfiles/grouped/{1}/{0}.fna".format(rep, genus))

sort().read("Lactococcus.csv","Lactococcus")
