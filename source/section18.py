#%% 1 네이버 영화
from bs4 import BeautifulSoup
import requests

#사이트가 종료하긴함.
url = "https://movie.naver.com/movie/sdb/rank/rpeople.nhn"
response = requests.get(url) #요청을 보내면 응답을 할텐데, 그 응답의 페이지를 response에 담음
html = response.text #F12나오는곳에있는 text를 모두 가져옴
soup = BeautifulSoup(html,'html.parser') #html에서 파싱을 할거다. 추출할거다
result_list = soup.find_all('td',class_='title')  # td라는 태그중에 클래스명이 title인걸 가져와리
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip()) #strip():앞뒤공백을 없애준다
for person in movie_in:
    print(person)

#%% 2 네이버영화
from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response= requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
result_list = soup.find_all('div',class_='tit3')
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip()) #strip():앞뒤공백을 없애준다
for person in movie_in:
    print(person)

#%% 3 순위상승 영화 추출하기
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