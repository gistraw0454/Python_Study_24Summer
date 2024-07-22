# 🟥 메소드
- 특정한 객체 유형에 적용할 수 있는 기능

## 문자열의 다양한 메소드 ❤️
```py
'abc'.upper()   # 대문자 만들기

'ABC'.lower()   # 소문자 만들기

'hobby'.count('b') # 'b' 문자가 나타나는 횟수세기

'hobby'.find('h')   # 'h' 문자의 index 위치를 반환

','.join('ABCD')    # 'A,B,C,D'

'   hello   '.rstrip()  # ' hello' 오른쪽 공백지우기

'   hello   '.lstrip()  # 'hello    ' 왼쪽 공백지우기

'   hello   '.strip()  # 'hello' 공백지우기

s1 = 'Long live the King'
s1.replace('King','Queen')  #Long Live the Queen 문자열 교환

s1.title()  # Long Live The King 타이틀 문자열로 변환

s1.capitalize() # Long live the king 첫문자만 대문자

s2 = "X:Y:Z"
s2.split(":")   # :를 구분자로하여 s2문자를 ***리스트***로 분리 ['X','Y','Z']

'Hello' + 'World' # 'Hello World'

```

# 🟧 내장함수 built-in function
- 기본으로 구현되어있어 제공하는 함수

## 다양한 내장함수 🧡
```py
abs(-100)   # 절댓값

min(200,100,300,400)    # 최솟값

max(200,100,300,400)    # 최댓값

len(str1)   # 문자열의 길이를 반환

eval("100+200+300") # 600, 문자열을 수치값과 연산자로 변환하여 평가

sorted("EABFD") # ['A','B','C','D','E','F'] 문자열을 ***리스트***로 정렬

sorted(list=[1,2,3,4],reverse=True) # 내림차순정렬

a_str="Hello Python"
id(a_str)   # 4549938992 객체의 식별값을 정수형으로 반환

type(123)   # int 객체의 자료형 반환

```
## 수식을 가진 문자열과 `eval(), chr(), ord()`
```py
eval('10+20')   # 10+20 문장을 파이썬 번역기가 수행

chr(65) # 'A' 정수-> 해당하는 아스키 문자

ord('A')    # 65 문자 -> 해당하는 아스키 정수
```

# 🟨 리스트에 적용되는 내장함수 
- min() : 사전상 앞에있음
- max() : 사전상 뒤에있음
- sum()  
- len() 

# 🟩 리스트의 메소드
## append vs extend 💚
```py
list1=[11,22,33,44]
list1.append([55,66])
#>> [11,22,33,44,[55,66]]

list2=[11,22,33,44]
list2.extend([55,66])
#>> [11,22,33,44,55,66]
```
- insert(인덱스,원소값)
- list1.remove('a')
- list1.pop() : 젤 마지막원소 pop후 그값 리턴
    - list1.pop(1) : 두번째 원소 pop후 그값 리턴
- list1.reverse() : 역순으로 배열

# 🟦 딕셔너리의 메소드

```py
person = {'이름': '홍길동','나이':26,'몸무게':82}

person.keys()
#>> dict_keys(['이름','나이','몸무게'])

person.values()
#>> dict_values(['홍길동',26,82])

person.items()
#>> dict_items([('이름':'홍길동'),('나이',26),('몸무게',82)])

person.get('취미')  
#>>None     취미가 없으니까 None반환. 그냥 person['취미']하면 오류발생

person.popitem()    # 마지막 아이템을 선택하여 반환 후 삭제
('몸무게',82)

person.pop('나이')    # 나이항목을 반환한 후 삭제

person.clear()  # person딕셔너리의 모든 항목 삭제

```

## 딕셔너리 순회 💙
```py
person = {'이름': '홍길동','나이':26,'몸무게':82}

for key in person:
    print("{} : {}\n".format(key,person[key]))

#>>이름 : 홍길동
#>>나이 : 26
#>>몸무게 : 82
```

# 🟪 튜플의 메소드
```py
t=(10,20,30,20,20,10,50)

t.count(10) # 유플에 포함된 10 원소의 개수
#>> 2

t.index(30) # 튜플에 포함된 30 원소의 인덱스
#>> 2

sum(t)  # 튜플요소합
```
## 튜플 내부 값 변경하기
> list()로 튜플을 리스트로 만들고, 이 리스트 값을 변경시킨 후, tuple()로 리스트를 튜플로 만든다.
```py
t_fruits = ('apple','orange','water melon')

f_list = list(t_fruits)

f_list[1]='kiwi'

t_fruit = tuple(f_list)

```

# 🟫 집합의 메소드
```py
s={100,100,200,200,300,400}

s.add(500)  # 집합에 500 원소 추가

s.discard(100)  # 집합에 100 원소 삭제
```

## 집합 연산 🤎
```py
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
s3={1,2,3}

s1|s2   # 합집합
s1.union(s2)
#>> {1,2,3,4,5,6,7,8,9}

s1&s2   # 교집합
s1.intersection(s2)
#>> {4,5,6}

s1-s2   # 차집합
s1.difference(s2)
#>> {1,2,3}

s1^s2   # 대칭차집합
s1.symmetric_difference(s2)
#>> {1,2,3,7,8,9}

s2.issubset(s1) # s2가 s1의 부분집합이냐?

s1.issuperset(s3)   # s1이 s3의 상위 집합인가?

s1.isdisjoint(s2)   # s1과 s2이 서로소냐
```