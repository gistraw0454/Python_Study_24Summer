#%% dict
�߱��� = {"¥���":1500,"«��":2500}
print(len(�߱���))
print(�߱���["¥���"]) # value���� ������������ ����

if "¥���" in �߱���:
    �߱���["¥���"]=4000
print(�߱���)

if "������" not in �߱���:
    �߱���["������"] =9000 #�߰�

print(�߱���)

# del �߱���["«��"]
# print(�߱���)

for i in �߱���.keys():
    print(i)
for i in range(len(�߱���)):
    print(str(i+1)+". "+list(�߱���.keys())[i])

total =0
for i in �߱���.values():
    total+=i
avg = total/len(�߱���)
print("��հ���: %.2f��" %avg)

#%% dict 2
#��� �Է¹ް� ���� ���
# 2�Է½� B ���
# 1~5���, A~F����

# dict ������ָ� ������ �˾Ƽ� dict���·� ����
scoreDict={}
# 0 1 2 3 4
# A B C D F
for i in range(5):
    scoreDict[i+1]= chr(i+1+ord('A')) if i==4 else chr(i
                                                       +ord('A'))
print(scoreDict)

rating=int(input("���: "))
for i in range(5):
    if rating == i+1:
        print(scoreDict[i+1] + "�����Դϴ�\n")
        break