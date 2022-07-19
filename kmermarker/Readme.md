genome상에서 특징적인 k-mer marker 찾기
============
## 1. Jellyfish
### Jellyfish result
<br/>

![jellyinputnew](https://user-images.githubusercontent.com/104611489/179664442-77db4ff0-95ec-46a7-ba83-002ecec9d734.PNG)
![jellyoutput](https://user-images.githubusercontent.com/104611489/179664491-8d1b5069-6ceb-4361-97b0-a10971d62aca.jpg)

<br/>

  - Jellyfish github (https://github.com/gmarcais/Jellyfish)
  - Jellyfish는 주어진 genome sequence에 존재하는 모든 k-mer를 빠르게 세는 프로그램.
  - .fna와 같은 fasta file을 input으로 받고 가능한 k-mer를 모두 count함.
  - output은 k-mer sequence와 등장 횟수가 한줄씩 쓰여있는 txt 파일.
  - Python3을 지원하지 않는 프로그램이므로, conda를 이용하거나 Python2.7 설치 (마지막 버전 2019.7.13)
<br/>

### k-mer counting
