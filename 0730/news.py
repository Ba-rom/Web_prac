import requests
from bs4 import BeautifulSoup
import csv
# response = requests.get("https://naver.com")
# print(response.text)

soup_objects = []

search_input = '광주인공지능사관학교'

for i in range(1, 102, 10):

    base_url = f'https://search.naver.com/search.naver?&where=news&query={search_input}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    start_num = i
    end_url = '&refresh_start=0'

    URL = base_url + str(start_num) + end_url

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    soup_objects.append(soup)

# print(len(soup_objects))

for j in soup_objects:
    news_section = j.select(
        'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li')

    for news in news_section:
        a_tag = news.select_one('dl > dt > a')

        news_title = a_tag['title']
        news_link = a_tag['href']
        
        news_data = {
            'title' : news_title,
            'link' : news_link
        }
        # print(news_data)

        with open('title_link.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['title', 'link']
            wr = csv.DictWriter(csvfile, fieldnames=fieldnames)

            wr.writerow(news_data)
            
        # print(news_title)
        # print(news_link, '\n')