#%% 1 만원을 모두사용해라
money=10000
while True:
    print("현재 {}원이 있다.".format(money))
    if money==0:
        break
    spend= int(input("사용할 금액 입력: "))
    if spend <=0:
        print("0이하의 금액은 사용할 수 없다")
    elif spend > money:
        print("{}이 부족하다".format(spend-money))
    else:
        money-=spend

#%% 2 평점 출력
while True:
    star = int(input("이번 영화의 평점을 입력하라"))
    if star >=1 and star <=5:
        print("평점: {}".format('*'*star))
        break   
    else:
        print("1~5까지만 입력")
    
#%% 3 저장된 비밀번호 맞추기
key = 'qwerty'
count = 0
while Ture:
    if count ==5:
        print("입력횟수 초과")
        break
    pw = input("비밀번호: ")
    if pw==key:
        print("비밀번호 맞춤")
        break
    count +=1

#%% 4 홀수 단만 해당 단수만큼 곱셈연산하기
for dan in range(2,10):
    if dan%2==0:
        print()
        continue
    for i in range(1,dan+1):
        print("{}*{}={}".format(dan,i,dan*i))