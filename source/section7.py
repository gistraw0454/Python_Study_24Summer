#%% 1 1부터5까지 출력
for i in range(5):
    print(i)
#%% 2 0부터 입력정수까지 수의 총합
sumTo=int(input("양의 정수 : "))
result =0
for i in range(sumTo):
    result +=i+1
print(result)

#%% 3 과일을 리스트에  추가하고 출력
cnt = int(input("몇개의 과일??"))
fruitList=[]
for i in range(cnt):
   fruitList.append(input("%d번째 과일?"%(i+1)))
print(fruitList)

#%% 4 min함수 사용하기
# min(값, 최소값) ; 값은 최소값을 지켜야한다.
exam =[99,78,100,91,81,85,54,100,71,50]
score = [min(n+5,100)for n in exam]
print(score)

#%% 5 369 게임
for n in range(1,100):
    units = n%10
    tens= n//10
    c1 = units%3==0 and units!=0
    c2 = tens%3 ==0 and tens!=0

    if c1 and c2:
        print("짝짝", end="\t")
    elif c1 or c2:
        print("짝",end="\t")
    else:
        print(n,end="\t")
    if n%10==0:
        print()