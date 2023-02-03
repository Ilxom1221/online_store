from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv





def parsStore(category):
    list_news = []
    load_dotenv()
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36'
    }
    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

    main_art = soup.find_all('div', class_= 'car-block-main')
    for art in main_art[:5]:
        images = art.find('img', class_='big-img').get('data-src')
        name =' '.join(art.find('span', class_='car-block-titile').get_text().split())
        price =' '.join(art.find('h4').get_text().split())
        link = HOST + art.find('a', class_='product_list_img slide').get('href')


        list_news.append({
            'images': images,
            'name': name,
            'price': price,
            'link': link
        })
    return list_news

parsStore('products/category/22')