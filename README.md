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

## 2. [probiotics 균주 유전자 데이터 수집](https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/genome)

#### 수집 범위

1. 식약처 고시형 균주 19종이 속해있는 9속의 bacteria들의 유전체 데이터 수집  
2. 총 9속에 대해서 NCBI taxid를 기준으로 함  
    - 8속의 하위로 포함되어 있는 모든 species, subspecies 유전체 수집     
    - _Streptococcus_ 에 대해서는 고시형 균주에 속하는 _S.thermophilus_ 만 모든 유전체를 수집
    - 다른 _Streptococcus_ species들은 representative genome만 수집

#### 수집 결과

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
<br/>

### 4-1. tool 선택하기
1. 여러 개의 genome 상에서 서열이나 유전자들을 비교하는 많은 tool들이 지난 수십년간 개발되었음.
2. 직접 만들기보다는 기존에 알려진 tool들 중 목적에 맞는 효율적인 tool을 찾고 사용하는 편이 효율적.
3. 첫번째 tool은 기존의 k-mer를 통한 연구와 연계성을 위해, k-mer 기반 알고리즘인 Neptune을 사용.
4. 두번째 tool은 여러 tool들의 특징을 비교한 논문에서, 가장 적합하다고 생각되는 Scoary를 선택.
 - Scoary 선택 이유
<br/>

### 4-2. [Neptune](https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/Neptune)
<br/>

### 4-3. Scoary
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


## 5. Genome상에 유전자/서열 mapping하기
<br/>

### 5-1. Neptune 결과 mapping하기
<br/>

### 5-2. Scoary 결과 mapping하기
<br/>

## 6. non redundent set 만들기
##### Non redundent set의 필요성
 - 수집한 genome의 수는 약 11,000개이며 Enterococcus에 속하는 genome만 약 6,000개임
 - 같은 종이나 아종 내에서 수집된 genome들이 많고, 따라서 대부분의 서열이 같은 중복되는 genome도 많음
 - 중복되는 genome들을 제외시키면서 총 genome의 수를 줄이고 효율성을 높일 필요성이 있음
<br/>

### 6-1. tool : Pyani
<br/> 
 - pyani는 주어진 genome들 사이의 ANI(Average Nucleotide Identity) score를 비교하여 표로 만들어주는 프로그램
 - 수집한 9속의 genome중, 이미 representative로 압축된 Streptococcus를 제외한 8속에 대해 속별로 pyani 진행
 - pyani의 output을 시각화하는 방법으로 R의 pheatmap package를 선택
 
