#%% 1 ������ ���� ���� �ο�
score = int(input("����: "))
grade =''
if score >=90:
    grade ='A'
elif score >=80:
    grade ='B'   
elif score >=70:
    grade ='C'  
elif score >=60:
    grade ='D'   
else:
    grade = 'F'

print(grade)

#%% 2 ������ ������ �Է¹ް� 3�� ������� �Ǵ�
num =int (input("����: "))
msg=""
if num%3 ==0:
    msg = "%d�� 3�� ����Դϴ�." %num
else:
    msg = "%d�� 3�� ����ƴմϴ�." %num

print(msg)

#%% 3 �� ������ ���� ū �� 
n1 =int (input("����1: "))
n2 =int (input("����2: "))
n3 =int (input("����3: "))

if n1>=n2 and n1>=3:
    msg = "%d�� ���� ū��" %n1
elif n2>=n1 and n2>=n3:
    msg = "%d�� ���� ū��" %n2
else :
    msg = "%d�� ���� ū��" %n3
print(msg)

#%% 4 ������ȣ�� ¦���� ���డ��, Ȧ���� ����Ұ���
car_no = input("������ȣ :")
if int(car_no[-1])%2==0:
    print("%s�� ���� ���డ��" %car_no)
else:
    print("%s�� ���� ���� �Ұ���" %car_no)