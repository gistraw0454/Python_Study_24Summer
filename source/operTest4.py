#%% (1) 대소비교
# 두 정수 입력 받기
n1Msg = "첫번째 정수 : "
n2Msg = "두번째 정수 : "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

# num1 이 num2 보다 크면 num1이 큰값
# num1 이 num2 보다 작으면 num2가 큰값
# else 쪽에서 한번더 두수가 같은지 물어본다.
# 만약 두수가 같으면 두수가 같습니다. 고, 두수가 같지않다면 num2가 더큰 것으로 출력
result = num1 if num1 > num2 else "두수가 같습니다" if num1== num2 else num2
print("더큰값 : {}".format(result))
# %% (2) 퀴즈게임
qMsg=("다음 중 프로그래밍 언어가 아닌 것은?")
choiceMsg=("1.JAVA\n2.파이썬\n3.C언어\n4.망둥어\n")

choice= int(input (qMsg+'\n'+choiceMsg))

answer = 4

result ="정답" if choice == answer else 오답 
print(result)
#%% 연산과 연결
print(10+9) #연산
print('10'+'9') #연결
print('10'+str(9))