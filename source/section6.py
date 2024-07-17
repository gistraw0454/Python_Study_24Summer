#%% 1 입력한만큼 hello 반복
count = int(input("정수: "))
if count<=0:
    print("다시")
else:
    n=0
    while(n!=count):
        print("%d번째 Hello" %(n+1))
        n+=1
# %% 2 1부터 100까지 7의 배수
n=0
while(n<98):
    n+=7
    print(n)

#%% 3 주어진돈으로 얼마나 커피를 뽑을 수 있을까?
coffee = 0
money = int(input("돈넣어"))
while money>=300:
    coffee+=1
    money-=300
    print('커피{}잔 잔돈{}원'.format(coffee,money))

#%% 4 입력된값들 출력 (중복없이)
numSet = set()
num=0
while len(numSet)<5:
    num= int(input("0~9사이의 정수: "))
    numSet.add(num)
print("모두 입력됐다")
print("입력된 값은 {}".format(numSet))

#%% 5 10의배수면 \n 아니면 \t출력
n=1
while(n<=100):
    if n%10==0:
        print(n)
    else:
        print(n,end="\t")
    n+=1

#%% 6 구구단
n=1
dan =2
while n<=9:
    dan=2
    while dan<=9:
        print("%d*%d=%d" %(dan,n,dan*n),end="\t")
        dan+=1
    print()
    n+=1