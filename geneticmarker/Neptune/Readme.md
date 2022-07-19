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
  - inclusion group에서는 공유되지만 exclusion group에서는 존재하지 않는 genomic locus를 찾음.
<br/>

## 2. Neptune 알고리즘

![image](https://user-images.githubusercontent.com/104611489/179479234-e00be085-3106-4671-a51d-dee42e14ccb3.png)
<br/>

  1) Blastn을 이용해 각 genome에서 어떤 k-mer가 몇 번 나타나는지 세고 txt파일로 저장.
  - reverse complement sequence는 한 서열로 통합.
  2) Inclusion group에서는 일정횟수 이상 등장하고, exclusion group에서는 등장 횟수가 적은 k-mer를 찾아 점수를 매김.
  3) 조건을 만족하는 k-mer들로 reference sequence를 만드는데, 이 때 k-mer들이 붙어 있다면 하나의 sequence로 합침.
  4) 만들어진 reference sequence가 일정 길이 이상이라면, matching score와 length, sequence를 기록함.
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
  - k = 22 이상과 19 이하에서 정확도 차이가 남.
  - 최소, 최대 contig 길이는 k와 상관관계가 있지만, k = 22 이상에서는 최대길이 변화 없음.
  
2) toyset 2,3
    
  - toyset 2에서는 결과가 출력되지 않음.
  - toyset 3에서는 결과가 출력되었으나, 총 46개의 서열만을 찾아냄.
    - score > 0.8 genome은 7개, score > 0.5 genome은 31개에 불과했음.
  - Neptune의 특성상, genome의 수가 늘어날수록 출력되는 contig가 적어질 수밖에 없음.
    - 따라서 Neptune은 100개 이하의 genome set에서만 사용하기로 결론지음.
<br/>


## 5. IGV mapping

1) IGV란?
<br/>

![IGV](https://user-images.githubusercontent.com/104611489/179492527-7ec036fa-8486-4b55-abc5-65be1fdeda5b.jpg)
<br/>
  
  - IGV github (https://github.com/igvteam/igv)
  - Integrated genome viewer의 줄임말
  - fna파일과 gff, bam 파일을 input으로 받고, fna sequence 상에 gff의 gene이나 bam의 sequence를 위치시켜 시각화해 줌.
  
2) IGV input format으로 변환
  <br/>
  ![Neptunemyset1](https://user-images.githubusercontent.com/104611489/179651690-11becffb-910a-4434-b220-6167c455584d.PNG)

  
  <br/>
  
  - Neptune의 output 파일명은 consolidated.fasta 형식
    - 그림과 같이 contig의 sequence와 score, length, 위치 등의 정보를 담고 있음.
    - 이를 IGV의 input으로 쓸 수 있는 .bam format으로 바꾸어야 함.
  - .sam, .bed, .bam file
    - .sam 파일은 input sequence들을 reference sequence에 mapping 한, sequence 내에서의 위치 정보를 담고 있는 파일
    - .bam 파일은 .sam 파일을 압축한 파일
    - .sam과 .bam 파일은 reference sequence 내에서의 순서에 따라 sorting 할 수 있음.
    - sorting할 경우 IGV mapping을 비롯한 작업들에서 속도가 크게 향상됨.
  - Bowtie2
    - Bowtie2 github (https://github.com/BenLangmead/bowtie2)
    - Bowtie2 manual (http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#building-from-source)
    - sequence.fasta 형식의 파일을 referencesequence.fna 형식 파일에 mapping하여 .sam 형식으로 바꿔줌.
    - 두 sequence를 match, mismatch, gap에 기반한 score를 통해 비교하여, 일정 score가 넘으면 mapping
    - 사용한 커맨드
      - -p 5 -f --very-sensitive-local -x ./index/thermoref -U ./neptuneoutput/k16.fasta -S ./SAM/ST26k16 --un ./SAM/ST26k16non
  - Samtools
    - .fasta file, .sam flie, .bam flie, .bed file등 파일을 다른 여러 format으로 변환해 주는 프로그램.
    - .sam file -> .bam file 변환을 위해 사용함.
    - 사용한 커맨드
      - Sam to bam : Samtools view bSF4 a > b
      - file sorting : samtools sort a > b
      - file indexing : samtools index a
  - IGV
    - IGV를 서버에서 사용하기 위해서는 Xming과 같은, server GNU program이 필요함.
    - Windows 버전을 사용할 수 있음.
    - 먼저 .fna 파일을 불러오고, 해당 genome의 .gff 파일이나 .bam 파일을 불러와 mapping된 위치를 확인할 수 있음.

3) IGV 결과
  
  - Neptune k=16, k=19, k=22, k=25, k=28 결과들을 원래 sequence의 .fna 파일에 mapping한 결과를 확인.
  - k=16은 다른 넷과 다른 위치에서 mapping된 sequence들이 많았음.
  - k=19~k=28은 비슷한 위치에서 많이 mapping되었는데, 이 경우 k크기와 mapping된 locus의 길이가 비례함.
  - gene 내부보다 intergenic region이나 gene upstream~gene 위치에 mapping된 서열이 많았음.
  - k=16~k=28 다섯 output을 비교했을 때, k=19, k=22가 다른 output과 가장 많이 겹쳤음.

4) sequence to gene 알고리즘


Neptune - -(Bedtools, Samtools, Bowtie2) - -> IGV
