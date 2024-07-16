#%% 28 - inheritance test 2
class Car:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    def engineStart(self):
        print(self.brand+"¿­¼è·Î ½Ãµ¿Å´")

    def engineStop(self):
        print(self.brand+"¿­¼è·Î ½Ãµ¿²û")

class SuperCar(Car):
    def __init__(self,brand,color,price,mode):
        super().__init__(brand,color,price)
        self.mode = mode
    def engineStart(self):
        print(self.brand + "À½¼ºÀ¸·Î ½Ãµ¿Å´")

    def openRoof(self):
        print("ÁöºØ¿­¸²")

    def closeRoof(self):
        print("ÁöºØ ´ÝÈû")
    
ferrari = SuperCar("ferrari","red",35000,"daily")
ferrari.engineStart()
ferrari.engineStop()
ferrari.openRoof()
ferrari.closeRoof()
# %% class variable
class A:

    seq=0

    def __init__(self):
        A.seq+=1
        self.num = A.seq

    def test(self):
        self.seq=10
obj1=A()
obj2=A()
obj3=A()
obj4=A()

obj1.test()
print(obj1.num)
print(obj1.seq)
print(obj2.num)