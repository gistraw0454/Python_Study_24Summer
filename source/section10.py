#%% 1 지역번호국번에서 국번을 추출해라
phone= input("전화번호써라: ")
print("국번: "+phone.split("-")[1])    #3칸짜리 배열이된다.

start = phone.index('-') +1
end = phone.index('-',start)    #start부터 시작해서 - 찾기
# end는 보통 포함이안되니 굳이 -1 할필요없다

code = phone[start:end]
print("국번: "+code)

#%% 2 올바른 사업자번호인가?
comp_num = input("사업자 등록 번호\n예) 123-45-23452\n")
#첫번째 - 인덱스 번호가 3일때
c1 = comp_num.find("-")==3
#두번째 - 인덱스 번호가 6일때
c2 = comp_num.find("-",4)==6
#총 길이가 12 일때
c3 = len(comp_num) ==12
#각 번호가 전부 숫자인지 검사
c4 = comp_num.replace("-","").isdecimal()
if c1 and c2 and c3 and c4:
    print("올바른 사업자 등록 번호")
else :
    print("잘못된 사업자 등록 번호")

#%% 3
std='"김철수",85'
name=std.split(",")[0].strip('""')
age = std.split(",")[1]
print("이름은 {} 점수는 {}".format(name,age))
