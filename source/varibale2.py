#%% (1) test1
name = "한동석"
age =10
height = 120.888
hobby = "피아노"

print("이름: ",name)
print("나이: ",age,end='살\n')
print("키: ",height,end='cm\n')
print("취미: ",hobby)
# %% (2) test
name = "한동석"
age =10
height = 120.888
hobby = "피아노"
print("이름: %s" %name)
print("나이: %d살"%age)
print("키: %.3fcm"%height)
print("취미: %s"%hobby)
