# 4강 - 출력함수와 변수의 사용
## 제어문자 
- 반드시 따옴표 안에서 사용한다.
`\n`,`\t`,`\\`,`\"`,`\'`
### print()는 default로 end='\n'을 가지고있다.
```py
#%% (1) test
print("자기소개", end='\n') # default
print("이름 :", end='')
print("한동석\n나이 : 10살")
# %%
```

## 포맷스트링 이용하기 (print())
`print("이름: %s" %name)`