# 28강 - 상속예제, 예외처리
### 상속예제
```py
# %% class variable
class A:

    seq=0               #여기 seq랑

    def __init__(self):
        A.seq+=1    
        self.num = A.seq

    def test(self):
        self.seq=10     #여기 seq랑 다르다. (필드에 정의된 seq)
obj1=A()
obj2=A()
obj3=A()
obj4=A()

obj1.test()
print(obj1.num)
print(obj1.seq)
print(obj2.num)
```

## 예외처리
- 예러: 심각한 오류
- 예외: 덜 심각한 오류
    - 오류가 발생했다? => 오류가 메모리에 할당됐다.

```
try:
    오류가 발생할 수 있는 문장
except 오류이름 as 객체:    //alias: 별칭
    오류 발생시 실행할 문장
```

- 모든 예외 클래스의 부모 클래스는 Exception이다.
- 어떤 오류든지 상관없이 except로 처리할때에는 "오류이름"자리에 예외의 최상위 부모인 Exception을 작성한다
```py
#%% 28 Exception test
try:
    int(input("정수입력 :"))
except Exception as e:  #모든 예외처리
    print("정수만 입력하시오")
print("반드시 실행되어야할 문장")


try:
    print(10/0)
except ZeroDivisionError as e:  # 0으로 나눌때나는 예외만 처리하겠다.
    # print(e.__str__)  #error 메세지를 받아와 출력한다.
    print("0으로 나눌수 없다.")
```