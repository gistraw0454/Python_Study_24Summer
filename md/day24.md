# 24강 함수 심화 예제
## 전역변수
```py
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
```
- 함수 안에서 읽기 전역O 지역O
- 함수 안에서 수정 불가(global써주면 가능) 지역O
- 함수 밖에서 읽기 전역O 지역은 선언된 지역에서만가능
- 함수 밖에서 수정 전역O 지역X
