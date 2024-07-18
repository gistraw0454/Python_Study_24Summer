#%% dict test
numDict = {"even":[2,4,6],"odd":[1,3,5]}
for i in numDict["even"]:
    print(i)

numListDict = {"1학년":[[30,40,50],[80,90,100]]}
for i in numListDict["1학년"]:
    for j in i:
        print(j)
    print("============")

#%% dict task 학생관리
#학생 이름과 학생점수를 받고 추가,수정,삭제,목록
title = "학생 성적 관리 프로그램\n"
msg = "1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n"
errMsg = "다시 시도해주세요"

studentDict = {}
subjectList = ["국어", "영어", "수학"]

while True:
    try:
        choice = int(input(title + msg))
    except ValueError:
        print(errMsg)
        continue

    if choice == 1:
        name = input("학생 이름: ")
        if name not in studentDict:
            scores = input("다음과 같이 각 점수를 입력하세요\n국어, 영어, 수학: ").split(",")
            if len(scores) == 3:
                studentDict[name] = list(map(int, scores))
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.")
        else:
            print("이미 등록된 학생입니다.")
    elif choice == 2:
        sub_choice = int(input("1.학생명 수정\n2.점수 수정\n"))
        name = input("수정할 학생명: ")
        if sub_choice == 1:
            if name in studentDict:
                new_name = input("새로운 학생명: ")
                studentDict[new_name] = studentDict.pop(name)
            else:
                print("존재하지 않는 학생입니다.")
        elif sub_choice == 2:
            if name in studentDict:
                sub_choice = int(input("1.국어 점수\n2.영어 점수\n3.수학 점수\n"))
                if 1 <= sub_choice <= 3:
                    new_score = int(input("새로운 점수: "))
                    studentDict[name][sub_choice - 1] = new_score
                else:
                    print("잘못된 선택입니다.")
            else:
                print("존재하지 않는 학생입니다.")
    elif choice == 3:
        name = input("삭제할 학생명: ")
        if name in studentDict:
            del studentDict[name]
        else:
            print("존재하지 않는 학생입니다.")
    elif choice == 4:
        for name, scores in studentDict.items():
            print(f"{name}:")
            for idx, score in enumerate(scores):
                print(f"  {subjectList[idx]}: {score}")
    elif choice == 5:
        break
    else:
        print(errMsg)
