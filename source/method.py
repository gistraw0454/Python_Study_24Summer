#%% method
def f(x):
    return 2*x+1
print(f(7)+9)
#%%
def add(a,b):
    return a+b
print(add(2,3))
#%%
def printFrom1To100():
    for i in range(100):
        print(i+1)
printFrom1To100()
#%%
def sumFrom1To10():
    sum=0
    for i in range(10):
        sum +=i+1
    return sum
sumFrom1To10()
#%%
def changeToNegative(num):
    result =0
    if num>0:
        result = num*(-1)
    else :
        result = False
    return result

result= changeToNegative(int(input("자연수:")))
if not result:
    print("자연수만 가능")
else:
    print(result)
#%%
def printSumFrom1(end):
    result=0
    for i in range(end):
        result +=i+1
    return result

printSumFrom1(10)
#%%
def change(num):
    if num>-1:
        num+=1
    else :
        num= False
    return num
change(1)

#%%5개의정수를 오름차순으로 정렬해주는 메소드
def sortASC(numList):
    for i in range(len(numList)-1):
        for j in range(i+1,len(numList)):
            if numList[i] > numList[j]:
                tmp=numList[i]
                numList[i]=numList[j]
                numList[j]=tmp

numList=[9,7,3,1,2]
sortASC(numList)
print(numList) # numlist 자체가 주소값이라서 따로 주소값을 전달하지 않아도 list내부 값이 변화함
