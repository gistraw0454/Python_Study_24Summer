#%% while Test
#�̸� 10�� ���
cnt = 0
while cnt!=10:
    print("{}. �ѵ���".format(cnt+1))
    cnt+=1
#Ƚ���� �˶��� for���� ����.

#%% while ������ task
qMsg = "����� ��������?\n1.A��\n2.B��\n3.O��\n4.AB��\n5.������\n"


answer_a = "����"
answer_b = "����"
answer_o = "����"
answer_ab = "����"
errMsg = "�ٽý��"

while(1):
    result =""
    choice = int(input(qMsg + "\n"))
    if choice == 1 :
        result = answer_a
    elif choice == 2:
        result = answer_b
    elif choice ==3:
        result = answer_o
    elif choice == 4:
        result = answer_ab
    elif choice == 5:
        break
    else :
        result = errMsg

    print(result)

#%% while ���� task
qMsg=("���� �� ���α׷��� �� �ƴ� ����?")
choiceMsg=("1.JAVA\n2.���̽�\n3.C���\n4.���վ�\n")
result =""
answer = 4

while result != "����!" : 
    choice= int(input (qMsg+'\n'+choiceMsg))
    if choice == answer:
        result = "����!"
    elif choice >= 1 and choice <=4 : 
        result = "����!"
    else:
        result = " �ٽ� "
    print(result)
# %%
