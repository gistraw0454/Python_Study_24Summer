#%% class
class A: 
    data =10

    def printData(self):
        print(self)
        print(self.data)    # ���� ���޹��� �ּ��� �����Ϳ� ����

    def intro():
        print("�� A Ŭ������")

obj1 = A()
obj2 = A()

obj1.data=20
obj1.printData()    # obj1�� �ּҰ������� printData�� ����Ѵ�.
obj2.printData()
print(obj1)
print(obj2)
A.intro()

#%% class 2
class Car:
    # ���� �޼ҵ忡�� ������ ���� ����
    brand=""
    color=""
    price=0

    #������
    def __init__(self,brand="",color="",price=0):
        #��ü�� ������ �ֵ��� ���� ���⿡ ������.
        self.brand = brand
        self.color = color
        self.price = price

    def enginStart(self):
        print(self.brand + "�õ�Ŵ")
    
    def enginStop(self):
        print(self.brand+"�õ���")


momCar = Car("Benz","Yellow",35000)
dadyCar = Car()
myCar = Car()

# momCar.brand = "Benz"
# momCar.color = "Yellow"
# momCar.price = 35000

momCar.enginStart()