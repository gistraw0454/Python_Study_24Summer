# ? 메소드
- 특정한 객체 유형에 적용할 수 있는 기능

## 문자열의 다양한 메소드 ??
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

# ? 내장함수 built-in function
- 기본으로 구현되어있어 제공하는 함수

## 다양한 내장함수 ?
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
