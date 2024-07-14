# 16강 - while 문
## 제어문
- 반복문
    - for 문
        - 반복횟수를 알 때 사용하는 목적
    - while 문
        ```
        while 조건식 :
            반복문장
        ```
        - 조건식이 참이면 반복
        - 반복횟수를 모를 때 사용하는 목적
        - 무한반복일 경우, 특정 조건에 break를 사용해 탈출
```py
#%% while Test
#이름 10번 출력
cnt = 0
while cnt!=10:
    print("{}. 한동석".format(cnt+1))
    cnt+=1
#횟수를 알때는 for문이 낫다.

```