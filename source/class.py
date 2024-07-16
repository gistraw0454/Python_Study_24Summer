#%% class
class A: 
    data =10

    def printData(self):
        print(self)
        print(self.data)    # 내가 전달받은 주소의 데이터에 접근

    def intro():
        print("난 A 클래스다")

obj1 = A()
obj2 = A()

obj1.data=20
obj1.printData()    # obj1의 주소값에가서 printData를 출력한다.
obj2.printData()
print(obj1)
print(obj2)
A.intro()

#%% class 2
class Car:
    # 여러 메소드에서 공유할 변수 선언
    brand=""
    color=""
    price=0

    #생성자
    def __init__(self,brand="",color="",price=0):
        #객체로 접근할 애들은 보통 여기에 선언함.
        self.brand = brand
        self.color = color
        self.price = price

    def enginStart(self):
        print(self.brand + "시동킴")
    
    def enginStop(self):
        print(self.brand+"시동끔")


momCar = Car("Benz","Yellow",35000)
dadyCar = Car()
myCar = Car()

# momCar.brand = "Benz"
# momCar.color = "Yellow"
# momCar.price = 35000

momCar.enginStart()