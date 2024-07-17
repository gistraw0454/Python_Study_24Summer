# Python_Study_24Summer

- �ڷᱸ�� ������ ������������ ������.
- �ճ����� ���� �� �ʿ���µ�, ���� �������� ���� �ȱ���. >�ſ� ���� �ʱ��� ����.

## ����

#### 1�� ���̽� ��ġ �� �����ϱ�
#### 2�� ���������� ��� ����� �⺻ ����
#### 3�� ������ ����� �ڷ���
#### 4�� ����Լ��� ������ ���
#### 5�� format()�� ����ȯ
#### 6�� ��ȣȭ�� ��ȣȭ, �Է��Լ�
#### 7�� ������1 - �켱������ ���ռ�
#### 8�� ������2 - ���ǽİ� ��Ʈ����
#### 9�� ������3 - ��Ʈ������ Ȱ��
#### 10�� ������4 - ���� ������
#### 11�� ���׿������� ����� if��
#### 12�� if�� ���� �� �ǽ�, ���� ������
#### 13�� for�� ����1
#### 14�� for�� ����2
#### 15�� ��Ÿ ���
#### 16�� while��
#### 17�� �÷��� - list1
#### 18�� �÷��� - list2
#### 19�� �÷��� -list �ǽ�
#### 20�� list�� tuple, dict
#### 21�� dict�� list �̴� ������Ʈ - �л� ���� ���α׷�
#### 22�� �Լ��� �޼ҵ� �̷�
#### 23�� �Լ� ���� ����
#### 24�� �Լ� ��ȭ ����
#### 25�� Ŭ���� �̷�
#### 26�� Ŭ���� ����
#### 27�� ���
#### 28�� ��� ����, ���� ó��
#### 29�� ����� ���� ó��, ���� �����
#### 30�� ���� ���� : ����1~����5
#### 31�� ���� ���� : ����6~����9
#### 32�� ���� ���� : ����10~����12
#### 33�� ���� ���� : ����13~����15
#### 34�� ���� ���� : ����16~����17
#### 35�� ���� ���� : ����18~����20

## �ʱ�
- Ctrl + alt ����Ű + ���� �ϸ� ���縦 ������ ����
- Python�� ���ǹ��� if����
    - switch case���� ���� !! ���..
- ���׿����� ���
    - `��1 if A>B else ��2
    - C������.. A>B ? �� : ��2
## ��ɾ�
- `ord` : ���� -> ����
- `chr` : ���� -> ����
- int() 
- "~{}~".format(a)
    - "~{here}~".format(here=a)
```py
#%% "ABC"���� B�� Z�� ����
# ���ڿ��� ����� ���Ҽ�����
strList = "ABC"
strList.replace("B","Z")
strList = strList.replace("B","Z")
print(strList)
```
```py
#%% �ڿ����� �ѱ۷� ����
# �Է� ��) 1024
# ��� ��) �ϰ��̻�
han = "�����̻�����ĥ�ȱ�"
num = int(input())
result = ""

while num != 0:
    result = han[num%10] + result
    num //=10

print(result)
```

## DICT
```py
dataDict = {}
�̷��� �����ؼ� 
dataDict[0]="A"�̷������� ������
dataDict= {0:'A'} ���ǰ�,
dataDict[0]�ϸ�, 'A'�� ��ȸ�ȴ�. //idex������ �ƴ϶� key �� ��ȸ�ϴ°���.
```

> list dict �κ��� �ѹ� �� ����.

- �Լ������� `global ��������` �̷��� ���ְ� �ش� ������������ ������ָ� �Լ������� global ������ ����� �� �ִ�.

���̽� : ��ü���� (class)


## set : ����, �ߺ��� ���Ҹ� ���� �� ����.
- ���� ���� �˻簡 �����̴�.

## min(��, �ּҰ�) ; ���� �ּҰ��� ���Ѿ��Ѵ�.
```py
exam =[99,78,100,91,81,85,54,100,71,50]
score = [min(n+5,100)for n in exam]
print(score)
```

 
## enumerate�� ����Ʈ�� �ε����� ���� �Բ� �����´�.
```py
rainbow = ['red','orange','yellow','blue','navy','purple']
for idx,value in enumerate(rainbow):
    print("�������� {}��° ���� {}�Դϴ�".format(idx+1,value))
