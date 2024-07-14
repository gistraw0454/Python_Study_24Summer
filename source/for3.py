#%% 기타제어문
# 1~4 출력
for i in range(10):
    print(i+1)
    if i==3 :
        break
    

print("\n")
# 1~10 중 4를 제외하고 출력
for i in range(10):
    if i==3:
        continue
    print(i+1)

#%% 기타제어문 실습
for i in range(100):
    if i>70 :break
    print(i,end=" ")
print("\n")
for i in range(100):
    if ((i+1)%3==0 and (i+1)%5==0):
        print(i+1,end=" ")

