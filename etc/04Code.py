#%% code 4-6 ) "문자열"*n 하면 n번 반복되어 출력됨.
def print_hello (n):
    print("hello "*n)

print_hello(3)

#%% code 4-13 ) 튜플로 반환하는 다중반환문
def get_root(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return r1,r2

result1, result2 = get_root(1,2,-8)
print(result1, result2)

#%% lab 4-7 ) 원면적과 둘레 반환 {:1f} 써보자.!
def circle_area_circum(radius):
    area = radius**2*3.14
    circum = radius*2*3.14
    return area,circum

radius = 10
area , circum = circle_area_circum(radius)
print("반지름 {}인 원의 면적은 {:.1f}, 원의 둘레는 {:.1f}".format(radius,area,circum))

#%% code 4-17 ) global 키워드를 사용한 전역변수의 참조 방법
def print_sum():
    global a,b
    a=100
    b=100
    result = a+b
    print("함수내부 a+b는",result)

a=10
b=10
print_sum()
result = a+b
print("함수외부 a+b는",result)

#%% code 4-26 ) 가변인자를 가지는 함수의 정의와 호출
def greet(*names):
    for name in names:
        print("안녕하세요",name,"씨")
greet("홍길동",'이순신','장보고')
greet("james",'thomas')

#%% code 4-27 ) 가변 인자를 가지는 함수에서 len함수 사용
def foo(*args):
    print("인자개수",len(args))
    print("인자들",args)    # 튜플형태로 나타난다.
foo(100,200,300)
foo("가","나")

#%% code 4-29 ) factorial 
def fac(n):
    if n <=1 :
        return 1
    return n*fac(n-1)

print(fac(5))

#%% code 4-30 ) fibonacci
def fibo(n):
    if n<=1:
        return n
    else :
        return fibo(n-1) + fibo(n-2)
    
# 몇개의 피보나치수
n = 10

if n <= 0:
    print("음수는 불가")
else :
    for i in range(n):
        print(fibo(i),end=" ")

#%% 대화창실습 : 1000 단위 쉼표 출력방법
print('{:,}'.format(1234567890))