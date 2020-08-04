import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

movie_obj = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')
# print(movie_obj)

movie_list = []

for i in movie_obj:
    movie_tag = i.select_one('dl > dt > a')

    movie_code = movie_tag.get('href')[movie_tag.get('href').index('=')+1:]
    movie_name = movie_tag.get_text()

    # movie_list.append({'title':movie_name, 'code':movie_code})
    movie_data = {'title':movie_name, 'code':movie_code}

    with open('movie_code.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ['title', 'code']
        wr = csv.DictWriter(csvfile, fieldnames=fieldnames)

        wr.writerow(movie_data)

# print(len(movie_list))