```

## �ε�����ȣ ���� ���� ����ϴ� ���
```py
#%% 1 ������ȣ�������� ������ �����ض�
phone= input("��ȭ��ȣ���: ")
print("����: "+phone.split("-")[1])    #3ĭ¥�� �迭�̵ȴ�.

start = phone.index('-') +1
end = phone.index('-',start)    #start���� �����ؼ� - ã��
# end�� ���� �����̾ȵǴ� ���� -1 ���ʿ����

code = phone[start:end]
print("����: "+code)

#%% 2
comp_num = input("����� ��� ��ȣ\n��) 123-45-23452\n")
#ù��° - �ε��� ��ȣ�� 3�϶�
c1 = comp_num.find("-")==3
#�ι�° - �ε��� ��ȣ�� 6�϶�
c2 = comp_num.find("-",4)==6
#�� ���̰� 12 �϶�
c3 = len(comp_num) ==12
#�� ��ȣ�� ���� �������� �˻�
c4 = comp_num.replace("-","").isdecimal()
if c1 and c2 and c3 and c4:
    print("�ùٸ� ����� ��� ��ȣ")
else :
    print("�߸��� ����� ��� ��ȣ")
```

## ��� : .py����
## ��Ű�� : ����� ����ִ� ����
- ���� ���� �ȿ� ��Ģ���� ���̽� ���� 4���� �ִٸ�, ���� ��Ű�� �ʿ�, ����� 4�� �ִ� ���̴�.
```py
import ����
from ��� import �Լ�
from ��� import �Լ�1, ���2
from ��� import *
```

## random ���
- random.shuffle(pot) : ���Ƿ� pot ����Ʈ�� ���´�.
- random.randint(1,100) : 1����100������ int�� ���Ƿ� �ϳ��� ����

## time ���
- time.sleep(2) : 2�ʵ��� ��ٸ�
- time.time() : ���� �ð� ����

## ��������� (txt, csv, json)
```py
#%% 1 ���� �����ϱ�
fileName =""
while True :
    fileName = input("������ ���ϸ��� �Է��ض�")
    #file.txt ��, txt �� �̾ƿ�.
    extName = fileName[fileName.rfind('.')+1:]
    if extName != "txt":
        print("������ �� ���� ����")
    else:
        break

# with ���̳����� �ڵ����� close�� ���ش�.
# source�� ��ü��
with open(fileName,'rt',encoding="euc-kr") as source: # utf-8�� �غôµ� �ȵǱ淡 �̰ɷ���
    with open("���纻-"+fileName,'wt') as copy:
        while True:
            #source��� ���Ͽ��� �ѱ��ھ� �����´�
            buffer=source.read(1)
            if not buffer:
                break
            copy.write(buffer)
print("���纻-"+fileName+"������ ������")
# %% 2 csv ���Ϸ� cctv�� ���ϱ�
import csv
with open('cctv.csv','r') as csvfile:
    # csvfile�� �����ǵ�, `,`�� �����ϰڴ�. ������ ���ڿ��� ""�� ���ڴ�
    buffer = csv.reader(csvfile,delimiter=",",quotechar='"')
    total =0
    for i,line in enumerate(buffer):
        if i!=0:
            total +=int(line[4])
print('CCTV �� {}���Դϴ�.'.format(total))

#%% 3 json ���Ͽ��� �о����
import json
with open('cctv.json','r',encoding='utf-8') as jsonfile:
    buffer = jsonfile.read()
    cctv_list=json.loads(buffer)
    cctv_purpose=set()
    for place in cctv_list:
        cctv_purpose.add(place['��ġ��������'])

print(cctv_purpose)
```