# %% (1) �������
qMsg=("���� �� ���α׷��� �� �ƴ� ����?")
choiceMsg=("1.JAVA\n2.���̽�\n3.C���\n4.���վ�\n")

choice= int(input (qMsg+'\n'+choiceMsg))

answer = 4

result ="����" if choice == answer else "����" if choice>=1 and choice <=4 else "�߸��� �Է�" 
print(result)

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
