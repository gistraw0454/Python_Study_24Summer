#%% 1 ������� �ִ��� �纸�� 
def vending_machine(money):
    price =700
    change =0
    count = money //700
    for i in range(count):
        change = money - (i+1)*price
        print("������� {}��, �ܵ��� {}��".format(i+1,change))

vending_machine(3000)

#%% 2 ���� ��� ���ϱ�
def get_avg(marks):
    total=0
    average=0.0
    for i in list(marks.values()):
        total +=i
    average=total/len(marks)
    return average

    
marks = {'����':90,'����':80,'����':85} 
print("���: %.2f" %get_avg(marks))

#%% 3 ���Ǳ� ��ܰ� ��ü ���Ǳ� ���
total =0
wedding ={}
def gift(dic,who,money):
    global total
    total+=money
    dic[who]=money

gift(wedding,'����',5)
gift(wedding,'ö��',3)
gift(wedding,'����',10)

print("���Ǳ� ���: {}".format(wedding))
print("��ü ���Ǳ�: {}".format(total))