# 18강 - 컬렉션 - list2
### list 사용
dataList=[1,2,3]
- 값 넣기 
    - 추가 `dataList.append(4)`
        - [1,2,3,4]
    - 삽입 `dataList.insert(인덱스번호,값) `
        - dataList.insert(1,1.5)
        - [1,1.5,2,3]
- 값 삭제
    - `dataList.remove(값)`
        - [1,2,3,4].remove(1)
        - [2,3,4] : 해당값 삭제
        - 중복시 좌에서 우 방향으로 가장 먼저 만난 값의 인덱스를 가져온다.

    - `del dataList[인덱스번호]`
        - del dataList[1]
        -[1,3] : 해당 인덱스 값 삭제

    - `dataList.clear()`
        - 모든 값 삭제
- 값 검색
    - `dataList.index(값)`
        - dataList.index(3)
        - 2 : 해당값의 인덱스 값을 리턴
        - 중복시 좌에서 우 방향으로 가장 먼저 만난 값의 인덱스를 가져온다.
- 값 수정
    - `dataList[인덱스번호] = 새로운값`
    - dataList[0]=10
    - [10,2,3]

### for 문 사용
- 0, ?, 1 로 사용가능
```
for i in range(len(list명)):
    list명[i]
```
- 빠른 for문 (향상된 for문, forEach 문)
    ```
    for i in list명:
        i 
    ```
    - list에있는 각각의 요소가 i에 담긴다

### 값의 유무 확인
- 값 in list명 : 조건식(참 또는 거짓의 값) list안에 값이 있으면 True
- 값 not in list명 : list안에 값이 없으면 True
