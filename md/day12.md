# 12�� - if�� ���� �� �ǽ�, ���� ������
### if�� ����
```py
#%% if task
qMsg = "����� ��������?\n1.A��\n2.B��\n3.O��\n4.AB��"
choice = int(input(qMsg + "\n"))

answer_a = "����"
answer_b = "����"
answer_o = "����"
answer_ab = "����"
errMsg = "�ٽý��"

result =""
if choice == 1 :
    result = answer_a
elif choice == 2:
    result = answer_b
elif choice ==3:
    result = answer_o
elif choice == 4:
    result = answer_ab
else :
    result = errMsg

print(result)
```
> ���̽��� ���ǹ��� if���ۿ� ���� switch ����...;;;;

## ���Կ�����(���� ���� ���糷, ���� ������)
- +=, -=, *=,/=,%=,//=
### ���� 
- ��������� ���� ������ ��Ȯ�� �� �� �˾ƾ��Ѵ�.