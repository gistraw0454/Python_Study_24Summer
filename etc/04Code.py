#%% code 4-6 ) "���ڿ�"*n �ϸ� n�� �ݺ��Ǿ� ��µ�.
def print_hello (n):
    print("hello "*n)

print_hello(3)

#%% code 4-13 ) Ʃ�÷� ��ȯ�ϴ� ���߹�ȯ��
def get_root(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return r1,r2

result1, result2 = get_root(1,2,-8)
print(result1, result2)

#%% lab 4-7 ) �������� �ѷ� ��ȯ {:1f} �Ẹ��.!
def circle_area_circum(radius):
    area = radius**2*3.14
    circum = radius*2*3.14
    return area,circum

radius = 10
area , circum = circle_area_circum(radius)
print("������ {}�� ���� ������ {:.1f}, ���� �ѷ��� {:.1f}".format(radius,area,circum))

#%% code 4-17 ) global Ű���带 ����� ���������� ���� ���
def print_sum():
    global a,b
    a=100
    b=100
    result = a+b
    print("�Լ����� a+b��",result)

a=10
b=10
print_sum()
result = a+b
print("�Լ��ܺ� a+b��",result)

#%% code 4-26 ) �������ڸ� ������ �Լ��� ���ǿ� ȣ��
def greet(*names):
    for name in names:
        print("�ȳ��ϼ���",name,"��")
greet("ȫ�浿",'�̼���','�庸��')
greet("james",'thomas')

#%% code 4-27 ) ���� ���ڸ� ������ �Լ����� len�Լ� ���
def foo(*args):
    print("���ڰ���",len(args))
    print("���ڵ�",args)    # Ʃ�����·� ��Ÿ����.
foo(100,200,300)
foo("��","��")

#%% code 4-29 ) factorial 
def fac(n):
    if n <=1 :
        return 1
    return n*fac(n-1)

print(fac(5))

#%% code 4-30 ) fibonacci
def fibo(n):
    if n<=1:
        return n
    else :
        return fibo(n-1) + fibo(n-2)
    
# ��� �Ǻ���ġ��
n = 10

if n <= 0:
    print("������ �Ұ�")
else :
    for i in range(n):
        print(fibo(i),end=" ")

#%% ��ȭâ�ǽ� : 1000 ���� ��ǥ ��¹��
print('{:,}'.format(1234567890))