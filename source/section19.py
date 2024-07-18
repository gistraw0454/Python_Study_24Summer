#%% 1 �����׷��� �ð�ȭ

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path ="C:\Windows\Fonts\H2HDRM.TTF"
font_name = font_manager.FontProperties(fname=font_path).get_name()

rc('font',family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)


data = [0.18,0.3,3.33,3.75,0.38,25,0.25,2.75,0.1]
vitamin = ['��Ÿ�� A', '��Ÿ�� B1', '��Ÿ�� B2', '���̾ƽ�', '��Ÿ�� B6','��Ÿ�� C', '��Ÿ�� D', '��Ÿ�� E', '����']

axes.pie(data, labels=vitamin, autopct="%0.1f%%")
plt.axis('equal') # Ÿ���� �ƴ϶� ������ �������Ѵ�.
plt.show()

#%% 2 bar plot 
import random
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = [n for n in range(101)]
y1 = []
y2 = []

for i in range(101):
    y1.append(random.randint(0, 100))
    y2.append(random.randint(0, 100))

axes.plot(x, y1, color='r', marker=".")
axes.bar(x, y2, color='g')
plt.show()