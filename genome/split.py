f = open("spiciesURL.txt","r")
g = open("StreptococcusURL.txt","w")
h = open("8genusURL.txt","w")

ff = f.readlines()
nff = len(ff)

for i in range(0,nff):
    if "-"*10 in ff[i]:
        p = i

for i in range(0,p):
    g.write(ff[i])
for i in range(p+1,nff):
    h.write(ff[i])

# spiciesURL에 있는 전체 URL에서, Streptococcus들의 URL은 StreptococcusURL에,
# 다른 genus의 URL은 8genusURL에 쓰기

f.close()
g.close()
h.close()
