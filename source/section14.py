#%% 1 파일 복사하기
fileName =""
while True :
    fileName = input("복사할 파일명을 입력해라")
    #file.txt 면, txt 를 뽑아옴.
    extName = fileName[fileName.rfind('.')+1:]
    if extName != "txt":
        print("복사할 수 없는 파일")
    else:
        break

# with 문이끝나면 자동으로 close를 해준다.
# source는 객체명
with open(fileName,'rt',encoding="euc-kr") as source: # utf-8로 해봤는데 안되길래 이걸로함
    with open("복사본-"+fileName,'wt') as copy:
        while True:
            #source라는 파일에서 한글자씩 가져온다
            buffer=source.read(1)
            if not buffer:
                break
            copy.write(buffer)
print("복사본-"+fileName+"파일이 생성됨")
# %% 2 csv 파일로 cctv수 구하기
import csv
with open('cctv.csv','r') as csvfile:
    # csvfile에 넣을건데, `,`로 구분하겠다. 각각의 문자열을 ""로 묶겠다
    buffer = csv.reader(csvfile,delimiter=",",quotechar='"')
    total =0
    for i,line in enumerate(buffer):
        if i!=0:
            total +=int(line[4])
print('CCTV 총 {}대입니다.'.format(total))

#%% 3 json 파일에서 읽어오기
import json
with open('cctv.json','r',encoding='utf-8') as jsonfile:
    buffer = jsonfile.read()
    cctv_list=json.loads(buffer)
    cctv_purpose=set()
    for place in cctv_list:
        cctv_purpose.add(place['설치목적구분'])

print(cctv_purpose)