#%% 1 �Է��Ѹ�ŭ hello �ݺ�
count = int(input("����: "))
if count<=0:
    print("�ٽ�")
else:
    n=0
    while(n!=count):
        print("%d��° Hello" %(n+1))
        n+=1
# %% 2 1���� 100���� 7�� ���
n=0
while(n<98):
    n+=7
    print(n)

#%% 3 �־��������� �󸶳� Ŀ�Ǹ� ���� �� ������?
coffee = 0
money = int(input("���־�"))
while money>=300:
    coffee+=1
    money-=300
    print('Ŀ��{}�� �ܵ�{}��'.format(coffee,money))

#%% 4 �ԷµȰ��� ��� (�ߺ�����)
numSet = set()
num=0
while len(numSet)<5:
    num= int(input("0~9������ ����: "))
    numSet.add(num)
print("��� �Էµƴ�")
print("�Էµ� ���� {}".format(numSet))

#%% 5 10�ǹ���� \n �ƴϸ� \t���
n=1
while(n<=100):
    if n%10==0:
        print(n)
    else:
        print(n,end="\t")
    n+=1

#%% 6 ������
n=1
dan =2
while n<=9:
    dan=2
    while dan<=9:
        print("%d*%d=%d" %(dan,n,dan*n),end="\t")
        dan+=1
    print()
    n+=1