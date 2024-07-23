#%% 대화창 실습 : 날짜 및 시간 변경
import datetime 
start_time = datetime.datetime.now()
start_time.replace(month=12,day=25)

#%% 대화창 실습 : from import 를 이용해 날짜 및 시간 변경
from datetime import datetime 
start_time = datetime.now()
start_time.replace(month=12,day=25)

#%% code 7-1 ) 크리스마스까지 남은 시간 구하기
import datetime as dt

today = dt.date.today()
print("오늘은 {}월 {}일".format(today.year,today.month,today.day))

xMas = dt.datetime(2024,12,25)
time_gap = xMas - dt.datetime.now()

print("{}일 {}시간 남음".format(time_gap.days,time_gap.seconds//3600))

#%% code 7-2 ) 100일 후, 100일 전 날짜 구하기
import datetime as dt
print("오늘=",dt.datetime.now())

hundred = dt.timedelta(days=100)
plus100day = dt.datetime.now() + hundred
print(plus100day)

#%% code 7-26 )
from tkinter import *

window = Tk()
label = Label(window, text= "헬로 파이썬")
label.pack()

window.mainloop()

#%% code 7-27 ) 버튼과 이벤트 처리 실습
from tkinter import *
def change_label():
    if label.cget("text")=="헬로파이썬":
        label.config(text='안녕파이썬')
        label.config(bg='cyan')
    else :
        label.config(text='헬로파이썬')
        label.config(bg='yellow')

window = Tk()
label = Label(window,text='헬로파이썬',bg='yellow')
label.pack()
btn = Button (window,text='클릭하면 문자가 변경됨',fg='blue',command= change_label)
btn.pack()

window.mainloop()
#%% lab 7-10 ) 엔트리 객체활용
def entry_to_label():
    str= input_entry.get()
    label.config(text=str)
from tkinter import *

window = Tk()
input_entry = Entry(window,width=50)
input_entry.pack()

button = Button(window,text='처리')
button.pack()

label = Label(window,text='')
label.pack()

window.mainloop()

#%% code 7-29 ) 체질량지수 계산기
from tkinter import *

def bmi_compute():
    w=float(weight.get())
    h=float(height.get())/100.0
    bmi=w/(h*h)
    answer= '당신의 bmi는 {:4.2f}'.format(bmi)
    result.config(text=answer)

window=Tk()
label = Label(window,text="체중 키 써라")
label.pack()

weight=Entry(window,width=50)
weight.pack()

height=Entry(window,width=50)
height.pack()

button = Button(window,text="bmi 계산",command=bmi_compute)
button.pack()

result = Label(window,text="당신의 bmi는")
result.pack()

window.mainloop()
# %% code 7-31 ) 계산기 만들기
from tkinter import *
window=Tk()
window.title("계산기")
window.geometry('350x200')

Label(window,text="숫자 1").grid(column=0,row=0)
Label(window,text="숫자 2").grid(column=0,row=1)
res_label = Label(window,text="결과 :")
res_label.grid(column=0,row=2)

num1 = Entry(window,width=10)
num2 = Entry(window,width=10)
num1.grid(column=1,row=0)
num2.grid(column=1,row=1)

def add():
    res_text="결과 ="+str(float(num1.get())+float(num2.get()))
    res_label.configure(text=res_text)

def substract():
    res_text="결과 ="+str(float(num1.get())-float(num2.get()))
    res_label.configure(text=res_text)

def multiple():
    res_text="결과 ="+str(float(num1.get())*float(num2.get()))
    res_label.configure(text=res_text)

def division():
    res_text="결과 ="+str(float(num1.get())/float(num2.get()))
    res_label.configure(text=res_text)

btn_plus = Button(window,text="+",command=add)
btn_minus = Button(window,text="-",command=substract)
btn_mult = Button(window,text="*",command=multiple)
btn_div = Button(window,text="/",command=division)

btn_plus.grid(column=2,row=1)
btn_minus.grid(column=3,row=1)
btn_mult.grid(column=4,row=1)
btn_div.grid(column=5,row=1)

window.mainloop()
# %%
