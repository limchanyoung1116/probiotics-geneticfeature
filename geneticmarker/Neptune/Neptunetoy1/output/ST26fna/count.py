for i in range(0,5):
    globals()['f{}'.format(i)] = open("k{0}/consolidated/consolidated.fasta".format(28-i*3),"r")
    g = globals()['f{}'.format(i)].read().split(">")
    l = len(g)
    
    seve = 0
    eve = 0
    mini = 100000
    maxi = 0
    
    for j in range(1,l):
        a = g[j].index("score")
        b = g[j].index("in")
        c = g[j].index("len")
        d = g[j].index("ref")
        
        e = g[j][a+6:b-1]
        f = g[j][c+4:d-1]
        sco = float(e)
        leng = float(f)
        seve = seve+sco
        eve = eve+leng
       
        if leng > maxi:
            maxi = leng
        if leng < mini:
            mini = leng

    print("everage score: {0}\n".format(seve/(l-1)))
    print("everage length: {0}\n".format(eve/(l-1)))
    print("maximum length: {0}\n".format(maxi))
    print("minimum length: {0}\n".format(mini))

