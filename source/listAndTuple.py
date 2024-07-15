#%% mutable
dataList1=[1,2,3]
dataList2=dataList1

dataList2.append(4)
print(dataList1)
# dataList2를 바꿨는데 dataList1에도 영향o

#%% immutable
dataTuple1 = (1,2,3)
# print(type(dataTuple1))
dataTuple2 = dataTuple1
dataTuple2 +=4,5

print(dataTuple1)
#dataTuple2를 바꿨는데 dataTuple1에 영향x
#있는데이터를 가져오는 목적, 검색 목적, 변경x
# dataTuple1[0]=10 튜플의 값은 변경 할 수 없다.