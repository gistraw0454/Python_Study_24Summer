#%% interitance
class A : 
    def __init__(self,data=10):
        self.data = data
        print("부모 생성자 호출")

    def printData(self):
        print(self.data)
    
    def show(self):
        print("부모 메소드")
    

class B(A):
    def __init__(self,data,data2):
        # A.__init__(self,data)
        super().__init__(data) # super로 부모생성자를 호출하는데, self까지 넘겨줌
        self.data2=data2

    def printData2(self):
        print(self.data,self.data2)

    #Overrideing 재정의, 다형성
    def printData(self):
        print(self.data,self.data2)

# b = B()
# b.printData() # 자식생성자가 부모 생성자를 자동으로 호출함
# b.show()

b=B(30,20)
b.printData()
b.printData2()