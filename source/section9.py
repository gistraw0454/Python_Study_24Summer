#%% 1 
#enumerate�� ����Ʈ�� �ε����� ���� �Բ� �����´�.
rainbow = ['red','orange','yellow','blue','navy','purple']
for idx,value in enumerate(rainbow):
    print("�������� {}��° ���� {}�Դϴ�".format(idx+1,value))


#%% 2
exam=[]
print("�����Է��ض�")
print("���̻� �Է��� ������ ������ ������ ���")
while(True):
    score =int(input("���� �Է�"))
    if score <0:
        break
    exam.append(score)
avg = sum(exam)/len(exam)
max1 = max(exam)
min1 = min(exam)

print("���: %.2f, �ִ�: %d, �ּ�: %d" %(avg,max1,min1))