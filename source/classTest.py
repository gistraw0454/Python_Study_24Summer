#%% interitance
class A : 
    def __init__(self,data=10):
        self.data = data
        print("�θ� ������ ȣ��")

    def printData(self):
        print(self.data)
    
    def show(self):
        print("�θ� �޼ҵ�")
    

class B(A):
    def __init__(self,data,data2):
        # A.__init__(self,data)
        super().__init__(data) # super�� �θ�����ڸ� ȣ���ϴµ�, self���� �Ѱ���
        self.data2=data2

    def printData2(self):
        print(self.data,self.data2)

    #Overrideing ������, ������
    def printData(self):
        print(self.data,self.data2)

# b = B()
# b.printData() # �ڽĻ����ڰ� �θ� �����ڸ� �ڵ����� ȣ����
# b.show()

b=B(30,20)
b.printData()
b.printData2()