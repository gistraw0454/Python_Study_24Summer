#%% 1 메모장에 쓰기
nation=['그리스','아테네','독일','베를린','러시아','모스크바','미국','워싱턴']

file=open('nation.txt',"wt")    #t- 문자 b-바이너리

for idx,country in enumerate(nation):
    if idx %2 ==0:
        file.write(nation[idx]+"-"+nation[idx+1]+"\n")
file.close()

#%% 2
old_file = open("연락처.txt","rt")
buffer = old_file.read()
n=buffer.count("011-")
buffer.replace("011-","010-")
print("총 {}건의 011 데이터를 찾았습니다.".format(n))
old_file.close()

new_file = open("연락처.txt","wt")
new_file.write(buffer)
new_file.close()
print("데이터 수정완료")
