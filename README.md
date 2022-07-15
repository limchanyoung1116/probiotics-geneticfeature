유산균만이 갖는 특징적인 유전자 영역 찾기(가제)-
============================
목차
----------------------------
### 1. 연구의 목적과 배경
### 2. probiotics 균주 유전자 데이터 수집
### 3. probiotics ingroup/outgroup marker kmer 찾기

####  3-1. tool : jellyfish
####  3-2. tool : phenotypeseeker
### 4. probiotics ingroup/outgroup marker 유전자 찾기

#### 4-1. tool : Neptune
#### 4-2. tool : Scoary
### 5. non redundant genome set 만들기

#### 5-1. tool : pyani
#### 5-2. tool : network clustring algorithms

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

## 2. [probiotics 균주 유전자 데이터 수집](https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/genome)

##### 수집 범위

1. 식약처 고시형 균주 19종이 속해있는 9속의 bacteria들의 유전체 데이터 수집  
2. 총 9속에 대해서 NCBI taxid를 기준으로 함  
    - 8속의 하위로 포함되어 있는 모든 species, subspecies 유전체 수집     
    - _Streptococcus_ 에 대해서는 고시형 균주에 속하는 _S.thermophilus_ 만 모든 유전체를 수집
    - 다른 _Streptococcus_ species들은 representative genome만 수집

##### 수집 결과

3. 총 11,489개의 genome data를 수집
<br/> <br/>

## 3. probiotics marker kmer 찾기
### 3-1. tool : jellyfish
<br/>

(여기에 젤리피쉬 링크 달예정)

1. jellyfish란?
    - 주어진 두 genome에서
2. 사용한 jellyfish command
3. jellyfish를 활용한 연속적인 k-mer counting
<br/><br/>

### 3-2. tool : phenotypeseeker
<br/>

(여기에 phenotypeseeker 링크 달예정)

1. phenotypeseeker란?
2. 사용한 phenotypeseeker command
3. phenotypeseeker 결과
  
<br/><br/>

## 4. probiotics marker 유전자 찾기
### 4-1. Neptune
<br/>
1. Neptune이란?
  
    - bacteria에서 유전적 차이를 빠르게 찾기 위한 tool.
    - inclusion group과 exclusion group을 설정
    - inclusion group들에서는 존재하지만 exclusion group에서는 존재하지 않는 genomic locus를 찾는다
    - k-mer를 기준으로 일치도를 판단하며 blastn을 이용해 두 서열을 비교한다.
    - Neptune github(https://github.com/phac-nml/neptune)
    - Neptune article NCBI(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5737611/)
  
2. 사용한 genome set
  1) toyset 1
    
    - inclusion : representative를 포함한 6개의 Streptococcus thermophilus genome
    - exclusion : 20개의 thermophilus가 아닌 Streptococcus genome
    - k=10, k=13, k=16, k=19, k=22, k=25, k=28 으로 진행
      - kmer의 k값에 따른 결과의 차이 비교
    - command : Neptune --inclusion/... --exclusion/... --output/... k=x
  
  2) toyset 2
    
    - inclusion : Lactococcus lactis 201개 genome 전체
    - exclusion : L.lactis를 제외한 Lactococcus 211개 genome 전체
  <br/>
  
3. Neptune 결과
  
  - Neptune score?
    - inclusion group의 genome 중 얼마나 많은 genome이 해당 서열을 포함하는지: inclusion score
    - exclusion group의 genome 중 얼마나 많은 genome이 해당 서열을 포함하는지: exclusion score
    - score = inclusion score - exclusion score
  
  1) toyset 1
  
  |k 길이|서열 수|평균 서열길이|평균 score|score>=0.9|최대길이|최소길이|
  |:----:|------:|-----------:|--------:|---------:|--------:|-------:|
  |10|
  |13|
  |k=16|384|86.52|0.70|96개|258|64|
  |k=19|576|360.64|0.70|144개|3378|76|
  |k=22|276|874.85|0.74|71개|8798|88|
  |k=25|224|1161.47|0.73|56개|8778|100|
  |k=28|203|1333.57|0.74|58개|8835|112|
    
    - k=10, k=13에서는 output fasta 파일이 생성되지 않음. Neptune이 영역을 찾지 못함.
    - contig의 수는 k=19에서 극대값이며 k가 커질수록 감소폭이 완만해짐
    - 평균 서열길이는 k값이 커질수록 커짐. k값이 작을때 k값에 따른 서열길이 변화폭이 큼.
    - k = 22 이상과 19 이하에서 정확도 차이가 남
    - 최소, 최대 contig 길이는 k와 상관관계가 있지만, k = 22 이상에서는 최대길이 변화 없음
  
  2) toyset 2
    
    - k = 23 에서 결과가 출력되지 않음.
    - Neptune의 특성상, genome의 수가 늘어날수록 출력되는 contig가 적어질 수밖에 없음.
      - 따라서 Neptune은 100개 이하의 genome set에서만 사용하기로 결론지음.
<br/>

### 4-2. Scoary
<br/>

1. Scoary란?
    - Genome 상에서 Gene의 존재 여부와 Phenotype과의 관계를 찾아내어 상관관계를 나타내주는 프로그램
    - Input file으로 Genome 별로 Gene presence/absence 여부가 1,0 으로 적힌 csv 파일, 표현형 csv파일이 필요
    - Gene presence/absence file은 Roary프로그램으로 만듬.(https://sanger-pathogens.github.io/Roary/)
    - Scoary github(https://github.com/AdmiralenOla/Scoary)

2. Scoary genome set
    - Neptune과 결과를 비교하기 위해 Neptune의 toyset1과 같은 set을 사용
      - Streptococcus thermophilus 6genome은 probiotics 표현형 1, S. non thermophilus 20genome은 0
      - 26개의 genome에 대해 Roary에서 gene presence.csv 파일 생성
 
3. Scoary 
