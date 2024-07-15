# 19강 - 컬렉션 - list 실습
```py
#%% 1~100 까지 값을 넣고 출력
dataList =[0]*100
for i in range(100):
    dataList[i]=i+1
print(dataList)
#%% 1~100 중 짝수만 넣고 출력
dataList =[0]*50
for i in range(50):
    dataList[i]= (i+1)*2
print(dataList)
#%% A~F 까지 넣고 출력
dataList=[]
for i in range(6):
    dataList.append(chr(ord('A')+i))
print(dataList)
#%% A~F 까지 중 C제외하고 출력
# dataList=[]
# for i in range(5):
#     if(i>1):
#         i+=1
#     dataList.append(chr(ord('A')+i))
# print(dataList)

dataList=[""]*5
tmp=0
for i in range(len(dataList)):
    tmp=i
    if tmp>1 :
        tmp+=1
    dataList[tmp]= chr(65+tmp)
print(dataList)

# dataList=[""]*5
# for i in range(len(dataList)):
#     dataList[i]=(i+1 if i>1 else i) + 65 
# print(dataList)
#%% aBcD..Z넣고 출력
dataList = [""]*26
for i in range(len(dataList)):
    if (i%2==0) :
        dataList[i]= chr(ord('a') +i)
    else :
        dataList[i]= chr(ord('A') +i)
print(dataList)

for i in dataList:
    print(i,end="")

#%% "ABC"에서 B를 Z로 변경
# 문자열은 상수니 변할수없음
strList = "ABC"
strList.replace("B","Z")
strList = strList.replace("B","Z")
print(strList)

#%% 자연수를 한글로 변경
# 입력 예) 1024
# 출력 예) 일공이사
han = "공일이삼사오육칠팔구"
num = int(input())
result = ""

while num != 0:
    result = han[num%10] + result
    num //=10

print(result)
```