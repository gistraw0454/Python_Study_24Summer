# 20�� - list�� tuple,dict
- mutable (���Ҽ��ִ�) : list
- immutable (���Ҽ�����) : tuple
```py
#%% mutable
dataList1=[1,2,3]
dataList2=dataList1

dataList2.append(4)
print(dataList1)
# dataList2�� �ٲ�µ� dataList1���� ����o

#%% immutable
dataTuple1 = (1,2,3)
# print(type(dataTuple1))
dataTuple2 = dataTuple1
dataTuple2 +=4,5

print(dataTuple1)
#dataTuple2�� �ٲ�µ� dataTuple1�� ����x
#�ִµ����͸� �������� ����, �˻� ����, ����x
# dataTuple1[0]=10 Ʃ���� ���� ���� �� �� ����.
```
## Dict
- �ѽ����� ����Ǿ� ����
- len()�� ����ϸ� �ѽ��� 1�� ī��Ʈ
- Ű���� �ߺ��ɼ� ������, ���� �ߺ��� �����ϴ�
- Ű ���� �ָ� �� Ű�� ¦�� ���� ������ �´�

###  DIct ����
```
dict �� = {Ű:��,Ű:��,...}
```
### Dict ���
- �߰� (Ű���� ���� ��)
    - `dict��[Ű] =��`
- ���� (Ű���� ���� ��)
    - `dict��[Ű] =��`
- ���� (�ѽ��� �����ȴ�)
    - `del dict��[Ű]`
- �˻�
    - `Ű in dict��` : Ű ���� ������ ��
    - `Ű not in dict��` : Ű ���� ������ ��

### KEY �и�
- list(dict��.keys())
### VALUE �и�
- dict��.values()