# 19�� - �÷��� - list �ǽ�
```py
#%% 1~100 ���� ���� �ְ� ���
dataList =[0]*100
for i in range(100):
    dataList[i]=i+1
print(dataList)
#%% 1~100 �� ¦���� �ְ� ���
dataList =[0]*50
for i in range(50):
    dataList[i]= (i+1)*2
print(dataList)
#%% A~F ���� �ְ� ���
dataList=[]
for i in range(6):
    dataList.append(chr(ord('A')+i))
print(dataList)
#%% A~F ���� �� C�����ϰ� ���
# dataList=[]
# for i in range(5):
#     if(i>1):
#         i+=1
#     dataList.append(chr(ord('A')+i))
# print(dataList)

dataList=[""]*5
tmp=0
for i in range(len(dataList)):
    tmp=i
    if tmp>1 :
        tmp+=1
    dataList[tmp]= chr(65+tmp)
print(dataList)

# dataList=[""]*5
# for i in range(len(dataList)):
#     dataList[i]=(i+1 if i>1 else i) + 65 
# print(dataList)
#%% aBcD..Z�ְ� ���
dataList = [""]*26
for i in range(len(dataList)):
    if (i%2==0) :
        dataList[i]= chr(ord('a') +i)
    else :
        dataList[i]= chr(ord('A') +i)
print(dataList)

for i in dataList:
    print(i,end="")

#%% "ABC"���� B�� Z�� ����
# ���ڿ��� ����� ���Ҽ�����
strList = "ABC"
strList.replace("B","Z")
strList = strList.replace("B","Z")
print(strList)

#%% �ڿ����� �ѱ۷� ����
# �Է� ��) 1024
# ��� ��) �ϰ��̻�
han = "�����̻�����ĥ�ȱ�"
num = int(input())
result = ""

while num != 0:
    result = han[num%10] + result
    num //=10

print(result)
```