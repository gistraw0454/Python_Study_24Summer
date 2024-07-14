#%% if test
n1Msg = "첫번째 정수 :"
n2Msg = "두번째 정수 :"

num1 = int (input(n1Msg))
num2 = int (input(n2Msg))

if (num1 > num2):
    print("큰값: "+ str(num1))
elif (num1==num2):
    print("같다")
else :
    print("큰값: "+str(num2))

#%% if task
qMsg = "당신의 혈액형은?\n1.A형\n2.B형\n3.O형\n4.AB형"
choice = int(input(qMsg + "\n"))

answer_a = "예민"
answer_b = "둔함"
answer_o = "밝음"
answer_ab = "찌질"
errMsg = "다시써라"

result =""
if choice == 1 :
    result = answer_a
elif choice == 2:
    result = answer_b
elif choice ==3:
    result = answer_o
elif choice == 4:
    result = answer_ab
else :
    result = errMsg

print(result)
# 파이썬은 조건문에 if문밖에 없다 switch 없대...;;;;
