#%% 1 ������ ��λ���ض�
money=10000
while True:
    print("���� {}���� �ִ�.".format(money))
    if money==0:
        break
    spend= int(input("����� �ݾ� �Է�: "))
    if spend <=0:
        print("0������ �ݾ��� ����� �� ����")
    elif spend > money:
        print("{}�� �����ϴ�".format(spend-money))
    else:
        money-=spend

#%% 2 ���� ���
while True:
    star = int(input("�̹� ��ȭ�� ������ �Է��϶�"))
    if star >=1 and star <=5:
        print("����: {}".format('*'*star))
        break   
    else:
        print("1~5������ �Է�")
    
#%% 3 ����� ��й�ȣ ���߱�
key = 'qwerty'
count = 0
while Ture:
    if count ==5:
        print("�Է�Ƚ�� �ʰ�")
        break
    pw = input("��й�ȣ: ")
    if pw==key:
        print("��й�ȣ ����")
        break
    count +=1

#%% 4 Ȧ�� �ܸ� �ش� �ܼ���ŭ ���������ϱ�
for dan in range(2,10):
    if dan%2==0:
        print()
        continue
    for i in range(1,dan+1):
        print("{}*{}={}".format(dan,i,dan*i))