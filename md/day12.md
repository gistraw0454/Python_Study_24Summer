# 12강 - if문 예제 및 실습, 누적 연산자
### if문 예제
```py
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
```
> 파이썬은 조건문에 if문밖에 없다 switch 없대...;;;;

## 대입연산자(복합 대입 연사낮, 누적 연산자)
- +=, -=, *=,/=,%=,//=
### 변수 
- 저장공간과 값의 구분을 정확히 할 줄 알아야한다.
