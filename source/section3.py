#%% 1 두실수의 합
num1 = float(input("첫번째 실수 : "))
num2 = float(input("두번째 실수 : "))

print("{n1}와 {n2}의 합은 {result}입니다.".format(n1=num1,n2=num2,result=num1+num2))

#%% 2 해당 월이 몇일까지 있는지?
days = [31,28,31,30,31,30,31,31,30,31,30,31]
month = int(input("1부터 12사이의 월을 입력하세요"))
print("%d월은 %d일 까지 있습니다." %(month,days[month-1]))

#%% 3 영어사전 만들기
english_dict= {'flower':'꽃', 'fly':'날다', 'floor':'바닥'}

word = input("영어 단어를 입력하세요")
print("{}:{}".format(word,english_dict[word]))

#%% 4 
#set : 집합, 중복된 원소를 담을 수 없다.
# 값의 유무 검사가 목적이다.

result = set()
for i in range(3):
    result.add(input("희망하는 수학 여행지를 입력하세요"))

print("조사된 수학여행지는 {}입니다.".format(result))

