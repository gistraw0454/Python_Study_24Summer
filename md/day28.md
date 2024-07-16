# 28�� - ��ӿ���, ����ó��
### ��ӿ���
```py
# %% class variable
class A:

    seq=0               #���� seq��

    def __init__(self):
        A.seq+=1    
        self.num = A.seq

    def test(self):
        self.seq=10     #���� seq�� �ٸ���. (�ʵ忡 ���ǵ� seq)
obj1=A()
obj2=A()
obj3=A()
obj4=A()

obj1.test()
print(obj1.num)
print(obj1.seq)
print(obj2.num)
```

## ����ó��
- ����: �ɰ��� ����
- ����: �� �ɰ��� ����
    - ������ �߻��ߴ�? => ������ �޸𸮿� �Ҵ�ƴ�.

```
try:
    ������ �߻��� �� �ִ� ����
except �����̸� as ��ü:    //alias: ��Ī
    ���� �߻��� ������ ����
```

- ��� ���� Ŭ������ �θ� Ŭ������ Exception�̴�.
- � �������� ������� except�� ó���Ҷ����� "�����̸�"�ڸ��� ������ �ֻ��� �θ��� Exception�� �ۼ��Ѵ�
```py
#%% 28 Exception test
try:
    int(input("�����Է� :"))
except Exception as e:  #��� ����ó��
    print("������ �Է��Ͻÿ�")
print("�ݵ�� ����Ǿ���� ����")


try:
    print(10/0)
except ZeroDivisionError as e:  # 0���� ���������� ���ܸ� ó���ϰڴ�.
    # print(e.__str__)  #error �޼����� �޾ƿ� ����Ѵ�.
    print("0���� ������ ����.")
```