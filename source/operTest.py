#%% ���� �Է�
price = int(input("���� : "))

print(price * 0.9)

#%% ���� 2���� �Է¹ް� ����, ����, ����, ������
num1 = int(input("����1 : "))
num2 = int(input("����2 : "))

addResult = num1+num2
subResult = num1-num2
mulResult = num1*num2
divResult = num1//num2
modResult = num1%num2

print("%d + %d = %d" %(num1,num2,addResult))
print("%d - %d = %d" %(num1,num2,subResult))
print("%d * %d = %d" %(num1,num2,mulResult))
print("%d // %d = %d" %(num1,num2,divResult))
print("%d %% %d = %d" %(num1,num2,modResult))

#%% ���ǽ�
isOk = True
isOk = False
print(type(isOk))