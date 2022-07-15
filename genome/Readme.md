## genome assembly


#### NCBI taxonomy ftp(https://ftp.ncbi.nih.gov/pub/taxonomy/). 2022/05/16 다운로드
#### 고시형 균주 19종이 속하는 9속의 bacteria들의 genome을 모두 수집.
#### _Streptococcus_는 genome 수가 16,000개로 너무 많은 비율을 차지하여 다른 기준으로 수집

<br/>

|속|유전체수|종|유전체수|
|:-|--:|:--|--:|
| <r4> _Lactobacillus_|1203|L.acidophilus|59|
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

- 총 9속, 11489개 유전체 데이터 수집
- _Streptococcus_는 16,000개 이상의 genome data 중 representative genome과 S.thermophilus genome만을 수집
- 수집한 genome 중 Enterococcus가 5863개로 50% 이상을 차지했음
- E.facalis와 E.faecium이 19종 중 가장 높은 비율을 차지했음
  
<br/><br/>  
  
## 다운로드에 사용한 코드들

#### 1. 9속에 속하는 모든 종, 아종들의 taxid 가져오기 
#### 2. taxid를 이용해 종, 아종들의 genome들의 URL 가져오기
#### 3. 9속에 속하는 11,326개 species, subspecies genome 다운로드 코드
#### 4. 163개 subspecies의 subspecies genome 다운로드 코드
#### 5. genome data 넘버링 코드

<br/>

#### assembly_summary.txt나 nodes.dmp 파일은 ncbi taxonomy 사이트에서 tar.gz형식으로 다운 가능

이탤릭체, 수집기준, 링크
