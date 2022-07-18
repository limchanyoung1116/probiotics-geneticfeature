Neptune
========
## 1. Neptune이란?
<br/>

![image](https://user-images.githubusercontent.com/104611489/179478062-5d99e63c-69a8-4e75-a6de-fc0a599fc989.png)
<br/>

  - Neptune github(https://github.com/phac-nml/neptune)
  - Neptune article NCBI(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5737611/)
  - bacteria에서 유전적 차이를 빠르게 찾기 위한 tool.
  - inclusion group과 exclusion group을 설정
  - inclusion group에서는 공유되지만 exclusion group에서는 존재하지 않는 genomic locus를 찾는다.
<br/>

## 2. Neptune 알고리즘

![image](https://user-images.githubusercontent.com/104611489/179479234-e00be085-3106-4671-a51d-dee42e14ccb3.png)
<br/>

  1) Blastn을 이용해 각 genome에서 어떤 k-mer가 몇 번 나타나는지 세고 txt파일로 저장.
  - reverse complement sequence는 한 서열로 통합.
  2) Inclusion group에서는 일정횟수 이상 등장하고, exclusion group에서는 등장 횟수가 적은 k-mer를 찾아 점수를 매긴다.
  3) 조건을 만족하는 k-mer들로 reference sequence를 만드는데, 이 때 k-mer들이 붙어 있다면 하나의 sequence로 합친다.
  4) 만들어진 reference sequence가 일정 길이 이상이라면, matching score와 length, sequence를 기록한다.
<br/>

#### scoring method
  - (inclusion score) = (만들어진 sequence와 inclusion group genome들 사이의 일치 점수)
  - (exclusion score) = (만들어진 sequence와 exclusion group genome들 사이의 일치 점수)
  - score = (inclusion score) - (exclusion score)
  - score를 매길 때 영향을 주는 요소는 일치하는 염기 수, gap, mutation rate, GC content
<br/>

## 3. 사용한 genome set
1) toyset 1
    
  - inclusion : representative를 포함한 6개의 Streptococcus thermophilus genome
  - exclusion : 20개의 thermophilus가 아닌 Streptococcus genome
  - k=10, k=13, k=16, k=19, k=22, k=25, k=28 으로 진행
    - kmer의 k값에 따른 결과의 차이 비교
    - command : Neptune --inclusion/... --exclusion/... --output/... k=x
  
2) toyset 2
    
  - inclusion : Lactococcus lactis 201개 genome 전체
  - exclusion : L.lactis를 제외한 Lactococcus 211개 genome 전체
  - k = 23
  - Neptune으로 어느정도 크기의 ingroup/outgroup까지 작업이 가능한지 확인.

3) toyset 3

  - inclusion : Lactococcus lactis 201개 genome중 20개
  - exclusion : L.lactis를 제외한 Lactococcus 211개 genome중 80개
  - k = 23
  - Neptune으로 어느정도 크기의 ingroup/outgroup까지 작업이 가능한지 확인.
  <br/>
  
## 4. Neptune 결과
  
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
  
2) toyset 2,3
    
  - toyset 2에서는 결과가 출력되지 않음.
  - toyset 3에서는 결과가 출력되었으나, 총 46개의 서열만을 찾아냄.
    - score > 0.8 genome은 7개, score > 0.5 genome은 31개에 불과했음.
  - Neptune의 특성상, genome의 수가 늘어날수록 출력되는 contig가 적어질 수밖에 없음.
    - 따라서 Neptune은 100개 이하의 genome set에서만 사용하기로 결론지음.
<br/>
