#%% list test
dataList = [2,4,5,6]
print(len(dataList))
print(dataList[2])
print(dataList)

print("--------------------")

dataList.append(7)
print(dataList)

dataList.insert(1,3)
print(dataList)

print(dataList.index(7))    #index를 ret
if (-1 in dataList):
    print(dataList.index(-1))
else :
    print("없다")

print("-------------------------")

dataList.remove(4)  #값 삭제
print(dataList)

del dataList[4] # 해당 인덱스 값 삭제
print(dataList)

dataList[0]=20
print(dataList)

print(dataList[-1]) # 가장 마지막 요소

print(dataList[0:3]) # 3번째 indx포함안함
print(dataList[1:2])
print(type(dataList[1:2]))
#%%
dataList =[0]*100
print(len(dataList))

for i in dataList:
    print(i)
cnt=1
for i in dataList:
    i=cnt
    cnt+=1
print(dataList)

# %%
for i in range(len(dataList)):
    dataList[i]=i+1
print(dataList)

for i in dataList:
    print(i)
dataList = list(range(5))
print(dataList)

dataList=list(range(1,10,2))
print(dataList)