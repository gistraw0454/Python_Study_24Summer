# 29�� - ����� ���� ó��, ���� �����
## ����� ����ó��
```py
#%% my exception 29
class NickNameError(Exception):
    pass

def checkNickName(name):
    if name=="�ٺ�":
        raise NickNameError #�ٺ���� �̸��� �Է��������� nicknameerror �߻�
    
nickname = input("�г���: ")

try:
    checkNickName(nickname)
    print("�г��� ���� ����!")
except NickNameError:
    print("��Ӿ�� ����� �� ����")

#%% my exception task
#�ܺο��� ä�� ���ڿ��� �޾ƿͼ� in���� ��Ӿ�˻縦 �Ѵ�
#�ù�,����,����,����
class BadWordError(Exception):
    pass
chat = ""

def checkChatting(temp):
    badWords=["�ù�","����","����","����"]
    for i in badWords:
        if i in temp:
            global chat
            chat = temp.replace(i,"**")
            raise BadWordError()
cnt=0
while True:
    chat = input("ä��[������:q] : ")
    if chat.lower() =='q':
        break
    try:
        checkChatting(chat)
        print(chat)
    except BadWordError:
        cnt+=1
        print("%dȸ ��Ӿ ����ϼ̽��ϴ�." %cnt)
        print(chat)
```

## ���������
```
���ϰ�ü = open("���","����")

����
-w : �ش� ��� ���� ����� (�������� ����)
-a : �ش� ��� ���� �߰��ϱ� (�������� ����)
-r : �ش� ��� ���� �б� (�ش� ��ο� ������ ������ ����)

#����ϱ�
���ϰ�ü.write("���ڿ�")

#�Է��ϱ�
���ϰ�ü.readlines()

���ϰ�ü.close(): ���۸� ������ ���Ͽ� ����ȴ�.
        �ݵ�� �۾��� ������ ���ϰ�ü��.close() ��� !
```

- ������: �� ��ġ�� ���� ã�ư� �� �ִ� ���
- �����: �� ��ġ�� ���� ��ΰ� ����ȴ�.
    - ., ..
