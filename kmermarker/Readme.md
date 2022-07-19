genome상에서 특징적인 k-mer marker 찾기
============
## 1. Jellyfish

### Jellyfish 사용법
<br/>

![jellyinputnew](https://user-images.githubusercontent.com/104611489/179664442-77db4ff0-95ec-46a7-ba83-002ecec9d734.PNG)
![jellyoutput](https://user-images.githubusercontent.com/104611489/179664491-8d1b5069-6ceb-4361-97b0-a10971d62aca.jpg)
<br/>

  - Jellyfish github (https://github.com/gmarcais/Jellyfish)
  - Jellyfish는 주어진 genome sequence에 존재하는 모든 k-mer를 빠르게 세는 프로그램.
  - .fna와 같은 fasta file을 input으로 받고 가능한 k-mer를 모두 count함.
  - count의 output은 .jf 파일인데, dump를 통해 fasta 형식의 파일로 바꿀 수 있음.
  - Python3을 지원하지 않는 프로그램이므로, conda를 이용하거나 Python2.7 설치 (마지막 버전 2019.7.13)
  - Jellyfish command
    - k-mer count : jellyfish count -m 24 -o (output) -s 100M -t 16 -C (input)
    - dump(jf > fasta) : jellyfish dump A.jf > A.fasta
  
<br/>

### k-mer counting

  - Jellyfish는 여러 genome에 존재하는 k-mer를 비교해주는 기능이 없음.
  - 따라서 다른 genome의 k-mer를 비교하기 위해서는 알고리즘을 짜야 함.
<br/>

1) Jellyfish output을 이용한 k-mer 비교
  
  - Jellyfish output 또한 k길이의 서열들로 이루어진 fasta format 파일임.
  - Jellyfish output file에 jellyfish를 다시 진행하고, output으로 나온 .jf파일들을 merge 기능을 이용해 합침.
  - 합친 .jf 파일을 dump 하고 등장횟수에 따라 sorting.
  - 주어진 genome set중 몇 개의 genome이 특정 k-mer를 포함하는지 셀수있음.

2) hashing function을 이용한 k-mer 비교 알고리즘

  - hashing이란?
    - 특정한 규칙에 의해 key의 할당위치가 정해지는 dictionary의 일종.
    - 주어진 문자열이나 숫자에 특정한 규칙에 따른 list/array 상의 위치를 할당.
    - input 문자열이나 숫자는 key, list/array 상의 위치(주소)는 value인 dictionary.
  
  - k-mer counting에서 hashing의 활용
    - k-mer를 셀 때 특정한 k-mer가 반복해서 등장한다면 이를 확인할 수 있어야 함.
    - n개의 k-mer중에서 특정 k-mer를 찾으려면, 평균적으로 n/2번 찾아야 함.
    - k-mer를 알파벳 순서로 sorting 하는 경우, 새로운 k-mer를 찾을 때마다 순서를 바꿔주어야 함.
    - 모든 k-mer를 미리 알파벳 순서로 만들어두는 경우, k 길이가 길어질수록 메모리 사용이 기하급수적으로 늘어남.
    - hashing을 이용할 경우 메모리 사용을 줄이면서도 모든 k-mer를 만들어두는 것과 비슷한 효과를 볼 수 있음.
  
  - hashing이 갖는 이점
    - n 길이의 sequence에 존재하는 k-mer의 수는 n-k+1 개임.
    - n 길이의 sequence에서 존재 가능한 모든 k-mer의 경우의 수는 n과 관계없이 4의 k제곱 개임.
    - k 크기가 커질수록 등장하지 않는 k-mer의 수가 크게 늘어남.
    - 모든 k-mer를 미리 기록해두는 경우, k 크기가 커질수록 버려지는 메모리의 양이 늘어남.
    - hashing table을 만드는 경우, n의 크기에 따라 table의 크기를 줄일 수 있음.
    - table의 크기를 4의 k제곱보다 작게 줄이는 경우 중복 문제가 나타날 수 있음.
      - 중복 문제는 open hashing, closed hashing을 이용해 해결 가능함.
  
  - k-mer counting algorithm
    - hash table의 칸이 많아질수록 충돌 확률이 낮아지므로 계산 속도가 빨라짐.
    - 따라서 hash table 한 칸의 크기는 최대한 줄여야 함.
    - k-mer sequence는 A,T,G,C의 네 염기만으로 이루어져 있고, 네 염기에 00,01,10,11을 할당 가능함.
      - 예를 들어, ATTCC는 0001011111의 이진수로 변환할 수 있음.
      - 문자 하나의 크기는 1byte지만 이진수는 8자리가 1byte이므로 메모리에서 4배 효율적.
    - n의 크기에 따라 k-mer의 앞에서부터 x개의 염기를 이진수로 변환.
      - x개의 염기는 같지만 서로 다른 서열의 경우 table에서 충돌이 일어남.
      - open hashing의 제곱 조사법을 통해 다른 칸으로 옮기고, 얼마나 옮겼는지 기록.
    - 알고리즘 링크(미완성)

  