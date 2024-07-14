#%% °¡°Ý ÀÔ·Â
price = int(input("°¡°Ý : "))

print(price * 0.9)

#%% Á¤¼ö 2°³¸¦ ÀÔ·Â¹Þ°í µ¡¼À, »¬¼À, °ö¼À, ³ª´°¼À
num1 = int(input("Á¤¼ö1 : "))
num2 = int(input("Á¤¼ö2 : "))

addResult = num1+num2
subResult = num1-num2
mulResult = num1*num2
divResult = num1//num2
modResult = num1%num2

print("%d + %d = %d" %(num1,num2,addResult))
print("%d - %d = %d" %(num1,num2,subResult))
print("%d * %d = %d" %(num1,num2,mulResult))
print("%d // %d = %d" %(num1,num2,divResult))
print("%d %% %d = %d" %(num1,num2,modResult))

#%% Á¶°Ç½Ä
isOk = True
isOk = False
print(type(isOk))