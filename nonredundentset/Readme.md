Pyani/clustering
====================
## Pyani - [github link](https://github.com/widdowquinn/pyani)

#### 1. Pyani란?

  - genome들 사이의 ANI(Average Nucleotide Identity)를 비교해주는 프로그램
  - ANI란?
    - 두 genome들의 Nucleotide 서열 일치도
    - genome A와 B 사이의 ANI 점수가 0.98이면, 98%의 Nucleotide 서열이 일치함을 뜻
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

#### 3. Pyani command

  - pyani ~ 대신 average_nucleotide_identity.py ~ 를 사용    
    - 최신 버전에서는 pyani command를 사용하나 conda 채널의 버전은 0.2x 버전이므로 pyani command 사용 불가
  - average_nucleotide_identity.py -i ./inputgenus/Ligilactobacillus -o ./outputgenus/Ligilactobacillus -g -m ANIb --workers 54
    - -m 옵션은 ANIb, ANIm, 그리고 다른 알고리즘 중에 선택하는 옵션
    - --workers는 사용할 쓰레드의 수를 지정
    - -g는 pdf, png 등의 형식으로 pyani 결과를 시각화할지 선택 

#### 4. Pyani 결과
  
  - Pyani에서 자체적인 시각화 옵션을 제공하지만, 이미지 옵션만을 제공함
    - 행렬을 바꿔 정렬하거나, 더 고해상도의 이미지를 얻거나, identity에 따른 색깔 옵션을 바꾸려면 표를 이용한 가공이 필요
    - tab으로 열을 나누고 enter로 행을 나눈, .tab format의 표를 R의 Pheatmap을 통해 시각화
  - Pheatmap이란? - [documentation](https://www.rdocumentation.org/packages/pheatmap/versions/1.0.12/topics/pheatmap)
    - heatmap은 주어진 table을 점수에 따라 색깔로 시각화하는 방식임.
    - Pheatmap은 heatmap을 그려주고 유사도에 따라 추정되는 계통도를 그려주는 R의 library임.
  - pheatmap command
    - library("pheatmap")으로 불러오기
    - pheatmap(AVIDEN) 으로 pheatmap 그리기
  - pheatmap에서 sorting한 행렬 순서 불러오는 방법
    
    - SOR <- pheatmap(AVIDEN)
    - ro <- SOR$tree_row$order
    - co <- SOR$tree_col$order
    - NEW <- AVIDEN[,ro]
    - NEWIDEN <- NEW[co,]

## clustering

#### 1. Network clustering 알고리즘들
  - Network clustering은 그래프 이론에서 다루는 분야이다.
  - 그래프에서 각 요소는 node, 요소 사이 관계를 나타내는 선은 edge이다.
  - Network clustering은, 그래프의 node들을 edge의 밀도를 기준으로 여러 그룹으로 나누는 과정이다.
    - 그룹 내에서는 edge의 밀도가 높고, 그룹 외에서는 edge의 밀도가 낮다.
  - [논문 조사](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4938516/)결과, clustering 알고리즘을 특징을 통해 분류할 수 있었다.
  - 지역조사 알고리즘
    - Louvain, SLM(smart local moving)은 좁은 지역에서 점점 넓은 지역으로 조사 범위를 넓히는 식으로 clustering을 진행한다.
  - 길찾기 알고리즘
    - Infomap, MCL(Markov Cluster algorithm)은 특정 node에서 다른 node로 가는 edge를 탐색한다.
    - 2번의 시행 내로 자신에게 돌아올 확률을 통해, 다른 node들과 가장 많이 연결된 중심 node를 찾고 이를 중심으로 clustering 한다.
  - 선택한 알고리즘
    - 지역조사 알고리즘중 가장 대표적인 Louvain, 가장 진보된 Leiden을 선택했고 길찾기 알고리즘중 가장 대표적인 MCL을 선택했다.

#### 2. clustering 결과
<br/>

|trial|score|Cluster algorithm|Cluster parameter|Ligilactobacillus|Lacticaseibacillus|Lactiplantibacillus|Lactococcus|Limosilactobacillus|
|:-|--:|:--|:--|--:|--:|--:|--:|--:|
|whole genomes||||373|505|767|412|510|
|Cluster try 01|0.95|Louvain|default without self edge|18|27|17|26|30|
|Cluster try 02|0.95|Leiden|default without self edge|18|27|17|26|30|
|Cluster try 03|0.95|MCL|default without self edge|18|27|17|NA|NA|
|Cluster try 04|0.96|Louvain|default without self edge|19|30|18|27|34|
|Cluster try 05|0.96|Leiden|default without self edge|19|30|18|27|34|
|Cluster try 06|0.96|MCL|default without self edge|19|30|17|NA|NA|
|Cluster try 07|0.97|Louvain|default without self edge|22|32|18|29|43|
|Cluster try 08|0.97|Leiden|default without self edge|22|32|18|29|43|
|Cluster try 09|0.97|MCL|default without self edge|23|32|19|NA|NA|
|Cluster try 10|0.98|Louvain|default without self edge|47|44|29|35|91|
|Cluster try 11|0.98|Leiden|default without self edge|47|44|29|35|91|
|Cluster try 12|0.98|MCL|default without self edge|NA|44|29|NA|NA|
|Cluster try 13|0.99|Louvain|default without self edge|121|86|47|94|158|
|Cluster try 14|0.99|Leiden|default without self edge|121|86|47|94|158|
|Cluster try 15|0.99|MCL|default without self edge|NA|NA|45|NA|NA|
|Cluster try 16|0.995|Louvain|default without self edge|144|129|130|163|250|
|Cluster try 17|0.995|Leiden|default without self edge|144|129|130|163|250|
|Cluster try 18|0.995|MCL|default without self edge|NA|132|NA|NA|NA|
|Cluster try 19|0.999|Louvain|default without self edge|207|264|383|265|323|
|Cluster try 20|0.999|Leiden|default without self edge|207|264|383|265|323|
|Cluster try 21|0.999|MCL|default without self edge|NA|NA|387|NA|NA|

<br/>
 1) count한 group 수
 - Leiden과 Louvain은 모든 set에서 완전히 같은 결과를 나타냈다.
 - MCL은 다른 둘과 비슷한 결과를 나타냈지만 일부 set에서 1~2씩 차이가 있었다.
 - MCL은 몇몇 set에서 결과를 내지 못했다.
  - MCL은 길찾기 알고리즘을 기반으로 중심 node를 찾으면서 clustering을 하는 알고리즘이다.
  - 이는 수학적으로는 edge를 통한 node 이동을 상태 변화확률로 표시한 행렬로 구현할 수 있다.
  - 따라서 edge수가 node에 비해 너무 적을 경우 알고리즘이 제대로 작동하지 않는 것으로 추정된다.
<br/>
 2) cut off에 따른 group 수
 - 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.999를 기준으로 7번씩 group을 만들었다.
 - cut off가 낮을수록 genome 수를 많이 줄일 수 있지만 신뢰도가 떨어지게 된다.
 - cut off가 높아질수록 group 수도 당연히 많아졌다.
 - 예상과는 다르게, cut off를 0.999로 잡더라도 genome 수의 절반 이하의 group만이 남았다.
 - 따라서 cut off를 0.99이상으로 잡아서 신뢰도에 중점을 두더라도 많은 genome을 줄일 수 있음이 확인되었다.
