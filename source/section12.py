#%% 1 로또번호 추첨
import random
import time

pot = [n for n in range(1,46)]
jackpot=[]
for n in range(1,7):
    random.shuffle(pot)
    jackpot.append(pot.pop())
    # time.sleep(2) # 2초에 한번씩 숫자 하나 나오게 하겠다

jackpot.sort()
print("이번 당첨 번호는 {}입니다".format(jackpot))

#%% 2 1~100
import random as r
import time
answer=r.randint(1,100)

print("updown 게임을 시작합니다")
start =time.time() # 현재시간
while(True):
    n= int(input("어떤값?"))
    if (answer==n):
        print("정답")
        break
    elif (answer<n):
        print("down")
    else:
        print("up")

end = time.time()

print("걸린시간: {}".format(end-start))