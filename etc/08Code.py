#%% code 8-16 ) ����ڷκ��� �Է¹��� �ټ��� ������ �����ϴ� ���α׷�
f=open('data5.txt','w')
for _ in range(5):
    n = input("������ �Է��Ͻÿ�")
    f.write(n)
    f.write("\n")
f.close()

#%% code 8-17 ) ���Ϸκ��� ������ �Է¹޾� �հ� ����� ���
f=open('data5.txt','r')
su =0
for _ in range(5):
    n = int(f.readline())
    su+=n
print("��={} ���={}".format(su,su/5))
f.close()
