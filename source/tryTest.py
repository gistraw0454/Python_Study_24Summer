#%% 28 Exception test
try:
    int(input("�����Է� :"))
except Exception as e:
    print("������ �Է��Ͻÿ�")
print("�ݵ�� ����Ǿ���� ����")


try:
    print(10/0)
except ZeroDivisionError as e:
    # print(e.__str__)
    print("0���� ������ ����.")