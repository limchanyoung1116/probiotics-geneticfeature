Pyani/clustering
====================
## Pyani - [github link](https://github.com/widdowquinn/pyani)

#### 1. Pyani란?
 - genome들 사이의 ANI(Average Nucleotide Identity)를 비교해주는 프로그램
 - ANI란?
  - 두 genome들의 Nucleotide 서열 일치도
  - genome A와 B 사이의 ANI 점수가 0.98이면, 98%의 Nucleotide 서열이 일치함을 뜻함
  - 서열 일치도를 판단할 때에는 blastn, murmur 등 기존의 서열 비교 프로그램이 주로 사용됨
 - ANI의 방향성
  - genome의 서열 전체를 비교하려면 오래 걸리기 때문에 한 서열을 일정 단위로 잘라서 비교
  - ANI A->B와 ANI B->A 점수가 서로 다르게 나올 수 있음

#### 2. Pyani set

 - 9속 중에서 이미 representative genome만을 남긴 Streptococcus를 제외한 8속에 대해 속 단위로 진행
 - genome 수 1000개를 기준으로 blastn과 murmur를 선택
  - blastn은 시간이 비교적 오래걸리는 대신 정확도가 비교적 높음.
  - murmur는 시간이 비교적 적게걸리는 대신 정확도가 비교적 낮음.
  - blastn 선택 genome
   - Ligilactobacillus, Lactococcus, Lacticaseibacillus, Limosilactobacillus, Lactiplantibacillus 5속
  - murmur 선택 genome
   - Lactobacillus, Bifidobacterium, Enterococcus 3속
  

#### 3. Pyani 결과
<br/>

## clustering

#### 1. Network clustering 이란?

#### 2. 세 알고리즘의 특징

#### 3. clustering 결과
