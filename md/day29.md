# 29강 - 사용자 예외 처리, 파일 입출력
## 사용자 예외처리
```py
#%% my exception 29
class NickNameError(Exception):
    pass

def checkNickName(name):
    if name=="바보":
        raise NickNameError #바보라는 이름을 입력했을때만 nicknameerror 발생
    
nickname = input("닉네임: ")

try:
    checkNickName(nickname)
    print("닉네임 생성 성공!")
except NickNameError:
    print("비속어는 사용할 수 없다")

#%% my exception task
#외부에서 채팅 문자열을 받아와서 in으로 비속어검사를 한다
#시발,씨발,ㅅㅂ,ㅆㅂ
class BadWordError(Exception):
    pass
chat = ""

def checkChatting(temp):
    badWords=["시발","씨발","ㅅㅂ","ㅆㅂ"]
    for i in badWords:
        if i in temp:
            global chat
            chat = temp.replace(i,"**")
            raise BadWordError()
cnt=0
while True:
    chat = input("채팅[나가기:q] : ")
    if chat.lower() =='q':
        break
    try:
        checkChatting(chat)
        print(chat)
    except BadWordError:
        cnt+=1
        print("%d회 비속어를 사용하셨습니다." %cnt)
        print(chat)
```

## 파일입출력
```
파일객체 = open("경로","목적")

목적
-w : 해당 경로 내용 덮어쓰기 (기존내용 삭제)
-a : 해당 경로 내용 추가하기 (기존내용 유지)
-r : 해당 경로 내용 읽기 (해당 경로에 파일이 없으면 오류)

#출력하기
파일객체.write("문자열")

#입력하기
파일객체.readlines()

파일객체.close(): 버퍼를 비워줘야 파일에 적용된다.
        반드시 작업이 끝나면 파일객체명.close() 사용 !
```

- 절대경로: 내 위치가 어디든 찾아갈 수 있는 경로
- 상대경로: 내 위치에 따라 경로가 변경된다.
    - ., ..
