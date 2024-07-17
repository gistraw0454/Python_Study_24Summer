# Python_Study_24Summer

- 자료구조 들어가기전 복습차원에서 정리함.
- 앞내용은 굳이 할 필요없는데, 뭐가 부족한지 몰라서 훑긴함. >매우 대충 필기함 주의.

## 목차

#### 1강 파이썬 설치 및 시작하기
#### 2강 인터프리터 사용 방법과 기본 구조
#### 3강 변수의 선언과 자료형
#### 4강 출력함수와 변수의 사용
#### 5강 format()과 형변환
#### 6강 암호화와 복호화, 입력함수
#### 7강 연산자1 - 우선순위와 결합성
#### 8강 연산자2 - 조건식과 비트연산
#### 9강 연산자3 - 비트연산의 활용
#### 10강 연산자4 - 삼항 연산자
#### 11강 삼항연산자의 응용과 if문
#### 12강 if문 예제 및 실습, 누적 연산자
#### 13강 for문 기초1
#### 14강 for문 기초2
#### 15강 기타 제어문
#### 16강 while문
#### 17강 컬렉션 - list1
#### 18강 컬렉션 - list2
#### 19강 컬렉션 -list 실습
#### 20강 list와 tuple, dict
#### 21강 dict와 list 미니 프로젝트 - 학생 관리 프로그램
#### 22강 함수와 메소드 이론
#### 23강 함수 기초 예제
#### 24강 함수 심화 예제
#### 25강 클래스 이론
#### 26강 클래스 예제
#### 27강 상속
#### 28강 상속 예제, 예외 처리
#### 29강 사용자 예외 처리, 파일 입출력
#### 30강 응용 예제 : 섹션1~섹션5
#### 31강 응용 예제 : 섹션6~섹션9
#### 32강 응용 예제 : 섹션10~섹션12
#### 33강 응용 예제 : 섹션13~섹션15
#### 34강 응용 예제 : 섹션16~섹션17
#### 35강 응용 예제 : 섹션18~섹션20

## 필기
- Ctrl + alt 방향키 + 복사 하면 복사를 빠르게 가능
- Python의 조건문은 if뿐임
    - switch case문이 없대 !! 충격..
- 삼항연산자 모양
    - `값1 if A>B else 값2
    - C에서는.. A>B ? 값 : 값2
## 명령어
- `ord` : 문자 -> 정수
- `chr` : 정수 -> 문자
- int() 
- "~{}~".format(a)
    - "~{here}~".format(here=a)
```py
#%% "ABC"에서 B를 Z로 변경
# 문자열은 상수니 변할수없음
strList = "ABC"
strList.replace("B","Z")
strList = strList.replace("B","Z")
print(strList)
```
```py
#%% 자연수를 한글로 변경
# 입력 예) 1024
# 출력 예) 일공이사
han = "공일이삼사오육칠팔구"
num = int(input())
result = ""

while num != 0:
    result = han[num%10] + result
    num //=10

print(result)
```

## DICT
```py
dataDict = {}
이렇게 선언해서 
dataDict[0]="A"이런식으로 넣으면
dataDict= {0:'A'} 가되고,
dataDict[0]하면, 'A'가 조회된다. //idex느낌이 아니라 key 로 조회하는거임.
```

> list dict 부분은 한번 더 보자.

- 함수내에서 `global 전역변수` 이렇게 써주고 해당 전역변수명을 사용해주면 함수내에서 global 변수를 사용할 수 있다.

파이썬 : 객체지향 (class)


## set : 집합, 중복된 원소를 담을 수 없다.
- 값의 유무 검사가 목적이다.

## min(값, 최소값) ; 값은 최소값을 지켜야한다.
```py
exam =[99,78,100,91,81,85,54,100,71,50]
score = [min(n+5,100)for n in exam]
print(score)
```

 
## enumerate로 리스트의 인덱스와 값을 함께 가져온다.
```py
rainbow = ['red','orange','yellow','blue','navy','purple']
for idx,value in enumerate(rainbow):
    print("무지개의 {}번째 색은 {}입니다".format(idx+1,value))
```

## 인덱스번호 직접 구해 사용하는 방법
```py
#%% 1 지역번호국번에서 국번을 추출해라
phone= input("전화번호써라: ")
print("국번: "+phone.split("-")[1])    #3칸짜리 배열이된다.

start = phone.index('-') +1
end = phone.index('-',start)    #start부터 시작해서 - 찾기
# end는 보통 포함이안되니 굳이 -1 할필요없다

code = phone[start:end]
print("국번: "+code)

#%% 2
comp_num = input("사업자 등록 번호\n예) 123-45-23452\n")
#첫번째 - 인덱스 번호가 3일때
c1 = comp_num.find("-")==3
#두번째 - 인덱스 번호가 6일때
c2 = comp_num.find("-",4)==6
#총 길이가 12 일때
c3 = len(comp_num) ==12
#각 번호가 전부 숫자인지 검사
c4 = comp_num.replace("-","").isdecimal()
if c1 and c2 and c3 and c4:
    print("올바른 사업자 등록 번호")
else :
    print("잘못된 사업자 등록 번호")
```

## 모듈 : .py파일
## 패키지 : 모듈을 담고있는 폴더
- 계산기 폴더 안에 사칙연산 파이썬 파일 4개가 있다면, 계산기 패키지 않에, 모듈이 4개 있는 것이다.
```py
import 모듈명
from 모듈 import 함수
from 모듈 import 함수1, 험수2
from 모듈 import *
```

## random 모듈
- random.shuffle(pot) : 임의로 pot 리스트를 섞는다.
- random.randint(1,100) : 1부터100까지의 int중 임의로 하나를 리턴

## time 모듈
- time.sleep(2) : 2초동안 기다림
- time.time() : 현재 시각 리턴

## 파일입출력 (txt, csv, json)
```py
#%% 1 파일 복사하기
fileName =""
while True :
    fileName = input("복사할 파일명을 입력해라")
    #file.txt 면, txt 를 뽑아옴.
    extName = fileName[fileName.rfind('.')+1:]
    if extName != "txt":
        print("복사할 수 없는 파일")
    else:
        break

# with 문이끝나면 자동으로 close를 해준다.
# source는 객체명
with open(fileName,'rt',encoding="euc-kr") as source: # utf-8로 해봤는데 안되길래 이걸로함
    with open("복사본-"+fileName,'wt') as copy:
        while True:
            #source라는 파일에서 한글자씩 가져온다
            buffer=source.read(1)
            if not buffer:
                break
            copy.write(buffer)
print("복사본-"+fileName+"파일이 생성됨")
# %% 2 csv 파일로 cctv수 구하기
import csv
with open('cctv.csv','r') as csvfile:
    # csvfile에 넣을건데, `,`로 구분하겠다. 각각의 문자열을 ""로 묶겠다
    buffer = csv.reader(csvfile,delimiter=",",quotechar='"')
    total =0
    for i,line in enumerate(buffer):
        if i!=0:
            total +=int(line[4])
print('CCTV 총 {}대입니다.'.format(total))

#%% 3 json 파일에서 읽어오기
import json
with open('cctv.json','r',encoding='utf-8') as jsonfile:
    buffer = jsonfile.read()
    cctv_list=json.loads(buffer)
    cctv_purpose=set()
    for place in cctv_list:
        cctv_purpose.add(place['설치목적구분'])

print(cctv_purpose)
```