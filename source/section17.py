#%% 1 ���� ��Ϳ� ����ó��
class Quiz:
    answer =['��⵵','������','��û����','��û�ϵ�','���󳲵�','����ϵ�','��󳲵�','���ϵ�','����Ư����ġ��']

    @classmethod
    def challenge(cls):
        #�ش� list�� ���������
        if not cls.answer:
            print("�� �����. ���� !!")
            return
        do = input ("������?")
        if do not in cls.answer:
            raise Exception("Ʋ�ȴ�")
        
        # pop(i) ���� �ش� �ε����κ��� ���ֱ�
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do:
                print("�����̴�")
                cls.answer.pop(i)
                cls.challenge()
try:
    print("�츮���� 9�� ���� ������ �����̴�. �ϳ��� �Է��϶�")
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
        n=int(input('�Է�(1~100)'))
        if n<1 or n>100:
            raise Exception("1~100 ���̸� �Է��ض�")
        return n 

    def play(self):
        while True:
            try:
                n= self.challenge()
            except Exception as e:
                print(e)
            #����ó���� �߻����� �ʴ´ٸ�
            else:
                if self.answer <n :
                    print("down")
                elif self.answer > n : 
                    print("up")
                else :
                    print("%d���� ����" %self.count)
                    break

game = UpDown()
game.play()
#%% 3 ���� ����ó��
# ����ó�� BankError �����
class BankError(Exception):
    # �ش� ��������������� Exception������ �ʱ�ȭ �����ش�
    def __init__(self,message):
        super().__init__(message)
#BankAccount class�����
class BankAccount:
    # �ش� Ŭ���� ���������, acc��ȣ, �뷱���� �ʱ�ȭ�����ش�.
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
    # �ִ� ���� 0���� ������ �Ա� �Ұ���� ����ó���� �߻���Ų��.
    def deposit(self,money):
        if money <=0:
            raise BankError ("%d�� �ԱݺҰ�" %money)
        # �ƴϸ� ���߰�
        self.balance +=money

    # �����ϱ� 
    def withdraw(self, money):
        # ��ݱݾ��� 0���� ������ ��� �Ұ���� ����ó���� �߻���Ų��.
        if money<=0:
            raise BankError("%d�� ��ݺҰ�" %money)
        # ��ݱݾ��� ���� �ܰ��� ������ �ܾ׺����̶�� ����ó���� �߻���Ų��.
        if money > self.balance:
            raise BankError("�ܾ׺���")
        # �ƴϸ� ����ϰ� ��ݱݾ� ����
        self.balance -=money
        return money
    # �����ϱ�
    def trasfer(self,your_acc,money):
        # your_acc�� ����� ���� �Ա��Ѵ�.
        your_acc.deposit(self.withdraw(money))
    # �ܰ����� ���
    def inquiry(self):
        print("���¹�ȣ : %s" %self.acc_no)
        print("�����ܾ� : %s" %self.balance)
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