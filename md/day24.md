# 24�� �Լ� ��ȭ ����
## ��������
```py
#%% �������� 
result =0 # ��������
# �ʱ�ȭ�� �ڿ��� ���� �ϱ�.
def add(num1,num2=0):
    global result #�̷��� ��������� ���������� result�� ���
    result =num1+num2
def sub(num1,num2):
    global result
    result =num1-num2
add(10)
sub(10,5)
print(result)
```
- �Լ� �ȿ��� �б� ����O ����O
- �Լ� �ȿ��� ���� �Ұ�(global���ָ� ����) ����O
- �Լ� �ۿ��� �б� ����O ������ ����� ��������������
- �Լ� �ۿ��� ���� ����O ����X
