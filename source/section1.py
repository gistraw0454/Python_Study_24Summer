#%% 1 �л��������
student="31025"
# 3 10 25
# 0 12 34
grade = student[0]
classNum= student[1:3]
stdNum=student[3:]

print(grade + "�г�" + classNum +"��"+ stdNum +"��")

#%% 2 ������ȣ ���
car1 = "����2��1234"
car2 = "10��1234"
car3 = "288��1234"

c1Num = car1[-4:]
c2Num = car2[-4:]
c3Num = car3[-4:]

print(car1+"�� ������ȣ: "+c1Num)
print(car2+"�� ������ȣ: "+c2Num)
print(car3+"�� ������ȣ: "+c3Num)

#%% 3 ���ڿ��� ����� �ִ� ���� ���
strData = "maple"
print(strData[len(strData)//2])

#%% 4 ����Ʈ 3~7 �����ϰ� ���߿� 2��°�� ����
dataList = [0] *10

for i in range(10):
    dataList[i] = (i+1)*10

print(dataList)

result = dataList[2:7]
print("3��°���� 7��°���� : "+str(result))
print("���߿��� 2��° ��� : "+str(result[1]))

#%% 5 ��ųʸ��� ���Ϻ� �޴� ����ϱ�
menu = {'��':'������','��':'���꽽','��':'�Ⱥ�ä'}
print("�ݿ��� : "+menu["��"])
print("����� : "+menu["��"])
print("�Ͽ��� : "+menu["��"])
