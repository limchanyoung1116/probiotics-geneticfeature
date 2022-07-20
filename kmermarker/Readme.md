genome상에서 특징적인 k-mer marker 찾기
============
## 1. Jellyfish

### Jellyfish 사용법
<br/>

![jellyinputnew](https://user-images.githubusercontent.com/104611489/179679041-79f7b93a-2ad5-43bf-a81d-ad58556fda95.PNG)
![jellyoutput](https://user-images.githubusercontent.com/104611489/179679072-944995ad-0e18-452d-b56e-2b5296736e10.jpg)
<br/>

  - Jellyfish github (https://github.com/gmarcais/Jellyfish)
  - Jellyfish는 주어진 genome sequence에 존재하는 모든 k-mer를 빠르게 세는 프로그램.
  - .fna와 같은 fasta file을 input으로 받고 가능한 k-mer를 모두 count함.
  - count의 output은 .jf 파일인데, dump를 통해 fasta 형식의 파일로 바꿀 수 있음.
  - Python3을 지원하지 않는 프로그램이므로, conda를 이용하거나 Python2.7 설치 (마지막 버전 2019.7.13)
  - Jellyfish command
    - k-mer count : jellyfish count -m 24 -o (output) -s 100M -t 16 -C (input)
    - dump(jf > fasta) : jellyfish dump A.jf > A.fasta
    - input/output example (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/kmermarker/Jellyfish/example)
  
<br/>

### k-mer counting

  - Jellyfish는 여러 genome에 존재하는 k-mer를 비교해주는 기능이 없음.
  - 따라서 다른 genome의 k-mer를 비교하기 위해서는 알고리즘을 짜야 함.

##### 1) Jellyfish output을 이용한 k-mer 비교
  - 비교 알고리즘 (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/kmermarker/Jellyfish/counting)
  - Jellyfish output 또한 k길이의 서열들로 이루어진 fasta format 파일임.
  - Jellyfish output file에 jellyfish를 다시 진행하고, output으로 나온 .jf파일들을 merge 기능을 이용해 합침.
  - 합친 .jf 파일을 dump 하고 등장횟수에 따라 sorting.
  - 주어진 genome set중 몇 개의 genome이 특정 k-mer를 포함하는지 셀수있음.

##### 2) hashing function을 이용한 k-mer 비교 알고리즘
  - hashing이란?
    - 특정한 규칙에 의해 key의 할당위치가 정해지는 dictionary의 일종.
    - 주어진 문자열이나 숫자에 특정한 규칙에 따른 list/array 상의 위치를 할당.
    - input 문자열이나 숫자는 key, list/array 상의 위치(주소)는 value인 dictionary.
  
  - k-mer counting에서 hashing의 활용
    - k-mer를 셀 때 특정한 k-mer가 반복해서 등장한다면 이를 확인할 수 있어야 함.
    - n개의 k-mer중에서 특정 k-mer를 찾으려면, 평균적으로 n/2번 찾아야 함.
    - k-mer를 알파벳 순서로 sorting 하는 경우, 새로운 k-mer를 찾을 때마다 순서를 바꿔주어야 함.
    - 모든 k-mer를 미리 알파벳 순서로 만들어두는 경우, k 길이가 길어질수록 메모리 사용이 기하급수적으로 늘어남.
    - hashing을 이용할 경우 메모리 사용을 줄이면서도 모든 k-mer를 만들어두는 것과 비슷한 효과를 볼 수 있음.
  
  - hashing이 갖는 이점
    - n 길이의 sequence에 존재하는 k-mer의 수는 n-k+1 개임.
    - n 길이의 sequence에서 존재 가능한 모든 k-mer의 경우의 수는 n과 관계없이 4의 k제곱 개임.
    - k 크기가 커질수록 등장하지 않는 k-mer의 수가 크게 늘어남.
    - 모든 k-mer를 미리 기록해두는 경우, k 크기가 커질수록 버려지는 메모리의 양이 늘어남.
    - hashing table을 만드는 경우, n의 크기에 따라 table의 크기를 줄일 수 있음.
    - table의 크기를 4의 k제곱보다 작게 줄이는 경우 중복 문제가 나타날 수 있음.
      - 중복 문제는 open hashing, closed hashing을 이용해 해결 가능함.
  
  - k-mer counting algorithm
    - (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/kmermarker/Jellyfish/hashing)
    - hash table의 칸이 많아질수록 충돌 확률이 낮아지므로 계산 속도가 빨라짐.
    - 따라서 hash table 한 칸의 크기는 최대한 줄여야 함.
    - k-mer sequence는 A,T,G,C의 네 염기만으로 이루어져 있고, 네 염기에 00,01,10,11을 할당 가능함.
      - 예를 들어, ATTCC는 0001011111의 이진수로 변환할 수 있음.
      - 문자 하나의 크기는 1byte지만 이진수는 8자리가 1byte이므로 메모리에서 4배 효율적.
    - n의 크기에 따라 k-mer의 앞에서부터 x개의 염기를 이진수로 변환.
      - x개의 염기는 같지만 서로 다른 서열의 경우 table에서 충돌이 일어남.
      - open hashing의 제곱 조사법을 통해 다른 칸으로 옮기고, 얼마나 옮겼는지 기록.
    - 알고리즘 링크(미완성)
<br/>

## 2. Phenotypeseeker

### Phenotypeseeker 사용법

  - Phenotypeseeker github (https://github.com/bioinfo-ut/PhenotypeSeeker)
  - Phenotypeseeker는 genome상의 k-mer와 genome의 표현형 사이의 상관관계를 학습하는 프로그램.
  - modeling 단계만을 이용해 k-mer와 phenotype과의 상관관계를 알아낼 수 있음.
  - prediction 단계에서는, modeling 단계에서 학습된 model을 바탕으로 다른 genome에 적용할 수 있음.
    - k-mer의 존재 유무를 통해 학습된 phenotype의 유무를 다른 genome에서도 확인 가능.
  - Phenotypeseeker modeling command
    - Phenotypeseeker modeling data.pheno
    - data.pheno에는 Phenotypeseeker에 사용할 파일들의 정보를 적어준다.      
      - SampleID, 경로와위치, 표현형의유무(1,0)
      - input file들의 형식은 fasta 또는 fastq

  - modeling subcommands
<br/>

    - Options for k-mer lists:      
      - -l , --kmer_length   (k-mer의 길이. 1이상 32이하. default = 13)
      - -c INT, --cutoff INT (k-mer 빈도 cut off. defalut = 1)
    - Options for k-mer filtering by frequency:
      - --min INT            (genome들에서 k-mer의 최소 등장 횟수)
      - --max INT            (genome들에서 k-mer의 최대 등장 횟수)
      - max값과 min값 사이로 등장한 k-mer만 기록됨.
    - Options for k-mer filtering by pvalue:
      - --pvalue             (k-mer의 검정과정에서 P-value cut off. default = 0.05)
      - --n_kmers            (모델링에 사용될 최대 k-mer 수. P-value가 낮은 순서대로 사용. default = 1000)
      - --n_kmers 0          (기준을 만족한 모든 k-mer를 모델링에 사용)
<br/>

### Phenotypeseeker 결과
  - 데이터 셋 (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/kmermarker/Phenotypeseeker)

##### 1) testset1
  - Phenotype1 : _Streptococcus thermophilus_ 5 genome (Probiotics 고시형 균주)
  - Phenotype2 : Other _Streptococcus_ 15 genome (Probiotics 고시형 균주가 아닌 균주)
  - subcommand : -l 24
  - 결과
    - Phenotypeseeker modeling에 실패

##### 2) testset 2
  - Phenotype 1 : _Streptococcus thermophilus_ 15 genome (Probiotics 고시형 균주)
  - Phenotype 0 : Other _Streptococcus_ 44 genome (Probiotics 고시형 균주가 아닌 균주)
  - subcommand : -l 24 
  - 결과
    - 학습된 모델로 재예측한 결과와 실제 결과가 일치.
      - _S. thermophilus_ 와 other _Streptococcus_ 를 제대로 구분.
    - Phenotypeseeker에서 _S. thermophilus_ 와 관련있다고 판단한 sequence를 직접 genome에 대입
      - _S. thermophilus_ genome에서는 해당 sequence가 존재했음.
      - Other _Streptococcus_ genome에서는 해당 sequence가 존재하지 않았음.
    - 관련성이 높다고 예측된 sequence들
      - TTCAACCGCATCACCTGTTGCCAA (log coefficient 0.50)
      - CTAAAGGTGCACAACCTTCAGATA (log coefficient 0.31)
      - GGCTAAGGAATTTTCAAAAATCAC (log coefficient 0.29)
      - AATCAGCAACACGGCTCTTGATTG (log coefficient 0.23)
    - 관련성이 있다고 뽑힌 1000개의 sequence들이 모두 5 genome에서 각각 한번만 등장했음.
      - 대부분의 sequence들의 coefficient가 0.00인 이유?
      - 몇몇 sequence들만 coefficient가 높은 이유?


##### 3) testset 3
  - Phenotype 1 : _Streptococcus thermophilus_ 5 cda genomic fna (Probiotics 고시형 균주)
  - Phenotype 0 : _Bifidobacterium_ 43 cds genomic fna (Probiotics 고시형 균주가 아닌 균주)
  - subcommand : -l 24
  - 특이사항 : 2회 반복
  - cds genomic fna는 genome 중 protein coding region sequence 만을 뽑아낸 파일.
  - 결과
    - 정상적으로 결과가 출력됨
    - _S. thermophhilus_ 5 genome을 표현형 1로 맞게 예측.
    - _Bifidobacterium_ 43 genome을 표현형 0으로 맞게 예측.
    - 학습 결과 만들어진 k-mer coefficient value에서 문제 발견
  - 문제점
    - 두 번의 시행에서, logistic regression modeling을 통해 학습된 k-mer coefficient value가 다름.
    - 두 번의 시행에서, 1000개 cut off 안에 들어간 k-mer들이 달랐음.


##### 4) testset 4
  - Phenotype 1 : _Lactococcus Lactis_ 202 genome (Probiotics 고시형 균주)
  - Phenotype 0 : Other _Lactococcus_ 212 genome (Probiotics 고시형 균주가 아닌 균주)
  - subcommand : -l 24
  - 결과
    - Phenotypeseeker modeling 실패


##### 4) 최종 결과
  - genome 수가 많아질수록, 조건에 맞는 k-mer가 줄어드므로 일정 수 이상의 genome에서는 k-mer를 찾지 못함.
  - 비교군과 대조군의 근연관계가 가까울수록 genome sequence의 유사도가 높아 k-mer를 찾기 힘들어짐.
    - sequence 유사도가 높으면 공유하는 k-mer도 많아지므로 조건을 만족하는 k-mer의 수도 줄어듦.

##### 5) Phenotypeseeker의 단점
  - 표현형과 관련성이 확실하고, unique한 k-mer를 찾기 위해서는 k값이 어느정도 커야 함.
  - k값이 너무 커지면, 대부분의 k-mer가 1번 등장하고 이 경우 제대로 된 modeling이 되지 않음.
    - Phenotypeseeker는 logistic regression model 학습을 사용.
    - 학습 과정에서, 대부분의 k-mer가 1회 등장하면 가중치가 제대로 설정되지 않고 결과도 제대로 출력되지 않음.
    - k값이 클떄, genome 수가 적으면 p-value 검정단계가 제대로 작동하지 않는 것으로 추측.
    - k값이 클때, genome 수가 많으면 조건에 맞는 k-mer를 찾기 힘든 것으로 추측.
  - 결론적으로, Phenotypeseeker는 어떤 k-mer가 더 표현형과 관련있는지 오직 등장횟수만으로 판단함.
