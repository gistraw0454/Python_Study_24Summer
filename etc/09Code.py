#%% code 9-13 ) __add__, __sub__, __str__ Ư�� �޼ҵ�� �������� ����
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector2D(self.x-other.x,self.y-other.y)
    
    def __str__(self):
        return '({},{})'.format(self.x,self.y)
    
v1 = Vector2D(30,40)
v2 = Vector2D(10,20)

v3 = v1+v2  # vector2d�� +������ ���ǵǾ������� __add__�� ����ȴ�. v1.__add__(v2) ���൵ ����
print(v3)
v4 = v1-v2
print(v4)