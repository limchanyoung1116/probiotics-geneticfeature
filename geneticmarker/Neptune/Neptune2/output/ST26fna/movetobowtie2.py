for i in range(0,5):
    globals()['f{}'.format(i)] = open("k{0}/consolidated/consolidated.fasta".format(28-i*3),"r")
    g = globals()['f{}'.format(i)].read().split(">")
    l = len(g)
    globals()['F{}'.format(i)] = open("/home/cylim/projects/lacto/bowtie22/ST26/s09k{}.fasta".format(28-i*3),"w")

    for j in range(1,l):
        a = g[j].index("score")
        b = g[j].index("in")
        e = g[j][a+6:b-1]
        sco = float(e)
        if sco >= 0.90:
            globals()['F{}'.format(i)].write(">"+g[j])
        a = ''
        b = ''
        c = ''
        sco = 0.00        
