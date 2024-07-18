# ? �޼ҵ�
- Ư���� ��ü ������ ������ �� �ִ� ���

## ���ڿ��� �پ��� �޼ҵ� ??
```py
'abc'.upper()   # �빮�� �����

'ABC'.lower()   # �ҹ��� �����

'hobby'.count('b') # 'b' ���ڰ� ��Ÿ���� Ƚ������

'hobby'.find('h')   # 'h' ������ index ��ġ�� ��ȯ

','.join('ABCD')    # 'A,B,C,D'

'   hello   '.rstrip()  # ' hello' ������ ���������

'   hello   '.lstrip()  # 'hello    ' ���� ���������

'   hello   '.strip()  # 'hello' ���������

s1 = 'Long live the King'
s1.replace('King','Queen')  #Long Live the Queen ���ڿ� ��ȯ

s1.title()  # Long Live The King Ÿ��Ʋ ���ڿ��� ��ȯ

s1.capitalize() # Long live the king ù���ڸ� �빮��

s2 = "X:Y:Z"
s2.split(":")   # :�� �����ڷ��Ͽ� s2���ڸ� ***����Ʈ***�� �и� ['X','Y','Z']

'Hello' + 'World' # 'Hello World'

```

# ? �����Լ� built-in function
- �⺻���� �����Ǿ��־� �����ϴ� �Լ�

## �پ��� �����Լ� ?
```py
abs(-100)   # ����

min(200,100,300,400)    # �ּڰ�

max(200,100,300,400)    # �ִ�

len(str1)   # ���ڿ��� ���̸� ��ȯ

eval("100+200+300") # 600, ���ڿ��� ��ġ���� �����ڷ� ��ȯ�Ͽ� ��

sorted("EABFD") # ['A','B','C','D','E','F'] ���ڿ��� ***����Ʈ***�� ����

sorted(list=[1,2,3,4],reverse=True) # ������������

a_str="Hello Python"
id(a_str)   # 4549938992 ��ü�� �ĺ����� ���������� ��ȯ

type(123)   # int ��ü�� �ڷ��� ��ȯ

```
## ������ ���� ���ڿ��� `eval(), chr(), ord()`
```py
eval('10+20')   # 10+20 ������ ���̽� �����Ⱑ ����

chr(65) # 'A' ����-> �ش��ϴ� �ƽ�Ű ����

ord('A')    # 65 ���� -> �ش��ϴ� �ƽ�Ű ����
```
