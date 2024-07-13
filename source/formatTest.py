#%% 포맷스트링
data=10
data2 = "%d" %100
# 결론적으론 data값이 들어가지만, data : %d가 출력된다.
print("data : %d" %data)
print(type(data2)) # 어떠한 서식문자가 들어가도 ""가있으면 str 처리
print(data2)
# %% 포맷 test 2
data1 = 10
data2 = 10.4231 # f면 원래 7자리가 나와야하는데 format의 경우 딱 저장해놓은 값 만큼만 나옴
data3 = 'A' #얘도 문자열임
data4 ="abc"
print("data1 : {}".format(data1))
print("data1 : {}\ndata2 : {}".format(data1,data2))
print("data3 : %s" %data3)
print("data3 : %c" %data3)
print("data4 : %s" %data4)
# 자동 형변환
print("data4 : %c" %65)
# %% 자동 형변환
# // : 몫 연산자
print(10/3)
print(10//3)
# 강제 형변환
print(10//3.0)
print(float(10)//3)
