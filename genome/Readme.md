## genome assembly


#### NCBI taxonomy ftp(https://ftp.ncbi.nih.gov/pub/taxonomy/). 2022/05/16 다운로드
#### 고시형 균주 19종이 속하는 9속의 bacteria들의 genome을 모두 수집.
#### _Streptococcus_ 는 genome 수가 16,000개로 너무 많은 비율을 차지하여 다른 기준으로 수집

<br/>

|속|유전체수|종|유전체수|
|:-|--:|:--|--:|
| <r4> _Lactobacillus_|1203|_L.acidophilus_|59|
|||_L.gasseri_|61|
|||_L.delbrueckii ssp. bulgaricus_|40|
|||_L.helveticus_|155|
|_Lacticaseibacillus_|526|_L.casei_|29|
|||_L.paracasei_|209|
|||_L.rhammnosus_|208|
|_Limosilactobacillus_|510|_L.fermentum_|101|
|||_L.reuteri_|316|
|_Lactiplantibacillus_|767|_L.plantarum_|663|
|_Ligilactobacillus_|373|_L.salivarius_|191|
|_Lactococcus_|412|_L.lactis_|201|
|_Streptococcus_|284(17259)|_S.thermophilus_|179|
|_Bifidobacterium_|1554|_B.bifidum_|116|
|||_B.breve_|158|
|||_B.longum_|524|
|||_B.animalis ssp. lactis_|199|
|_Enterococcus_|5863|_E.faecium_|2722|
|||_E.faecalis_|2084|

<br/>

- 총 9속, 11489개 유전체 데이터 수집
- _Streptococcus_ 는 16,000개 이상의 genome data 중 representative genome과 _S.thermophilus_ genome만을 수집
- 수집한 genome 중 _Enterococcus_ 가 5863개로 50% 이상을 차지했음
- _E.facalis_ 와 _E.faecium_ 이 19종 중 가장 높은 비율을 차지했음
  
<br/><br/>  
  
## 다운로드에 사용한 코드들

#### 1. 9속에 속하는 모든 종, 아종들의 taxid 가져오기 - [link](https://github.com/limchanyoung1116/probiotics-geneticfeature/tree/main/genome/1.%20taxid)
#### 2. taxid를 이용해 종, 아종들의 genome들의 URL 가져오기
#### 3. 9속에 속하는 11,326개 species, subspecies genome 다운로드 코드
#### 4. 163개 subspecies의 subspecies genome 다운로드 코드
#### 5. genome data 넘버링 코드

<br/>

#### assembly_summary.txt나 nodes.dmp 파일은 ncbi taxonomy 사이트에서 tar.gz형식으로 다운 가능

이탤릭체, 수집기준, 링크
