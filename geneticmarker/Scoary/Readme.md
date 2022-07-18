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

## Roary/Scoary genome set

  - Neptune과 결과를 비교하기 위해 Neptune에서 사용한 toyset1과 같은 set을 사용
    - 표현형 1 : Probiotics 고시형 균주인 _Streptococcus thermophilus_ 6개 genome
    - 표현형 2 : _Streptococcus_ 에 속하는 고시형 균주가 아닌 20개 genome
    - _S. thermophilus_ representative genome을 포함
    - 26개의 genome에 대해 Roary에서 gene presence.csv 파일 생성
 <br/>
 
## Roary/Scoary output

#### 1. Roary

|number of genomes|
  - Roary 결과 26개의 genome에는 서로 다른 35,410개의 genome이 존재했음.
  - 22개의 gene은 data set의 26개 genome에 모두 존재했음.
    - 22개의 gene중 17개는 길이가 같았고 나머지 5개도 길이가 비슷했음(오차 30bp 이내).
    - 이들 conserved gene은 _Streptococcus_ 의 생존에 필수적인 gene으로 추정됨.
  - 50%(13개) 이상의 genome에 존재하는 gene의 수는 58개임.
  - 6개 이상의 genome에 존재하는 gene의 수는 1,380개임.
  - 2개 이상의 genome에 존재하는 gene의 수는 3,976개임.
  - 35,410개의 gene중 약 31,400개의 gene이 단 하나의 genome상에만 존재하는 gene임.
<br/>

#### 2. Scoary
  - 총 1,739개의 gene이 _S.thermophilus_ 와 다른 _Streptococcus_ 에서 다른 분포를 보인다고 나타났음.
  - 총 502개의 gene이 _S. thermophilus_ 6개 genome 모두에 존재하고, 다른 _Streptococcus_ 20개 genome에서는 모두 존재하지 않았음.
    - 이는 Roary 결과에서 6개 이상의 genome에 존재했던 gene의 수(1,380개)의 약 36%에 해당하는 수치임.
    - 502개의 gene 중에는 열저항성에 관련된 유전자들의 비율이 높았음.
<br/>

#### 3. 발견된 특이한 gene들
- small multi drug resistance gene (protein ID : WP_011225296.1)
  - 이 gene과 관련된 논문 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7416660/)
    - _S. thermophilus_ 내에서도 유전적 다양성이 큼
    - 많은 유전자(~10%)들이 제 기능을 못하는 pseudogene
    - _S. thermophilus_ 는 pathogenicity를 갖는 다른 _Streptococcus_ 와 진화적으로 가까움
    - _S. thermophilus_ 도 많은 virulence gene을 갖지만 대부분은 pseudogene임
  - 논문에서는 _S. thermophilus_ 의 virulence gene들은 대부분 발현되지 않고, 따라서 안전하다고 하였음.
- hypothetical protein
  - hypothetical protein은 어떤 기능을 하는지, 실제로 발현이 되는지 밝혀지지 않은 protein임.
  - 1,739개의 gene중 10%를 넘는 238개의 gene이 hypothetical protein을 coding하는 gene임.
