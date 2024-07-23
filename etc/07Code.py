#%% ��ȭâ �ǽ� : ��¥ �� �ð� ����
import datetime 
start_time = datetime.datetime.now()
start_time.replace(month=12,day=25)

#%% ��ȭâ �ǽ� : from import �� �̿��� ��¥ �� �ð� ����
from datetime import datetime 
start_time = datetime.now()
start_time.replace(month=12,day=25)

#%% code 7-1 ) ũ������������ ���� �ð� ���ϱ�
import datetime as dt

today = dt.date.today()
print("������ {}�� {}��".format(today.year,today.month,today.day))

xMas = dt.datetime(2024,12,25)
time_gap = xMas - dt.datetime.now()

print("{}�� {}�ð� ����".format(time_gap.days,time_gap.seconds//3600))

#%% code 7-2 ) 100�� ��, 100�� �� ��¥ ���ϱ�
import datetime as dt
print("����=",dt.datetime.now())

hundred = dt.timedelta(days=100)
plus100day = dt.datetime.now() + hundred
print(plus100day)

#%% code 7-26 )
from tkinter import *

window = Tk()
label = Label(window, text= "��� ���̽�")
label.pack()

window.mainloop()

#%% code 7-27 ) ��ư�� �̺�Ʈ ó�� �ǽ�
from tkinter import *
def change_label():
    if label.cget("text")=="������̽�":
        label.config(text='�ȳ����̽�')
        label.config(bg='cyan')
    else :
        label.config(text='������̽�')
        label.config(bg='yellow')

window = Tk()
label = Label(window,text='������̽�',bg='yellow')
label.pack()
btn = Button (window,text='Ŭ���ϸ� ���ڰ� �����',fg='blue',command= change_label)
btn.pack()

window.mainloop()
#%% lab 7-10 ) ��Ʈ�� ��üȰ��
def entry_to_label():
    str= input_entry.get()
    label.config(text=str)
from tkinter import *

window = Tk()
input_entry = Entry(window,width=50)
input_entry.pack()

button = Button(window,text='ó��')
button.pack()

label = Label(window,text='')
label.pack()

window.mainloop()

#%% code 7-29 ) ü�������� ����
from tkinter import *

def bmi_compute():
    w=float(weight.get())
    h=float(height.get())/100.0
    bmi=w/(h*h)
    answer= '����� bmi�� {:4.2f}'.format(bmi)
    result.config(text=answer)

window=Tk()
label = Label(window,text="ü�� Ű ���")
label.pack()

weight=Entry(window,width=50)
weight.pack()

height=Entry(window,width=50)
height.pack()

button = Button(window,text="bmi ���",command=bmi_compute)
button.pack()

result = Label(window,text="����� bmi��")
result.pack()

window.mainloop()
# %% code 7-31 ) ���� �����
from tkinter import *
window=Tk()
window.title("����")
window.geometry('350x200')

Label(window,text="���� 1").grid(column=0,row=0)
Label(window,text="���� 2").grid(column=0,row=1)
res_label = Label(window,text="��� :")
res_label.grid(column=0,row=2)

num1 = Entry(window,width=10)
num2 = Entry(window,width=10)
num1.grid(column=1,row=0)
num2.grid(column=1,row=1)

def add():
    res_text="��� ="+str(float(num1.get())+float(num2.get()))
    res_label.configure(text=res_text)

def substract():
    res_text="��� ="+str(float(num1.get())-float(num2.get()))
    res_label.configure(text=res_text)

def multiple():
    res_text="��� ="+str(float(num1.get())*float(num2.get()))
    res_label.configure(text=res_text)

def division():
    res_text="��� ="+str(float(num1.get())/float(num2.get()))
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
