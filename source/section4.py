#%% 1 ���ڸ������� �����ڸ��� �����ڸ��� ���
num = int(input("10~99 ������ ������ �Է��ϼ���"))
print("�����ڸ�: %d, �����ڸ�: %d" %(num//10,num%10))

#%% 2 �ʸ� �Է��ϸ� �ú��ʷ� ���
times = int(input("�ʸ� �Է��ϼ���"))
hour = times//3600
minute = times%3600 //60
second = times%60

print("%d�ð�%d��%d��" %(hour,minute,second))

#%% 3 ���ڸ������� ���ڸ��� ����/���� �ٹ� ���
emp_no = int(input("4�ڸ� �����ȣ�� �Է��ض�"))
emp_last_no = emp_no%10
print("�ٹ��ð��� %s�Դϴ�" %('����'if emp_last_no >=5 else '����'))

#%% 4 
print("�ѹڽ��� ����� 20�� ���µ�, ��� �ڽ��� �ʿ��ұ��?")
ramen= int(input("��鰳��:"))
print(ramen//20 if ramen%20==0 else ramen//20+1)

#%% 5 �հ� ���հ� ���
kor=int(input("��������: "))
eng=int(input("��������: "))
math=int(input("��������: "))

total = kor+eng+math
avg = total/3

print( '�հ�' if avg >=80 else '���հ�')