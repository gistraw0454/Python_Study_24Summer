#%% code 8-16 ) 사용자로부터 입력받은 다섯개 정수를 저장하는 프로그램
f=open('data5.txt','w')
for _ in range(5):
    n = input("정수를 입력하시오")
    f.write(n)
    f.write("\n")
f.close()

#%% code 8-17 ) 파일로부터 정수를 입력받아 합과 평균을 계산
f=open('data5.txt','r')
su =0
for _ in range(5):
    n = int(f.readline())
    su+=n
print("합={} 평균={}".format(su,su/5))
f.close()
