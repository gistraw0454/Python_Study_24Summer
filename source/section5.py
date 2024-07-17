#%% 1 점수에 대한 학점 부여
score = int(input("정수: "))
grade =''
if score >=90:
    grade ='A'
elif score >=80:
    grade ='B'   
elif score >=70:
    grade ='C'  
elif score >=60:
    grade ='D'   
else:
    grade = 'F'

print(grade)

#%% 2 임의의 점수를 입력받고 3의 배수인지 판단
num =int (input("정수: "))
msg=""
if num%3 ==0:
    msg = "%d는 3의 배수입니다." %num
else:
    msg = "%d는 3의 배수아닙니다." %num

print(msg)

#%% 3 세 정수중 가장 큰 수 
n1 =int (input("정수1: "))
n2 =int (input("정수2: "))
n3 =int (input("정수3: "))

if n1>=n2 and n1>=3:
    msg = "%d가 가장 큰수" %n1
elif n2>=n1 and n2>=n3:
    msg = "%d가 가장 큰수" %n2
else :
    msg = "%d가 가장 큰수" %n3
print(msg)

#%% 4 차량번호가 짝수면 운행가능, 홀수면 운행불가능
car_no = input("차량번호 :")
if int(car_no[-1])%2==0:
    print("%s는 오늘 운행가능" %car_no)
else:
    print("%s는 오늘 운행 불가능" %car_no)