#%% dict
중국집 = {"짜장면":1500,"짬뽕":2500}
print(len(중국집))
print(중국집["짜장면"]) # value값을 가져오기위한 목적

if "짜장면" in 중국집:
    중국집["짜장면"]=4000
print(중국집)

if "탕수육" not in 중국집:
    중국집["탕수육"] =9000 #추가

print(중국집)

# del 중국집["짬뽕"]
# print(중국집)

for i in 중국집.keys():
    print(i)
for i in range(len(중국집)):
    print(str(i+1)+". "+list(중국집.keys())[i])

total =0
for i in 중국집.values():
    total+=i
avg = total/len(중국집)
print("평균가격: %.2f원" %avg)

#%% dict 2
#등급 입력받고 학점 출력
# 2입력시 B 출력
# 1~5등급, A~F학점

# dict 만들어주면 넣을때 알아서 dict형태로 들어간다
scoreDict={}
# 0 1 2 3 4
# A B C D F
for i in range(5):
    scoreDict[i+1]= chr(i+1+ord('A')) if i==4 else chr(i
                                                       +ord('A'))
print(scoreDict)

rating=int(input("등급: "))
for i in range(5):
    if rating == i+1:
        print(scoreDict[i+1] + "학점입니다\n")
        break