유산균만이 갖는 특징적인 유전자 영역 찾기
============================
목차
----------------------------
### 1. 연구의 목적과 배경
### 2. probiotics 균주 유전자 데이터 수집
### 3. probiotics marker k-mer 찾기

#### 3-1. tool : jellyfish
#### 3-2. tool : phenotypeseeker
### 4. probiotics marker 유전자 찾기

#### 4-1. tool : Neptune
#### 4-2. tool : Scoary
### 5. 유전자 영역 확인
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

<br/>
- NCBI taxonomy ftp(https://ftp.ncbi.nih.gov/pub/taxonomy/). 2022/05/16 다운로드

<br/>

|속|유전체수|종|유전체수|
|:-|--:|:--|--:|
| <r4> Lactobacillus|1203|L.acidophilus|59|
|||L.gasseri|61|
|||L.delbrueckii ssp. bulgaricus|40|
|||L.helveticus|155|
|Lacticaseibacillus|526|L.casei|29|
|||L.paracasei|209|
|||L.rhammnosus|208|
|Limosilactobacillus|510|L.fermentum|101|
|||L.reuteri|316|
|Lactiplantibacillus|767|L.plantarum|663|
|Ligilactobacillus|373|L.salivarius|191|
|Lactococcus|412|L.lactis|201|
|Streptococcus|284(17259)|S.thermophilus|179|
|Bifidobacterium|1554|B.bifidum|116|
|||B.breve|158|
|||B.longum|524|
|||B.animalis ssp. lactis|199|
|Enterococcus|5863|E.faecium|2722|
|||E.faecalis|2084|

<br/>

1. 식약처 고시형 균주 19종이 속해있는 9속의 bacteria들의 유전체 데이터 수집  
2. Streptococcus를 제외한 8속에 대해서, NCBI taxid를 기준으로  
  8genus의 하위로 포함되어 있는 모든 species, subspecies 유전체 수집     
    - Streptococcus에 대해서는 고시형 균주에 속하는 S.thermophilus만 모든 유전체를 수집하고,
      나머지 종들은 representative genome만 수집
3. 총 11,326개의 genome data를 수집
<br/>
<br/>

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
3. phenotypeseeker의 단점
  
<br/><br/>

## 4. probiotics marker 유전자 찾기
### 4-1. Neptune
<br/>
1. Neptune이란?
    - bacteria에서 유전적 차이를 빠르게 찾기 위한 tool.
    - inclusion group과 exclusion group을 설정하고, inclusion group들에서는 존재하지만
      exclusion group에서는 존재하지 않는 
  
2. 사용한 Neptune command
 
