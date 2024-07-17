#%% 1 퀴즈 재귀와 예외처리
class Quiz:
    answer =['경기도','강원도','충청남도','충청북도','전라남도','전라북도','경상남도','경상북도','제주특별자치도']

    @classmethod
    def challenge(cls):
        #해당 list가 비어있을때
        if not cls.answer:
            print("다 맞췄다. 성공 !!")
            return
        do = input ("정답은?")
        if do not in cls.answer:
            raise Exception("틀렸다")
        
        # pop(i) 으로 해당 인덱스부분을 없애기
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do:
                print("정답이다")
                cls.answer.pop(i)
                cls.challenge()
try:
    print("우리나라 9개 도를 맞히는 게임이다. 하나씩 입력하라")
    Quiz.challenge()
except Exception as e:
    print(e)

#%% 2 up down game
import random

class UpDown:
    def __init__(self):
        self.answer=random.randint(1,100)
        self.count=0
    def challenge(self):
        self.count+=1
        n=int(input('입력(1~100)'))
        if n<1 or n>100:
            raise Exception("1~100 사이만 입력해라")
        return n 

    def play(self):
        while True:
            try:
                n= self.challenge()
            except Exception as e:
                print(e)
            #예외처리가 발생하지 않는다면
            else:
                if self.answer <n :
                    print("down")
                elif self.answer > n : 
                    print("up")
                else :
                    print("%d만의 정답" %self.count)
                    break

game = UpDown()
game.play()
#%% 3 은행 예외처리
# 예외처리 BankError 만들기
class BankError(Exception):
    # 해당 에러가만들어지면 Exception에서도 초기화 시켜준다
    def __init__(self,message):
        super().__init__(message)
#BankAccount class만들기
class BankAccount:
    # 해당 클래스 만들어지면, acc번호, 밸런스를 초기화시켜준다.
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
    # 넣는 돈이 0보다 적으면 입금 불가라는 예외처리를 발생시킨다.
    def deposit(self,money):
        if money <=0:
            raise BankError ("%d원 입금불가" %money)
        # 아니면 돈추가
        self.balance +=money

    # 인출하기 
    def withdraw(self, money):
        # 출금금액이 0보다 적으면 출금 불가라는 예외처리를 발생시킨다.
        if money<=0:
            raise BankError("%d원 출금불가" %money)
        # 출금금액이 현재 잔고보다 많으면 잔액부족이라는 예외처리를 발생시킨다.
        if money > self.balance:
            raise BankError("잔액부족")
        # 아니면 출금하고 출금금액 리턴
        self.balance -=money
        return money
    # 전달하기
    def trasfer(self,your_acc,money):
        # your_acc에 출금한 돈을 입금한다.
        your_acc.deposit(self.withdraw(money))
    # 잔고정보 출력
    def inquiry(self):
        print("계좌번호 : %s" %self.acc_no)
        print("통장잔액 : %s" %self.balance)
me = BankAccount("1234",50000)
you = BankAccount("1111",50000)

try :
    # me.deposit(-1000)
    # me.withdraw(-1000)
    # me.withdraw(100000)
    me.trasfer(you,5000)
except BankError as e:
    print(e)
finally :
    me.inquiry()
    you.inquiry()