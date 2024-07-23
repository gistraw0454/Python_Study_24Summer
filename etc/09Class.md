# 객체지향 프로그래밍
- 다양한 객체를 미리 정의해 둔 클래스에 따라 생성하고, 이들이 프로그램 상에서 상호작용하여 목표에 도달하는 문제 해결 방식
- 실제 세상에 가깝게 모델링하는 기법
- 연산 메소드
    - `(200).__add__(100)`    : 200+100 연산
    - `(200).__sub__(100)`    : 200-100 연산
    - `(200).__truediv__(100)` : 200/100 연산 (flaot)

# 클래스
```py
class Cat:  # 클래스 정의
    def meow(self): #메소드, 멤버함수
        print("meow!")

nabi = Cat()    # cat 객체 생성
nabi.meow()     # 인스턴스이름.메소드(인자)
```

## 생성자
- 초기화 메소드 `__init__(self,..)`
- 객체를 만들때 인스턴스 내부의 변수가 기본값을 가지도록 하는 역할을 하는 메소드   
    - 객체 생성시 자동으로 실행
```py
class Cat:
    def __init__(self,name,color):  # 생성자
        self.name = name
        self.color = color

    def meow(self):
        printf("내이름은 {}, 색깔은 {}, 야옹 야옹~~".format(self.name,self.color))

nabi = Cat("나비","검정")
nabi.meow()
```
- 생성한 인스턴스를 클래스 내에서는 부를 방법이 없기 때문에 self라고 부른다.
- self 키워드를 통해 인스턴스의 메소드와 속성에 접근할 수 있다.
    - nabi가 self로 드간다

## 문자열화 메소드
- `__str__()`
- 어떤 객체의 문자열 표현 방식을 정의하는데, 반환값은 문자열이다.
- `__main__`은 현재 파이썬 인터프리터에 의해 수행되는 메인 프로그램을 의미 (현재 수행중인 프로그램 지칭)
    - __main__.Cat 위의 예제경우, 이건 nabi객체를 의미
```py
class Cat:
    def __init__(self,name,color):  # 생성자
        self.name = name
        self.color = color

    def __str__(self):
        return "Cat(name= '+self.name+',color='+self.color+')"

nabi = Cat("나비","검정")
print(nabi)

#>> Cat(name= 나비, color= 검정색)
```

- \_\_str\_\_ 메소드는 Cat객체의 name과 color를 문자열 형식으로 반환하도록 정의하였는데 이때문에 print(nabi) 를 실행하면 nabi객체의 \_\_str()\_\_ 메소드가 실행된다.

> \_\_init\_\_ ,  \_\_str\_\_ 는 파이썬에 정의된 object라는 클래스의 메소드를 재정의하여 사용하는 것

## 캡슐화
```py
class Cat:
    def __init__(self,name,age):
        self.__name=name    # Cat 클래스의 인스턴스변수를 감추는 역할
        self.__age=age

    # Cat의 문자열 표현방식
    def __str__(self):
        return "Cat(name= '+self.name+',color='+self.color+')"

    # self.__age를 외부에서 자유롭게 접근하는 것을 제한하고 음수가 되지 않도록함
    def set_age(self,age):
        if age >0:
            self.__age=age

    def get_age(self):
        return self.__age

nabi = Cat('나비',3)    # nabi 인스턴스 생성
print(nabi)
nabi.set_age(4) # set_age() 메소드를 통해서 age에 접근
nabi.set_age(-5)    # set_age() 메소드를 통해서 age가 음수가 되지 않도록 함
print(nabi)        
```

## 클래스와 특수메소드
![alt text](image-1.png)
![alt text](image-2.png)

## 클래스 변수와 __dict__
- 클래스 변수 : 인스턴스들이 이 변수를 공유함
- 인스턴스변수 : 인스턴스마다 가지는 변수
```py
class Circle:
    PI = 3.1415 #클래스변수
    def __init__(self,name,radius):
        self.__name = name  # 인스턴스 변수
        self.__radius = radius  # 인스턴스 변수
    
    def area(self):
        return Circle.PI * self.__radius**2

c1 = Circle('C1',4)
print(c1.area())
print("c1의 속성들:",c1.__dict__)

#__dic__[key] 형식으로 value를 얻을 수 있음
print("c1의 __name 변수값:",c1.__dict__['_Circle__name'])
```