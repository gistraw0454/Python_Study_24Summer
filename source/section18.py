#%% 1 ���̹� ��ȭ
from bs4 import BeautifulSoup
import requests

#����Ʈ�� �����ϱ���.
url = "https://movie.naver.com/movie/sdb/rank/rpeople.nhn"
response = requests.get(url) #��û�� ������ ������ ���ٵ�, �� ������ �������� response�� ����
html = response.text #F12�����°����ִ� text�� ��� ������
soup = BeautifulSoup(html,'html.parser') #html���� �Ľ��� �ҰŴ�. �����ҰŴ�
result_list = soup.find_all('td',class_='title')  # td��� �±��߿� Ŭ�������� title�ΰ� �����͸�
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip()) #strip():�յڰ����� �����ش�
for person in movie_in:
    print(person)

#%% 2 ���̹���ȭ
from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response= requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
result_list = soup.find_all('div',class_='tit3')
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip()) #strip():�յڰ����� �����ش�
for person in movie_in:
    print(person)

#%% 3 ������� ��ȭ �����ϱ�
from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response= requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
movie_list = soup.find_all('tr')
up_list = []
for movie in movie_list:
    target_list = movie.find_all('td',class_='ac')
    if target_list:
        if (target_list[1].find('img',class_='arrow').get('alt')=='up'):
            up_list.append(movie.find('td',class_='title').text.stri[()])
        
for up_movie in up_list:
    print(up_movie)