#%% 1 1����5���� ���
for i in range(5):
    print(i)
#%% 2 0���� �Է��������� ���� ����
sumTo=int(input("���� ���� : "))
result =0
for i in range(sumTo):
    result +=i+1
print(result)

#%% 3 ������ ����Ʈ��  �߰��ϰ� ���
cnt = int(input("��� ����??"))
fruitList=[]
for i in range(cnt):
   fruitList.append(input("%d��° ����?"%(i+1)))
print(fruitList)

#%% 4 min�Լ� ����ϱ�
# min(��, �ּҰ�) ; ���� �ּҰ��� ���Ѿ��Ѵ�.
exam =[99,78,100,91,81,85,54,100,71,50]
score = [min(n+5,100)for n in exam]
print(score)

#%% 5 369 ����
for n in range(1,100):
    units = n%10
    tens= n//10
    c1 = units%3==0 and units!=0
    c2 = tens%3 ==0 and tens!=0

    if c1 and c2:
        print("¦¦", end="\t")
    elif c1 or c2:
        print("¦",end="\t")
    else:
        print(n,end="\t")
    if n%10==0:
        print()