#%% 1 
class Person:
    population =0

    def __init__(self,name):
        self.name = name
        Person.population +=1
        print("{} is born".format(self.name))

    def __del__(self):  #del ��ü �ϸ� �����
        Person.population-=1
        print("{} is dead".format(self.name))

    @classmethod    #�̰ɾ��� classmethod�� cls�� �޴´� ����
    def get_population(cls):
        return cls.population

man = Person("james")
woman = Person("emily")
print("��ü �α��� : {}��".format(Person.get_population()))
del man
print("��ü �α��� : {}��".format(Person.get_population()))

#%% 2 shop class
class Shop:
    total =0
    menu_list = [{'������':3000},{'����':3000},{'Ƣ��':500},{'���':2000}]

    @classmethod
    def sales(cls,food,count):
        for menu in cls.menu_list:
            if food in menu:
                cls.total+=menu[food]*count
Shop.sales("������",1)
Shop.sales("���",2)
Shop.sales("Ƣ��",5)

print("����: {}��".format(Shop.total))

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
        print("���� ��������: {}".format(self.oil))
    
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
        print("���� ��������: {}".format(self.battery))
car = Hybrid(0,0)
car.add_oil(100)
car.charge(30)
car.hybrid_info()