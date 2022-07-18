Probiotics Scoary data/result
==============================
## Scoary란?

  - Scoary github(https://github.com/AdmiralenOla/Scoary)
  - Genome 상에서 gene의 존재 여부와 phenotype과의 관계를 찾아내어 상관관계를 나타내주는 프로그램
  - Input file
    - genome별로 gene의 존재 유무가 1,0으로 표시된 2차원 table 형식의 csv file
    - genome별로 나타나는 phynotype들이 1,0으로 표시된 2차원 table 형식의 csv file
  - Gene presence/absence file은 Roary프로그램으로 만듬.(https://sanger-pathogens.github.io/Roary/)
  - Roary
    - 여러 개의 input genome들에서 유전자의 존재 유무를 2차원 table csv 파일로 만들어주는 프로그램
    - input : genome의 gff+fna파일
    - output : genome별로 gene의 존재 유무를 1,0으로 알려주는 csv 파일
<br/>    

## Scoary genome set

  - Neptune과 결과를 비교하기 위해 Neptune에서 사용한 toyset1과 같은 set을 사용
    - 표현형 1 : Probiotics 고시형 균주인 _Streptococcus thermophilus_ 6개 genome
    - 표현형 2 : _Streptococcus_에 속하는 고시형 균주가 아닌 20개 genome
    - _S. thermophilus_ representative genome을 포함
    - 26개의 genome에 대해 Roary에서 gene presence.csv 파일 생성
 
# Scoary output

  - 
