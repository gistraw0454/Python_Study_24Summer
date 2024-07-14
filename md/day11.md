# 11강 - 삼항연산자의 응용과 if문
### 삼항연산자 예제
```py
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
```
-> 너무 불편해요...
## 제어문
- 조건문
    - if문
    ```
    if 조건식:
        실행문장
    if 조건식:
        실행문장
    ```
    
    - if else문
    ```
    if 조건식:
        실행문장
    elif 조건식:
        실행문장
    else:
        실행문장
    ```
- 반복문
