#%% 1 음료수를 최대한 사보자 
def vending_machine(money):
    price =700
    change =0
    count = money //700
    for i in range(count):
        change = money - (i+1)*price
        print("음료수는 {}개, 잔돈은 {}원".format(i+1,change))

vending_machine(3000)

#%% 2 점수 평균 구하기
def get_avg(marks):
    total=0
    average=0.0
    for i in list(marks.values()):
        total +=i
    average=total/len(marks)
    return average

    
marks = {'국어':90,'영어':80,'수학':85} 
print("평균: %.2f" %get_avg(marks))

#%% 3 축의금 명단과 전체 축의금 출력
total =0
wedding ={}
def gift(dic,who,money):
    global total
    total+=money
    dic[who]=money

gift(wedding,'영희',5)
gift(wedding,'철수',3)
gift(wedding,'영숙',10)

print("축의금 명단: {}".format(wedding))
print("전체 축의금: {}".format(total))