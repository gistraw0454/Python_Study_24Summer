#%% while Test
#이름 10번 출력
cnt = 0
while cnt!=10:
    print("{}. 한동석".format(cnt+1))
    cnt+=1
#횟수를 알때는 for문이 낫다.

#%% while 혈액형 task
qMsg = "당신의 혈액형은?\n1.A형\n2.B형\n3.O형\n4.AB형\n5.나가기\n"


answer_a = "예민"
answer_b = "둔함"
answer_o = "밝음"
answer_ab = "찌질"
errMsg = "다시써라"

while(1):
    result =""
    choice = int(input(qMsg + "\n"))
    if choice == 1 :
        result = answer_a
    elif choice == 2:
        result = answer_b
    elif choice ==3:
        result = answer_o
    elif choice == 4:
        result = answer_ab
    elif choice == 5:
        break
    else :
        result = errMsg

    print(result)

#%% while 퀴즈 task
qMsg=("다음 중 프로그래밍 언어가 아닌 것은?")
choiceMsg=("1.JAVA\n2.파이썬\n3.C언어\n4.망둥어\n")
result =""
answer = 4

while result != "정답!" : 
    choice= int(input (qMsg+'\n'+choiceMsg))
    if choice == answer:
        result = "정답!"
    elif choice >= 1 and choice <=4 : 
        result = "오답!"
    else:
        result = " 다시 "
    print(result)
# %%
