#%% ��ȭâ �ǽ� : person ��ųʸ��� ������ ��ȸ
person = {'�̸�': 'ȫ�浿','����':26,'������':82}

person['�̸�']
person['����']
person['������']

#%% ��ȭâ �ǽ� : student ��ųʸ��� ������ ��ȸ
students = {2019001:'�̼���', 2029002:"������",2020003:'������'}

students[2019001]

#%% ��ȭâ �ǽ� : ����Ʈ�� Ʃ�÷κ��� ���� �����
days_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
days_set = set(days_list)
days_set

fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple)
fruits_set

h_str='hello'
h_set=set(h_str)
h_set
#%% code 6-7 ) ������ �Լ� product_set() �� a,b ������ ������
def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}   # ���� for������ �̿��� ������
    return res

A={1,3}
B={2,4}

AXB = product_set(A,B)
print(AXB)

#%% code 6-8 ) ������ �Լ��� �̿��� ������ ������ ����
def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}   # ���� for������ �̿��� ������
    return res

def exp(input_set,exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res,input_set)
    return res

A={1,3}
A3=exp(A,3)
print(A3)

#%% code 6-9 ) �ֻ��� �ι� ���� ��� ��� ��� ���ϱ�
def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}   # ���� for������ �̿��� ������
    return res

cases ={1,2,3,4,5,6}
print(product_set(cases,cases))

#%% lab 6-12 ) ������ �ֻ����� ������ �� Ư���� �̻��� ���� Ȯ��
def tuple_sum(tup):
    if isinstance(tup,int):
        return tup
    else:
        accum=0
        for element in tup :
            accum += tuple_sum(element)
    return accum

def product_set(set1,set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}
    return res

def exp(input_set,exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res,input_set)
    return res


def prob_over(x):
    cases = {1, 2, 3, 4, 5, 6}
    all_cases = exp(cases, 3)
    total_cases = len(all_cases)
    favorable_cases = sum(1 for case in all_cases if tuple_sum(case) >= x)
    return 100*(favorable_cases / total_cases)


cases ={1,2,3,4,5,6}
case2times = (product_set(cases,cases))
case3times = product_set(cases,case2times)
print("�ֻ��� ���� ���� �߻��� �� �ִ� �����",len(case3times),"���� ��찡 �����մϴ�")
print("�ֻ��� ���� ���� ���� ���� ���� 10�̻��� ����", sum(1 for case in case3times if tuple_sum(case) >= 10),"�����Դϴ�")
#�ֻ����������� ���� ���� ���� Ư���Ѱ� x�̻��� ���� Ȯ���� ����ϴ� prob_over(x) �Լ��� ����� Ȯ������غ���
for x in range(3, 19, 1):
    print("�ֻ��� ���� ���� ���� ���� ���� {} �̻��� Ȯ����: {:.2f}".format(x,prob_over(x)), "%")