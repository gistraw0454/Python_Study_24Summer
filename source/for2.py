#%% for task2
for i in range(0,26,1):
    print(chr(ord('A')+i),end=" ")
print("\n")

for i in range(0,25,1):
    if (i>1) :
        i+=1
    print(chr(ord('A')+i),end=" ")
#i���� �ȿ��� �ٲ㵵 �ٽ� ���� �ö󰡸� range���� i�� �����Ŷ� ����
print("\n")

for i in range(0,26,1):
    if (i%2==0) :
        print(chr(ord('a')+i),end="")
    else :
        print(chr(ord('A')+i),end="")
print("\n")