#%% 1 ������ȣ�������� ������ �����ض�
phone= input("��ȭ��ȣ���: ")
print("����: "+phone.split("-")[1])    #3ĭ¥�� �迭�̵ȴ�.

start = phone.index('-') +1
end = phone.index('-',start)    #start���� �����ؼ� - ã��
# end�� ���� �����̾ȵǴ� ���� -1 ���ʿ����

code = phone[start:end]
print("����: "+code)

#%% 2 �ùٸ� ����ڹ�ȣ�ΰ�?
comp_num = input("����� ��� ��ȣ\n��) 123-45-23452\n")
#ù��° - �ε��� ��ȣ�� 3�϶�
c1 = comp_num.find("-")==3
#�ι�° - �ε��� ��ȣ�� 6�϶�
c2 = comp_num.find("-",4)==6
#�� ���̰� 12 �϶�
c3 = len(comp_num) ==12
#�� ��ȣ�� ���� �������� �˻�
c4 = comp_num.replace("-","").isdecimal()
if c1 and c2 and c3 and c4:
    print("�ùٸ� ����� ��� ��ȣ")
else :
    print("�߸��� ����� ��� ��ȣ")

#%% 3
std='"��ö��",85'
name=std.split(",")[0].strip('""')
age = std.split(",")[1]
print("�̸��� {} ������ {}".format(name,age))
