#%% method task
# 5개의 정수 중 최댓값과 최소값을 구해주는 메소드
def getMaxAndMin(dataList):
    maxdata =dataList[0] 
    mindata =dataList[0] 
    for i in range(1,len(dataList)):
        if maxdata < dataList[i] : maxdata = dataList[i]
        if mindata > dataList[i] : mindata = dataList[i]
    return maxdata, mindata
# tuple이 return 된다.

dataList = [3,5,7,8]
print(getMaxAndMin(dataList))

#%% 소문자 대문자로 바꾸기
def changeToUpper(string):
    result =""
    for i in string:
        if (i>='a' and i<='z'):
            result += chr(ord(i) - ord('a') + ord('A'))
        else:
            result += i
    return result
print(changeToUpper("Apple"))

#%% 한글을 정수로 바꿔주는 메소드 (일공이사 -> 1024)
def hanToNum(dataStr):
    han = "공일이삼사오육칠팔구"

    result =0
    for i in dataStr:
        result = result*10+han.index(i)
    return result

dataStr="일공이사"
print(hanToNum(dataStr))

#%% 전역변수 
result =0 # 전역변수
# 초기화는 뒤에서 부터 하기.
def add(num1,num2=0):
    global result #이렇게 선언해줘야 전역변수로 result를 사용
    result =num1+num2
def sub(num1,num2):
    global result
    result =num1-num2
add(10)
sub(10,5)
print(result)
# %%
