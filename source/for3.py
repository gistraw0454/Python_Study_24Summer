#%% ��Ÿ���
# 1~4 ���
for i in range(10):
    print(i+1)
    if i==3 :
        break
    

print("\n")
# 1~10 �� 4�� �����ϰ� ���
for i in range(10):
    if i==3:
        continue
    print(i+1)

#%% ��Ÿ��� �ǽ�
for i in range(100):
    if i>70 :break
    print(i,end=" ")
print("\n")
for i in range(100):
    if ((i+1)%3==0 and (i+1)%5==0):
        print(i+1,end=" ")

