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