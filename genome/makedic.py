f = open("spiciesURL.txt","r")
g = open("spedictionary.txt","r")
h = open("dictionaryfinal.txt","w")

A = f.readlines()
B = g.readlines()

LA = len(A)
LB = len(B)

h.write(B[0]+str(B[1]).replace("\n","")+"\t"+"Biosample"+"\t"+"Bioproject"+"\n")

for i in range(0,LA):
    a = A[i].split("\t")
    for j in range(2,LB):
        b = B[j].split("\t")
        if a[0] == b[0]:
            h.write(str(B[j]).replace("\n","")+"\t"+a[2]+"\t"+a[1]+"\n")

# 다운로드 과정에서 만들어진 spedictionary.txt에Biosample, Bioproject 정보를
# 추가로 넣어주는 코드

f.close()
g.close()
h.close()
