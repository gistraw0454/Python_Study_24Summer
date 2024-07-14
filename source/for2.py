#%% for task2
for i in range(0,26,1):
    print(chr(ord('A')+i),end=" ")
print("\n")

for i in range(0,25,1):
    if (i>1) :
        i+=1
    print(chr(ord('A')+i),end=" ")
#i값을 안에서 바꿔도 다시 위로 올라가면 range값을 i에 담을거라 ㄱㅊ
print("\n")

for i in range(0,26,1):
    if (i%2==0) :
        print(chr(ord('a')+i),end="")
    else :
        print(chr(ord('A')+i),end="")
print("\n")