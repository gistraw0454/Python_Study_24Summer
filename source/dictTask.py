#%% dict test
numDict = {"even":[2,4,6],"odd":[1,3,5]}
for i in numDict["even"]:
    print(i)

numListDict = {"1�г�":[[30,40,50],[80,90,100]]}
for i in numListDict["1�г�"]:
    for j in i:
        print(j)
    print("============")

#%% dict task �л�����
#�л� �̸��� �л������� �ް� �߰�,����,����,���
title = "�л� ���� ���� ���α׷�\n"
msg = "1.�߰�\n2.����\n3.����\n4.���\n5.������\n"
errMsg = "�ٽ� �õ����ּ���"

studentDict = {}
subjectList = ["����", "����", "����"]

while True:
    try:
        choice = int(input(title + msg))
    except ValueError:
        print(errMsg)
        continue

    if choice == 1:
        name = input("�л� �̸�: ")
        if name not in studentDict:
            scores = input("������ ���� �� ������ �Է��ϼ���\n����, ����, ����: ").split(",")
            if len(scores) == 3:
                studentDict[name] = list(map(int, scores))
            else:
                print("�߸��� �Է��Դϴ�. �ٽ� �õ����ּ���.")
        else:
            print("�̹� ��ϵ� �л��Դϴ�.")
    elif choice == 2:
        sub_choice = int(input("1.�л��� ����\n2.���� ����\n"))
        name = input("������ �л���: ")
        if sub_choice == 1:
            if name in studentDict:
                new_name = input("���ο� �л���: ")
                studentDict[new_name] = studentDict.pop(name)
            else:
                print("�������� �ʴ� �л��Դϴ�.")
        elif sub_choice == 2:
            if name in studentDict:
                sub_choice = int(input("1.���� ����\n2.���� ����\n3.���� ����\n"))
                if 1 <= sub_choice <= 3:
                    new_score = int(input("���ο� ����: "))
                    studentDict[name][sub_choice - 1] = new_score
                else:
                    print("�߸��� �����Դϴ�.")
            else:
                print("�������� �ʴ� �л��Դϴ�.")
    elif choice == 3:
        name = input("������ �л���: ")
        if name in studentDict:
            del studentDict[name]
        else:
            print("�������� �ʴ� �л��Դϴ�.")
    elif choice == 4:
        for name, scores in studentDict.items():
            print(f"{name}:")
            for idx, score in enumerate(scores):
                print(f"  {subjectList[idx]}: {score}")
    elif choice == 5:
        break
    else:
        print(errMsg)
