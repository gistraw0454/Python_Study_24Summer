# 람다 💡
- **정의:** `return` 문도 없고 함수의 이름도 없는 아주 간략화된 함수 (1회용)
- **구문:** `lambda 매개변수1, 매개변수2, ... : 표현식`
- **주의할점:**
    - 표현식 안에서 새로운 변수를 선언할 수 없다.
    - 반환값은 변수 없이 식 한줄로 표현할 수 있어야 하므로 복잡한 함수는 `def`를 사용하자.
```py
#람다 함수 사용 방법

#1)
add = lambda x, y: x + y
print("100과 200의 합:", add(100, 200))

#2)
print("100과 200의 합:", (lambda x, y: x + y)(100, 200))
```
- **필터나 맵에서 편리하게 사용할 수 있는 함수다.**

## 필터 함수 (filter function) 🧹
- **구문:** `filter(적용시킬 함수, 반복가능 객체 (리스트, 딕셔너리, ...))`
- **기능:** 반복 가능한 요소들을 함수에 넣어 그 리턴값이 참인 것만 묶어 반환
```py
ages = [34, 39, 20, 18, 13, 54]
print("성년 리스트")
for a in filter(lambda x: x >= 19, ages):
    print(a, end=" ")
```
```py
#1)
n_list = [-30, 45, -5, 90, -20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))

#2)
minus_list = []
for a in filter(lambda x: x < 0, n_list):
    minus_list.append(a)
print("음수 리스트", minus_list)
```

## 맵 함수 (map function) 🗺️
- **구문:** `map(적용시킬 함수, 반복가능 객체, ...)`
- **기능:** 반복 가능한 자료형의 각 요소들에 대해 지정된 매핑 함수를 적용하여 반복 가능한 자료형을 반환
```py
a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
print(a)
#>> [1, 4, 9, 16, 25, 36, 49]
```

## 리듀스 함수 (reduce function) 🔽
- **구문:** `reduce(함수, 반복가능 객체)`
- **기능:** 반복 가능한 객체의 항목들에 대해 주어진 함수로 연산을 수행하여 하나의 값을 얻는 데 사용할 수 있다.
- **필요 모듈:** `from functools import reduce`
```py
from functools import reduce

a = [1, 2, 3, 4]
n = reduce(lambda x, y: x * y, a)
print(n)
```

## 리스트와 축약 표현 (list comprehension) 📝
- **구문:** `[표현식 for 변수 in 반복자/연속열 if 조건식]`
    - `if 조건식`은 생략 가능
- **기능:** 반복 가능한 객체를 이용해 쉽게 리스트를 생성할 수 있는 기능
```py
a = [x**2 for x in range(1, 8)]

st = "Hello World"
s_list = [x.upper() for x in st]
print(s_list)
#>> ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

product_xy = [x * y for x in [1, 2, 3] for y in [2, 4, 6]]
print(product_xy)
#>> [2, 4, 6, 4, 8, 12, 6, 12, 18]

[n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]
#>> [6, 12, 18, 24, 30] 2와 3의 배수 구하기
```

## 반복자 (iterator) 🔄
- **정의:** 반복자 객체는 하나 이상의 항목이 포함된 자료구조에서 데이터를 순차적으로 꺼내어 이용할 수 있는 객체
- **메소드:** `__next__`
    - 여러 항목을 포함한 객체의 다음 항목을 반환하는 기능을 가진 함수
- **반복 가능한 자료형:**
    - 리스트, 딕셔너리, 튜플, 문자열, 집합, 파일, range
- **구문:** `iter()`
    - 반복 가능한 자료형을 반복자 객체로 만든다.
```py
lst = [10, 20, 30]
l_iter = iter(lst)  # 리스트 형 객체를 반복자로 만듦
next(l_iter)
#>> 10
next(l_iter)
#>> 20
next(l_iter)
#>> 30
next(l_iter)
#>> StopIteration:..
```
### 반복자 클래스 정의
- **구성 요소:**
    - `__iter__()`과 `__next__()` 메소드를 그 멤버로 가져야만 한다.
    - `__iter__()`는 반복자 객체 자신을 반환해야 한다.
    - `__next__()`는 루프가 돌 때마다 지정된 값을 반환하는 일을 한다.
```py
class OddCounter:
    '''1부터 증가하는 홀수를 반환하는 클래스'''
    def __init__(self, n=1):  # 초기화 메소드, n을 1로 둔다
        self.n = n

    def __iter__(self):  # 반복자는 __iter__() 함수를 가져야 한다.
        return self

    def __next__(self):  # 반복자는 __next__() 함수를 가져야 한다.
        if self.n < 20:   # 반복자가 수행되는 조건
            t = self.n   # self.n을 임시 변수 t에 저장하고
            self.n += 2  # self.n을 2 증가시킨다.
            return t    # t부터 출력해야 1이 가장 먼저 출력된다
        raise StopIteration     # 조건 만족하지 않으면 StopIteration을 raise 한다.
    
my_counter = OddCounter()
for x in my_counter:
    print(x, end=" ")
```

## 반복 가능한 객체를 위한 내장 함수 🔍
- **`all(반복 가능한 객체)`**
    - 반복 가능한 객체의 모든 요소가 참일 때 True, 하나라도 0이면 False 반환
- **`any(반복 가능한 객체)`**
    - 하나라도 참이면 참, 모두 0이면 False
- **`bool(반복 가능한 객체)`**
    - 원소가 있으면 True, 비어 있으면 False
- **`list(반복 가능한 객체)`**
    - <ins>리스트</ins>로 변환한다.
    ```py
    char_list = list('hello')  #=> ['h', 'e', 'l', 'l', 'o']
    ```
- **`반복 가능한 객체.split()`**
    - 공백을 구분자로 하여 <ins>리스트</ins>를 만들어준다.
- **`'구분자'.join(반복 가능한 객체)`**
    - 구분자로 연결해 <ins>문자열</ins>을 만들어준다.

## 제너레이터와 yield 문 🔄
- **정보 없음**