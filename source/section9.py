#%% 1 
#enumerate로 리스트의 인덱스와 값을 함께 가져온다.
rainbow = ['red','orange','yellow','blue','navy','purple']
for idx,value in enumerate(rainbow):
    print("무지개의 {}번째 색은 {}입니다".format(idx+1,value))


#%% 2
exam=[]
print("점수입력해라")
print("더이상 입력할 점수가 없으면 음수를 써라")
while(True):
    score =int(input("점수 입력"))
    if score <0:
        break
    exam.append(score)
avg = sum(exam)/len(exam)
max1 = max(exam)
min1 = min(exam)

print("평균: %.2f, 최대: %d, 최소: %d" %(avg,max1,min1))