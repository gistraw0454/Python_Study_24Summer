#%% 1 �޸��忡 ����
nation=['�׸���','���׳�','����','������','���þ�','��ũ��','�̱�','������']

file=open('nation.txt',"wt")    #t- ���� b-���̳ʸ�

for idx,country in enumerate(nation):
    if idx %2 ==0:
        file.write(nation[idx]+"-"+nation[idx+1]+"\n")
file.close()

#%% 2
old_file = open("����ó.txt","rt")
buffer = old_file.read()
n=buffer.count("011-")
buffer.replace("011-","010-")
print("�� {}���� 011 �����͸� ã�ҽ��ϴ�.".format(n))
old_file.close()

new_file = open("����ó.txt","wt")
new_file.write(buffer)
new_file.close()
print("������ �����Ϸ�")
