#%% 1 
class Person:
    population =0

    def __init__(self,name):
        self.name = name
        Person.population +=1
        print("{} is born".format(self.name))

    def __del__(self):  #del 객체 하면 실행됨
        Person.population-=1
        print("{} is dead".format(self.name))

    @classmethod    #이걸쓰면 classmethod로 cls를 받는다 설정
    def get_population(cls):
        return cls.population

man = Person("james")
woman = Person("emily")
print("전체 인구수 : {}명".format(Person.get_population()))
del man
print("전체 인구수 : {}명".format(Person.get_population()))

#%% 2 shop class
class Shop:
    total =0
    menu_list = [{'떡볶이':3000},{'순대':3000},{'튀김':500},{'김밥':2000}]

    @classmethod
    def sales(cls,food,count):
        for menu in cls.menu_list:
            if food in menu:
                cls.total+=menu[food]*count
Shop.sales("떡볶이",1)
Shop.sales("김밥",2)
Shop.sales("튀김",5)

print("매출: {}원".format(Shop.total))

#%% 3 
class Car:
    max_oil = 50

    def __init__(self,oil):
        self.oil=oil
    def add_oil(self,oil):
        if oil <=0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil
    def car_info(self):
        print("현재 주유상태: {}".format(self.oil))
    
class Hybrid(Car):
    max_battery =30
    def __init__(self,oil,battery):
        super().__init__(oil)
        self.battery = battery
    def charge(self,battery):
        if battery <=0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery
    def hybrid_info(self):
        super().car_info()
        print("현재 충전상태: {}".format(self.battery))
car = Hybrid(0,0)
car.add_oil(100)
car.charge(30)
car.hybrid_info()