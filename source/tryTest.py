#%% 28 Exception test
try:
    int(input("정수입력 :"))
except Exception as e:
    print("정수만 입력하시오")
print("반드시 실행되어야할 문장")


try:
    print(10/0)
except ZeroDivisionError as e:
    # print(e.__str__)
    print("0으로 나눌수 없다.")