
import requests
from bs4 import BeautifulSoup
import lxml

# Define URL
url = 'https://istari.ru/search/search_do/?search_string=spy'
url2 = 'https://www.bookvoed.ru/'
url3 = 'https://xlm.ru/'
names = ['Без игры жизни нет. Том 2.', 'SPY x FAMILY: Семья шпиона. Том I']

s = requests.Session()
for i in range(2):
    sea = s.get(url3+'search?search=' + names[i].replace(' ', '+'))

    f = open('result.txt', 'w+')
    f.write(sea.text)
    soup = BeautifulSoup(sea.text, 'lxml')
    price1 = soup.find('span', class_='price has-text-danger')
    try:
        print(names[i] + ' ' + price1.text)
    except AttributeError as e:
        print(names[i] + ' ' + 'отсутствует')
'''
s = requests.Session()
for i in range(2):
    datas = {
        'search_string': names[i]
    }
    sea = s.post(url, data=datas)
    soup = BeautifulSoup(sea.text, 'lxml')
    price1 = soup.find('h2')
    print(names[i] + ' ' + ''.join(price1.text.split()))
'''
