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
        ro <- SOR$tree_row$order
        co <- SOR$tree_col$order
        NEW <- AVIDEN[,ro]
        NEWIDEN <- NEW[co,]

## clustering

#### 1. Network clustering 이란?

#### 2. 세 알고리즘의 특징

#### 3. clustering 결과
