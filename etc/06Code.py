#%% 대화창 실습 : person 딕셔너리의 생성과 조회
person = {'이름': '홍길동','나이':26,'몸무게':82}

person['이름']
person['나이']
person['몸무게']

#%% 대화창 실습 : student 딕셔너리의 생성과 조회
students = {2019001:'이순신', 2029002:"김유신",2020003:'강감찬'}

students[2019001]

#%% 대화창 실습 : 리스트와 튜플로부터 집합 만들기
days_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
days_set = set(days_list)
days_set

fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple)
fruits_set

h_str='hello'
h_set=set(h_str)
h_set
#%% code 6-7 ) 곱집합 함수 product_set() 와 a,b 집합의 곱집합
def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}   # 이중 for루프를 이용한 곱집합
    return res

A={1,3}
B={2,4}

AXB = product_set(A,B)
print(AXB)

#%% code 6-8 ) 곱집합 함수를 이용한 집합의 세제곱 연산
def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}   # 이중 for루프를 이용한 곱집합
    return res

def exp(input_set,exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res,input_set)
    return res

A={1,3}
A3=exp(A,3)
print(A3)

#%% code 6-9 ) 주사위 두번 던져 얻는 경우 모두 구하기
def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}   # 이중 for루프를 이용한 곱집합
    return res

cases ={1,2,3,4,5,6}
print(product_set(cases,cases))

#%% lab 6-12 ) 복수로 주사위를 던졌을 때 특정값 이상을 얻을 확률
def tuple_sum(tup):
    if isinstance(tup,int):
        return tup
    else:
        accum=0
        for element in tup :
            accum += tuple_sum(element)
    return accum

def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}
    return res

def exp(input_set,exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res,input_set)
    return res


def prob_over(x):
    cases = {1, 2, 3, 4, 5, 6}
    all_cases = exp(cases, 3)
    total_cases = len(all_cases)
    favorable_cases = sum(1 for case in all_cases if tuple_sum(case) >= x)
    return 100*(favorable_cases / total_cases)


cases ={1,2,3,4,5,6}
case2times = (product_set(cases,cases))
case3times = product_set(cases,case2times)
print("주사위 세번 던져 발생할 수 있는 사건은",len(case3times),"가지 경우가 존재합니다")
print("주사위 세번 던져 나온 눈의 합이 10이상인 경우는", sum(1 for case in case3times if tuple_sum(case) >= 10),"가지입니다")
#주사위세번던져 나온 눈의 합이 특정한값 x이상이 나올 확률을 계산하는 prob_over(x) 함수를 만들어 확률계산해보자
for x in range(3, 19, 1):
    print("주사위 세번 던져 나온 눈의 합이 {} 이상일 확률은: {:.2f}".format(x,prob_over(x)), "%")