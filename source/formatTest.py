#%% ���˽�Ʈ��
data=10
data2 = "%d" %100
# ��������� data���� ������, data : %d�� ��µȴ�.
print("data : %d" %data)
print(type(data2)) # ��� ���Ĺ��ڰ� ���� ""�������� str ó��
print(data2)
# %% ���� test 2
data1 = 10
data2 = 10.4231 # f�� ���� 7�ڸ��� ���;��ϴµ� format�� ��� �� �����س��� �� ��ŭ�� ����
data3 = 'A' #�굵 ���ڿ���
data4 ="abc"
print("data1 : {}".format(data1))
print("data1 : {}\ndata2 : {}".format(data1,data2))
print("data3 : %s" %data3)
print("data3 : %c" %data3)
print("data4 : %s" %data4)
# �ڵ� ����ȯ
print("data4 : %c" %65)
# %% �ڵ� ����ȯ
# // : �� ������
print(10/3)
print(10//3)
# ���� ����ȯ
print(10//3.0)
print(float(10)//3)
