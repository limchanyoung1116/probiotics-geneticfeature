유산균만이 갖는 특징적인 유전자 영역 찾기(가제)-
============================
목차
----------------------------
### 1. 연구의 목적과 배경
### 2. probiotics 균주 유전자 데이터 수집
### 3. probiotics ingroup/outgroup marker kmer 찾기
#### 3-1. tool 선택
#### 3-2. tool : jellyfish
#### 3-3. tool : phenotypeseeker

### 4. probiotics ingroup/outgroup marker 유전자 찾기
#### 4-1. tool 선택
#### 4-2. tool : Neptune
#### 4-3. tool : Scoary/Roary

### 5. Genome에 유전자/서열 mapping
#### 5-1. Neptune 결과 mapping
#### 5-2. Scoary 결과 mapping

### 6. non redundant genome set 만들기
#### 6-1. tool : pyani
#### 6-2. tool : network clustring algorithms

<br/>  
  
## 1. 연구의 목적과 배경
1. 건강에 대한 사회적 관심이 증가하면서 건강기능식품의 소비가 증가
    - 유산균에 대한 수요도 증가하면서 이를 활용한 제품들이 다양하게 출시됨
    - 유산균 제품에 실제로 해당 유산균이 존재하는지 쉽고 빠르게 확인가능한 marker
2. probiotics만이 갖는, 다른 세균들과는 다른 특징적인 유전자 영역 찾기

***
- 식약처 고시형 균주인 9속 19종 probiotics를 target으로 함.
- 19종 균주와 다른 균주를 구분지을수 있는 genetic marker를 찾는것이 목표
<br/>
<br/>

## 2. probiotics 균주 유전자 데이터 수집

#### 수집 범위

1. 식약처 고시형 균주 19종이 속해있는 9속의 bacteria들의 유전체 데이터 수집  
2. 총 9속에 대해서 NCBI taxid를 기준으로 함  
    - 8속의 하위로 포함되어 있는 모든 species, subspecies 유전체 수집     
    - _Streptococcus_ 에 대해서는 고시형 균주에 속하는 _S.thermophilus_ 만 모든 유전체를 수집
    - 다른 _Streptococcus_ species들은 representative genome만 수집

#### 수집 결과 - data (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/genome)

3. 총 11,489개의 genome data를 수집 

<br/> <br/>

## 3. probiotics marker kmer 찾기
### 3-1. tool : jellyfish
<br/>

