import Bio
from Bio import SeqIO
import numpy as np
from Bio.Seq import Seq


class hashmer():
    # init에서 전체 seq를 만들고, makemer에서 입력한 k-mer로 canonical/noncanonical 선택해서 만들고,
    # counthash에서 k-mer를 hash형태로 만들고
    # unique에선 unique한 k-mer를, common에선 공통된 k-mer를 찾고 clean으로 끝내기

    def __init__(self, file1, form1 ,file2, form2, length):
        global listmer1, listmer2, leng
        listmer1 = list()
        listmer2 = list()
        leng = length

        for record1 in SeqIO.parse(file1, 'fasta'):
            seq1 = str(repr(record1.seq))
            length1 = len(seq1)
        for i in range(0, length1-length+1):
            listmer1.append(seq1[i:i+length])
        if form1 == '1':
            seq11 = Seq(seq1).reverse_complement()
            for i in range(0, length1-length+1):
                listmer1.append(str(seq11)[i:i+length])

        for record2 in SeqIO.parse(file2, 'fasta'):
            seq2 = str(repr(record2.seq))
            length2 = len(seq2)
        for i in range(0, length2-length+1):
            listmer2.append(seq2[i:i+length])
        if form2 == '1':
            seq22 = Seq(seq2).reverse_complement()
            for i in range(0, length2-length+1):
                listmer2.append(str(seq22)[i:i+length])


    def counthash(self,size):
        global hash_table, hash_origin
        hash_table = np.array([0 for i in range (4**size)])
        hash_origin = np.array([0 for i in range(4**size)])
        L1 = len(listmer1)
        L2 = len(listmer2)
        hash_num = 0
        hash_org = 0

        for i in range(0,L1):
            hash_num = 0
            hash_org = 0

            for j in range(0,size):
                if listmer1[i][j] == 'A':
                    hash_num += 0
                elif listmer1[i][j] == 'T':
                    hash_num += 1*(4**j)
                elif listmer1[i][j] == 'G':
                    hash_num += 2*(4**j)
                elif listmer1[i][j] == 'C':
                    hash_num += 3*(4**j)
                else :
                    hash_num = -1
                    break

            for k in range(0,leng):
                if listmer1[i][k] == 'A':
                    hash_org += 0
                elif listmer1[i][k] == 'T':
                    hash_org += 1*(4**k)
                elif listmer1[i][k] == 'G':
                    hash_org += 2*(4**k)
                elif listmer1[i][k] == 'C':
                    hash_org += 3*(4**k)
                else :
                    hash_org = -1
                    break

            if hash_num != -1 and hash_org != -1:

                if hash_table[hash_num] == 1:
                    for l in range(1,100000):
                        if hash_origin[hash_num] != hash_org:
                            hash_num += l**2
                        elif hash_origin[hash_num] == hash_org:
                            break

                elif hash_table[hash_num] == 0:
                    hash_table[hash_num] += 1
                    hash_origin[hash_num] = hash_org


        hash_num = 0
        hash_org = 0

        def hash(hash_num):
            for x in range (1, 100000):
                if hash_table[hash_num] == 0:
                    break
                elif hash_table[hash_num] == 1:
                    if hash_origin[hash_num] == hash_org:
                        hash_table[hash_num] = 2
                        break
                    elif hash_origin[hash_num] != hash_org:
                        hash_num = hash_num + x**2
                elif hash_table[hash_num] == 2:
                    if hash_origin[hash_num] == hash_org:
                        break
                    elif hash_origin[hash_num] != hash_org:
                        hash_num = hash_num + x**2


        for i in range(0, L2):
            hash_num = 0
            hash_org = 0

            for j in range(0, size):
                if listmer2[i][j] == 'A':
                    hash_num += 0
                elif listmer2[i][j] == 'T':
                    hash_num += 1 * (4 ** j)
                elif listmer2[i][j] == 'G':
                    hash_num += 2 * (4 ** j)
                elif listmer2[i][j] == 'C':
                    hash_num += 3 * (4 ** j)
                else:
                    hash_num = -1
                    break

            for k in range(0, leng):
                if listmer2[i][k] == 'A':
                    hash_org += 0
                elif listmer2[i][k] == 'T':
                    hash_org += 1 * (4 ** k)
                elif listmer2[i][k] == 'G':
                    hash_org += 2 * (4 ** k)
                elif listmer2[i][k] == 'C':
                    hash_org += 3 * (4 ** k)
                else:
                    hash_org = -1
                    break

            if hash_num != -1 and hash_org != -1:
                hash(hash_num)

    def output(self,UC, title):
        F = open("{}.txt".title, "w")
        if UC == 'U':
            F.write("Unique k-mer")
        elif UC == 'C':
            F.write("Common k-mer")
        L = len(hash_table)
        for i in range(0,L):
            if UC == 'U':
                if hash_table[i] == 1:
                    b = ''
                    c = hash_origin[i]
                    for j in range(1,leng):
                        a = c % 4**j
                        c = c - a
                        if a == 0:
                            b = 'A'+ b
                        elif a == 1:
                            b = 'T'+ b
                        elif a == 2:
                            b = 'G'+ b
                        elif a == 3:
                            b = 'C'+ b
                    F.write(b+'\n')

            elif UC == 'C':
                if hash_table[i] == 2:
                    b = ''
                    c = hash_origin[i]
                    for j in range(1,leng):
                        a = c % 4**j
                        c = c - a
                        if a == 0:
                            b = 'A'+ b
                        elif a == 1:
                            b = 'T'+ b
                        elif a == 2:
                            b = 'G'+ b
                        elif a == 3:
                            b = 'C'+ b
                    F.write(b+'\n')

    def clean(self):
        global listmer1, listmer2
        listmer1 = None
        listmer2 = None


A = hashmer('./seq/N00000_ST_s0001302_u0001302_fna.fna', './seq/N00001_ST_s0001304_u0001304_fna.fna')



# file1, file2에 각각 순서대로 genome 넣기
# 더하기 빼기 응용?
'''공통된 k-mer 찾는 알고리즘에서는, 1번seq에서 첫 등장시에만 +1 해주고 2번 seq에서 첫 등장시에만 또 +2 해주기
    그리고 값이 3인 seq들만, 1번 seq list를 처음부터 끝까지 읽으면서 출력해주기'''
'''unique 찾는 알고리즘에서는, +1 -1 해주고 1인 애들만 찾기'''
'''
주어진 genome들을 jellyfish의 output과 같은 형태로 만들기
=> 중복되는 k-mer들도 1회만 나타나게 됨
=> 이를 읽으면 중복걱정 없이 count 가능
=> 구현방법 - 등장시마다 +1 해주고 값 찾기
'''

