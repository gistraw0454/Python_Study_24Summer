# 11�� - ���׿������� ����� if��
### ���׿����� ����
```py
#%% (2) �������� ����
qMsg = "����� ��������?\n1.A��\n2.B��\n3.O��\n4.AB��"
choice = int(input(qMsg + "\n"))

answer_a = "����"
answer_b = "����"
answer_o = "����"
answer_ab = "����"

result = (answer_a if choice == 1 else 
          answer_b if choice == 2 else
          answer_o if choice == 3 else
          answer_ab if choice == 4 else
          "�߸��� ����")

print(result)
```
-> �ʹ� �����ؿ�...
## ���
- ���ǹ�
    - if��
    ```
    if ���ǽ�:
        ���๮��
    if ���ǽ�:
        ���๮��
    ```
    
    - if else��
    ```
    if ���ǽ�:
        ���๮��
    elif ���ǽ�:
        ���๮��
    else:
        ���๮��
    ```
- �ݺ���
