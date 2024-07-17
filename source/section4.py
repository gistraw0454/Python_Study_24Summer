#%% 1 두자리정수의 십의자리와 일의자리를 출력
num = int(input("10~99 사이의 정수를 입력하세요"))
print("십의자리: %d, 일의자리: %d" %(num//10,num%10))

#%% 2 초를 입력하면 시분초로 출력
times = int(input("초를 입력하세요"))
hour = times//3600
minute = times%3600 //60
second = times%60

print("%d시간%d분%d초" %(hour,minute,second))

#%% 3 네자리정수의 끝자리로 오전/오후 근무 출력
emp_no = int(input("4자리 사원번호를 입력해라"))
emp_last_no = emp_no%10
print("근무시간은 %s입니다" %('오전'if emp_last_no >=5 else '오후'))

#%% 4 
print("한박스에 라면이 20개 들어가는데, 몇개의 박스가 필요할까요?")
ramen= int(input("라면개수:"))
print(ramen//20 if ramen%20==0 else ramen//20+1)

#%% 5 합격 불합격 출력
kor=int(input("국어점수: "))
eng=int(input("영어점수: "))
math=int(input("수학점수: "))

total = kor+eng+math
avg = total/3

print( '합격' if avg >=80 else '불합격')