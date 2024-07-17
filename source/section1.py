#%% 1 학생정보출력
student="31025"
# 3 10 25
# 0 12 34
grade = student[0]
classNum= student[1:3]
stdNum=student[3:]

print(grade + "학년" + classNum +"반"+ stdNum +"번")

#%% 2 차량번호 출력
car1 = "서울2가1234"
car2 = "10가1234"
car3 = "288가1234"

c1Num = car1[-4:]
c2Num = car2[-4:]
c3Num = car3[-4:]

print(car1+"의 차량번호: "+c1Num)
print(car2+"의 차량번호: "+c2Num)
print(car3+"의 차량번호: "+c3Num)

#%% 3 문자열의 가운데에 있는 문자 출력
strData = "maple"
print(strData[len(strData)//2])

#%% 4 리스트 3~7 추출하고 그중에 2번째꺼 추출
dataList = [0] *10

for i in range(10):
    dataList[i] = (i+1)*10

print(dataList)

result = dataList[2:7]
print("3번째부터 7번째까지 : "+str(result))
print("그중에서 2번째 요소 : "+str(result[1]))

#%% 5 딕셔너리로 요일별 메뉴 출력하기
menu = {'금':'탕수육','토':'유산슬','일':'팔보채'}
print("금요일 : "+menu["금"])
print("토요일 : "+menu["토"])
print("일요일 : "+menu["일"])
