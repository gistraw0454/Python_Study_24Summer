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