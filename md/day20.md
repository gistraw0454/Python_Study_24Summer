# 20강 - list와 tuple,dict
- mutable (변할수있는) : list
- immutable (변할수없는) : tuple
```py
#%% mutable
dataList1=[1,2,3]
dataList2=dataList1

dataList2.append(4)
print(dataList1)
# dataList2를 바꿨는데 dataList1에도 영향o

#%% immutable
dataTuple1 = (1,2,3)
# print(type(dataTuple1))
dataTuple2 = dataTuple1
dataTuple2 +=4,5

print(dataTuple1)
#dataTuple2를 바꿨는데 dataTuple1에 영향x
#있는데이터를 가져오는 목적, 검색 목적, 변경x
# dataTuple1[0]=10 튜플의 값은 변경 할 수 없다.
```
## Dict
- 한쌍으로 저장되어 관리
- len()을 사용하면 한쌍을 1로 카운트
- 키값은 중복될수 없으며, 값은 중복이 가능하다
- 키 값을 주면 그 키의 짝꿍 값을 가지고 온다

###  DIct 선언
```
dict 명 = {키:값,키:값,...}
```
### Dict 사용
- 추가 (키값이 없을 때)
    - `dict명[키] =값`
- 수정 (키값이 있을 때)
    - `dict명[키] =깂`
- 삭제 (한쌍이 삭제된다)
    - `del dict명[키]`
- 검색
    - `키 in dict명` : 키 값이 있으면 참
    - `키 not in dict명` : 키 값이 없으면 참

### KEY 분리
- list(dict명.keys())
### VALUE 분리
- dict명.values()