1. Jellyfish란?
  - Jellyfish github (https://github.com/gmarcais/Jellyfish)
  - 주어진 sequence에 존재하는 모든 k-mer들을 빠르게 counting해주는 프로그램.
  - 원하는 k 길이는 선택 가능하나, k 길이가 길어질수록 작업시간이 길어지고 output 파일이 커짐.
<br/>

2. k-mer compare
  - Jellyfish는 sequence의 k-mer의 counting 기능만 제공함.
    - 다른 sequence의 k-mer를 비교하거나, 여러 파일의 k-mer를 같이 counting하려면 알고리즘을 짜야 함.
  - Jellyfish output을 읽고 연속적으로 k-mer를 count하는 알고리즘.
  - Jellyfish를 이용하지 않는 방법
    - 여러 genome을 input으로 받고, ingroup에서는 존재하지만 outgroup에선 존재하지 않는 sequence를 찾는 알고리즘.
    - 약 50% 정도 완성됨.

<br/><br/>

### 3-2. tool : Phenotypeseeker
<br/>

(여기에 phenotypeseeker 링크 달예정)

1. phenotypeseeker란?
2. 사용한 phenotypeseeker command
3. phenotypeseeker 결과
<br/><br/>

## 4. Probiotics marker 유전자 찾기
<br/>

### 4-1. tool 선택하기
1. 여러 개의 genome 상에서 서열이나 유전자들을 비교하는 많은 tool들이 지난 수십년간 개발되었음.
2. 직접 만들기보다는 기존에 알려진 tool들 중 목적에 맞는 효율적인 tool을 찾고 사용하는 편이 효율적.
3. 첫번째 tool은 기존의 k-mer를 통한 연구와 연계성을 위해, k-mer 기반 알고리즘인 Neptune을 사용.
4. 두번째 tool은 여러 tool들의 특징을 비교한 논문에서, 가장 적합하다고 생각되는 Scoary를 선택.
  - Scoary 선택 이유
    - tool들을 비교한 논문을 읽고 비교 후 선택. (논문 링크 - https://www.cell.com/trends/microbiology/fulltext/S0966-842X(20)30317-6#relatedArticles)
    - 너무 오래된 tool은 호환성 문제가 발생할 수 있으므로 제외.
    - SNP기반 알고리즘은 목표로 하는 큰 locus를 찾기 부적합하므로 제외.
    - k-mer 기반 알고리즘은 이미 Neptune을 선택했기 때문에 제외.
    - TreeWAS, BugWAS, Scoary, Seer, Pyseer 프로그램이 위 조건을 만족.
    - BugWAS는 TreeWAS의 파생 프로그램이고, Pyseer는 Seer의 파이썬 버전 프로그램이므로 통합.
    - 이들 중 파이썬으로 구동되고, 최근까지 많은 논문에서 인용된 Scoary를 먼저 사용하기로 선택(피인용수 350).    
<br/>

### 4-2. Neptune
1. Neptune이란?
  - Neptune github(https://github.com/phac-nml/neptune)
  - Neptune article NCBI(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5737611/)
  - bacteria에서 유전적 차이를 빠르게 찾기 위한 tool.
  - inclusion group과 exclusion group을 설정
  - inclusion group들에서는 존재하지만 exclusion group에서는 존재하지 않는 genomic locus를 찾는다
  - k-mer를 기준으로 일치도를 판단하며 blastn을 이용해 두 서열을 비교한다.
<br/>

2. Neptune 결과
  - 데이터셋, 상세 결과 (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/geneticmarker/Neptune)
  - k-mer의 길이가 길어질수록, 찾는 서열의 수는 줄어들고 길이는 길어짐.
  - k = 19 이하에서보다 k = 22 이상에서 서열의 평균 score가 높음.
  - score > 0.9인 정확도가 높은 서열의 비율은 k길이에 관계없이 비슷함.
  - 같은 속의 genome 100개, k = 23까지는 결과가 출력되었으나 genome 400개, k = 23 부터는 결과가 출력되지 않음.
<br/>

3. IGV mapping
  - IGV(Integraged genome viewer) article (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3346182/)
  - IGV는 genome 상에 mapping된 sequence나 gene을 시각화해 주는 tool임.
  - toyset1 output mapping 결과
    - k=16은 k=19, k=22, k=25, k=28과 다른 위치에 mapping되는 경우가 잦았음.
    - k=16을 제외한 네 output은 같은 위치에 mapping되는 경우가 많았고, k 길이가 길수록 더 넓은 구간에 mapping됨.
    - gene 뿐만 아니라 gene upstream region, intergenic region에도 sequence가 mapping되었음.
  - IGV 결과를 바탕으로, toyset1 output의 sequence와 gff 파일의 gene을 연결짓는 알고리즘을 만들었음.
<br/>

### 4-3. Scoary
1. Scoary란?
  - Genome 상에서 Gene의 존재 여부와 Phenotype과의 관계를 찾아내어 상관관계를 나타내주는 프로그램
  - Input file으로 Genome 별로 Gene presence/absence 여부가 1,0 으로 적힌 csv 파일, 표현형 csv파일이 필요
  - Gene presence/absence file은 Roary프로그램으로 만듬.(https://sanger-pathogens.github.io/Roary/)
  - Scoary github(https://github.com/AdmiralenOla/Scoary)
<br/>

2. Roary/Scoary result - data (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/geneticmarker/RoaryScoary)
  - Neptune과 결과를 비교하기 위해 Neptune의 toyset1과 같은 set을 사용
  - Roary 결과 26개 _Streptococcus_ genome set에 총 35,410개의 gene이 존재
    - 22개의 gene은 26개 genome 모두에 존재했고, 약 31,400개의 gene은 genome 하나에서만 존재했음.
  - Scoary 결과 35,410개의 gene중 1,739개의 gene이 _Streptococcus thermophilus_ 와 다른 _Streptococcus_ 사이의 차이와 관련 있다고 나타났음.
    - 1,739개 gene중 502개의 gene은 _S. thermophilus_ set 에서는 모두 존재하고, 다른 _Streptococcus_ set 에서는 전혀 존재하지 않았음.
    - 502개의 gene은 _S. thermophilus_ 와 다른 _Streptococcus_ 의 차이를 만들어내는 중요한 gene이라고 추측할 수 있음.
<br/><br/>

## 6. Probiotics non redundent set 제작
 - non redundent set page (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/nonredundentset)
#### Non redundent set의 필요성
 - 수집한 genome의 수는 약 11,000개이며 Enterococcus에 속하는 genome만 약 6,000개임
 - 같은 종이나 아종 내에서 수집된 genome들이 많고, 따라서 대부분의 서열이 같은 중복되는 genome도 많음
 - 중복되는 genome들을 제외시키면서 총 genome의 수를 줄이고 효율성을 높일 필요성이 있음
<br/>

### 6-1. tool : Pyani
 - pyani는 주어진 genome들 사이의 ANI(Average Nucleotide Identity) score를 비교하여 표로 만들어주는 프로그램
 - 수집한 9속의 genome중, 이미 representative로 압축된 Streptococcus를 제외한 8속에 대해 속별로 pyani 진행
 - pyani의 output을 시각화하는 방법으로 R의 pheatmap package를 선택
 - pheatmap은 2차원 표에서 색깔의 차이로 genome들 사이의 identity 점수를 시각화해주고, 추정되는 계통도를 각 변에 그려줌
 - pyani output data page (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/nonredundentset/Pyani)
 <br/>
 
### 6-2. tool : network clustering algorithm
#### 사용한 알고리즘 (https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/nonredundentset/clustering)
 - pyani output을 서로간의 identity 점수에 따라 몇 개의 group으로 나누기 위해 network clustering algorithm을 이용
 - 많은 알고리즘들 중 Leiden, Louvain, MCL을 선택
 - cut off를 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.999 7가지로 잡고 진행. 
<br/>

#### 결과
 - 세 알고리즘 모두 비슷한 수와 형태의 grouping을 보여줌
 - MCL은 identity 점수 cut off가 높을 때(0.98이상), 종종 결과를 내지 못함
 - MCL은 길찾기 기반 알고리즘이기 때문에, 전체 유전체 수에 비해 너무 흩어진 경우 제대로 된 결과를 내지 못하는 것으로 보임
 - 예상과는 달리, cut off 0.995 에서도 grouping을 통해 genome수를 절반 이하로 줄일 수 있음
 - 0.99, 0.995, 0.999중 하나를 cut off로 정하기로 함.
