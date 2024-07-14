# %% (1) 퀴즈게임
qMsg=("다음 중 프로그래밍 언어가 아닌 것은?")
choiceMsg=("1.JAVA\n2.파이썬\n3.C언어\n4.망둥어\n")

choice= int(input (qMsg+'\n'+choiceMsg))

answer = 4

result ="정답" if choice == answer else "오답" if choice>=1 and choice <=4 else "잘못된 입력" 
print(result)

#%% (2) 혈액형별 성격
qMsg = "당신의 혈액형은?\n1.A형\n2.B형\n3.O형\n4.AB형"
choice = int(input(qMsg + "\n"))

answer_a = "예민"
answer_b = "둔함"
answer_o = "밝음"
answer_ab = "찌질"

result = (answer_a if choice == 1 else 
          answer_b if choice == 2 else
          answer_o if choice == 3 else
          answer_ab if choice == 4 else
          "잘못된 선택")

print(result)
