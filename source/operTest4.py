#%% (1) ��Һ�
# �� ���� �Է� �ޱ�
n1Msg = "ù��° ���� : "
n2Msg = "�ι�° ���� : "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

# num1 �� num2 ���� ũ�� num1�� ū��
# num1 �� num2 ���� ������ num2�� ū��
# else �ʿ��� �ѹ��� �μ��� ������ �����.
# ���� �μ��� ������ �μ��� �����ϴ�. ��, �μ��� �����ʴٸ� num2�� ��ū ������ ���
result = num1 if num1 > num2 else "�μ��� �����ϴ�" if num1== num2 else num2
print("��ū�� : {}".format(result))
# %% (2) �������
qMsg=("���� �� ���α׷��� �� �ƴ� ����?")
choiceMsg=("1.JAVA\n2.���̽�\n3.C���\n4.���վ�\n")

choice= int(input (qMsg+'\n'+choiceMsg))

answer = 4

result ="����" if choice == answer else ���� 
print(result)
#%% ����� ����
print(10+9) #����
print('10'+'9') #����
print('10'+str(9))