#%% ���� ����ȯ
print("%d" %65)

print(chr(ord('A')*3))

#��ȣȭ
pw = "a1b2c3"
en_pw = ""
de_pw = ""

for i in pw:
    en_pw+=chr(ord(i) *9)
print("���� ��й�ȣ : %s" %pw)
print("��ȣȭ�� ��й�ȣ : {pw}".format(pw=en_pw))


for i in en_pw:
    de_pw += chr(ord(i)//9)
print("��ȣȭ�� ��й�ȣ : {pw}".format(pw=de_pw))