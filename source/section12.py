#%% 1 �ζǹ�ȣ ��÷
import random
import time

pot = [n for n in range(1,46)]
jackpot=[]
for n in range(1,7):
    random.shuffle(pot)
    jackpot.append(pot.pop())
    # time.sleep(2) # 2�ʿ� �ѹ��� ���� �ϳ� ������ �ϰڴ�

jackpot.sort()
print("�̹� ��÷ ��ȣ�� {}�Դϴ�".format(jackpot))

#%% 2 1~100
import random as r
import time
answer=r.randint(1,100)

print("updown ������ �����մϴ�")
start =time.time() # ����ð�
while(True):
    n= int(input("���?"))
    if (answer==n):
        print("����")
        break
    elif (answer<n):
        print("down")
    else:
        print("up")

end = time.time()

print("�ɸ��ð�: {}".format(end-start))