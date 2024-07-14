#%% 문자 형변환
print("%d" %65)

print(chr(ord('A')*3))

#암호화
pw = "a1b2c3"
en_pw = ""
de_pw = ""

for i in pw:
    en_pw+=chr(ord(i) *9)
print("기존 비밀번호 : %s" %pw)
print("암호화된 비밀번호 : {pw}".format(pw=en_pw))


for i in en_pw:
    de_pw += chr(ord(i)//9)
print("복호화된 비밀번호 : {pw}".format(pw=de_pw))