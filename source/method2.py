#%% method task
# 5���� ���� �� �ִ񰪰� �ּҰ��� �����ִ� �޼ҵ�
def getMaxAndMin(dataList):
    maxdata =dataList[0] 
    mindata =dataList[0] 
    for i in range(1,len(dataList)):
        if maxdata < dataList[i] : maxdata = dataList[i]
        if mindata > dataList[i] : mindata = dataList[i]
    return maxdata, mindata
# tuple�� return �ȴ�.

dataList = [3,5,7,8]
print(getMaxAndMin(dataList))

#%% �ҹ��� �빮�ڷ� �ٲٱ�
def changeToUpper(string):
    result =""
    for i in string:
        if (i>='a' and i<='z'):
            result += chr(ord(i) - ord('a') + ord('A'))
        else:
            result += i
    return result
print(changeToUpper("Apple"))

#%% �ѱ��� ������ �ٲ��ִ� �޼ҵ� (�ϰ��̻� -> 1024)
def hanToNum(dataStr):
    han = "�����̻�����ĥ�ȱ�"

    result =0
    for i in dataStr:
        result = result*10+han.index(i)
    return result

dataStr="�ϰ��̻�"
print(hanToNum(dataStr))

#%% �������� 
result =0 # ��������
# �ʱ�ȭ�� �ڿ��� ���� �ϱ�.
def add(num1,num2=0):
    global result #�̷��� ��������� ���������� result�� ���
    result =num1+num2
def sub(num1,num2):
    global result
    result =num1-num2
add(10)
sub(10,5)
print(result)
# %%
