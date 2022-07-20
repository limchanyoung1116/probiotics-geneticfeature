import Bio
from Bio import SeqIO
import numpy as np

class hashmer():
    # init에서 전체 seq를 만들고, makemer에서 입력한 k-mer로 canonical/noncanonical 선택해서 만들고,
    # counthash에서 k-mer를 hash형태로 만들고
    # unique에선 unique한 k-mer를, common에선 공통된 k-mer를 찾고 clean으로 끝내기

    def __init__(self, file1, form1 ,file2, form2):
        global seq1, length1, seq2, length2, listmer1, listmer2
        listmer1 = list()
        listmer2 = list()
        if 1 == form1:
            for record1 in SeqIO.parse(file1, 'fasta'):
                seq1 = str(repr(record1.seq))
                length1 = len(seq1)
        elif 2 == form1:
            for record1 in SeqIO.parse(file1, 'fasta'):
                seq1 = str(repr(record1.seq))
                listmer1.append(seq1)

        if 1 == form2:
            for record2 in SeqIO.parse(file2, 'fasta'):
                seq2 = str(repr(record2.seq))
                length2 = len(seq2)
        elif 2 == form2:
            for record2 in SeqIO.parse(file2, 'fasta'):
                seq2 = str(repr(record2.seq))
                listmer2.append(seq2)

    def makemer(self,length):#seqIO reverse complement 사용
        if listmer1 == list():
            for i in range(0,length1-length+1):
                listmer1.append(seq1[i:i+length])
            seqa = seq1.replace('A', 'a')
            seqb = seqa.replace('T', 'A')
            seqc = seqb.replace('a', 'T')
            seqd = seqc.replace('G', 'g')
            seqe = seqd.replace('C', 'G')
            seqf = seqe.replace('g', 'C')
            for i in range(0, length1 - length + 1):
                listmer1.append(seqf[i:i + length])

        if listmer2 == list():
            for i in range(0,length2-length+1):
                listmer2.append(seq1[i:i+length])
            seqA = seq2.replace('A', 'a')
            seqB = seqA.replace('T', 'A')
            seqC = seqB.replace('a', 'T')
            seqD = seqC.replace('G', 'g')
            seqE = seqD.replace('C', 'G')
            seqF = seqE.replace('g', 'C')
            for i in range(0, length2 - length + 1):
                listmer2.append(seqF[i:i + length])

            seqa = None
            seqb = None
            seqc = None
            seqd = None
            seqe = None
            seqf = None
            seqA = None
            seqB = None
            seqC = None
            seqD = None
            seqE = None
            seqF = None

    def counthash(self,size,UC):
        hash_table = np.array([0 for i in range (4**size)])
        L1 = len(listmer1)
        L2 = len(listmer2)
        hash_num = 0
        for i in range(0,L1):
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
                    break

                if UC == 'U' and hash_table[hash_num] == 0:
                    hash_table[hash_num] += 1
                elif UC == 'C' and hash_table[hash_num] == 0:
                    hash_table[hash_num] += 1

        for i in range(0,L2):
            for j in range(0,size):
                if listmer1[i][j] == 'A':
                    hash_num += 0
                if listmer1[i][j] == 'T':
                    hash_num += 1*(4**j)
                if listmer1[i][j] == 'G':
                    hash_num += 2*(4**j)
                if listmer1[i][j] == 'C':
                    hash_num += 3*(4**j)

                if UC == 'U' and hash_table[hash_num] == 1:
                    hash_table[hash_num] += 1
                elif UC == 'C' and hash_table[hash_num] == 1:
                    hash_table[hash_num] += 1



    def clean(self):
        global seq1, length1, seq2, length2, listmer1, listmer2
        seq1 = None
        seq2 = None
        length1 = None
        length2 = None
        listmer1 = None
        listmer2 = None


A = hashmer('./seq/N00000_ST_s0001302_u0001302_fna.fna', './seq/N00001_ST_s0001304_u0001304_fna.fna')

print(seq1)
print(length1)

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