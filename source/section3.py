#%% 1 �νǼ��� ��
num1 = float(input("ù��° �Ǽ� : "))
num2 = float(input("�ι�° �Ǽ� : "))

print("{n1}�� {n2}�� ���� {result}�Դϴ�.".format(n1=num1,n2=num2,result=num1+num2))

#%% 2 �ش� ���� ���ϱ��� �ִ���?
days = [31,28,31,30,31,30,31,31,30,31,30,31]
month = int(input("1���� 12������ ���� �Է��ϼ���"))
print("%d���� %d�� ���� �ֽ��ϴ�." %(month,days[month-1]))

#%% 3 ������� �����
english_dict= {'flower':'��', 'fly':'����', 'floor':'�ٴ�'}

word = input("���� �ܾ �Է��ϼ���")
print("{}:{}".format(word,english_dict[word]))

#%% 4 
#set : ����, �ߺ��� ���Ҹ� ���� �� ����.
# ���� ���� �˻簡 �����̴�.

result = set()
for i in range(3):
    result.add(input("����ϴ� ���� �������� �Է��ϼ���"))

print("����� ���п������� {}�Դϴ�.".format(result))

