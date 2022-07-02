
import requests
from bs4 import BeautifulSoup
import lxml

# Define URL
url = 'https://istari.ru/search/search_do/?search_string=spy'
url2 = 'https://www.bookvoed.ru/'
url3 = 'https://xlm.ru/'

names = ['Истребитель демонов. Том 1. Жестокость',
         'SPY x FAMILY: Семья шпиона. Том I',
         'Без игры жизни нет. Том 2.', 'Человек-бензопила. Книга 1. Пес и бензопила. Бензопила против нетопыря',
         'Beastars. Выдающиеся звери. Том 1', ]

s1 = requests.Session()
s2 = requests.Session()
s3 = requests.Session()
for i in range(len(names)):
    print(names[i])
    datas = {
        'search_string': names[i]
    }
    istari = s1.post(url, data=datas)
    bookvo = s2.post(url2+'books?q=' + names[i].replace(' ', '+'))
    ixl = s3.get(url3+'search?search=' + names[i].replace(' ', '+'))

    soup = BeautifulSoup(istari.text, 'lxml')
    price1 = soup.find('h2')
    try:
        print('истари ' + ''.join(price1.text.split()))
    except AttributeError as e:
        print('истари' + ' ' + 'отсутствует')
    soup = BeautifulSoup(bookvo.text, 'lxml')
    price1 = soup.find('div', class_='Ag')
    try:
        print('буквожуй ' + price1.text[1:])
    except AttributeError as e:
        print('буквожуй' + ' ' + 'отсутствует')
    soup = BeautifulSoup(ixl.text, 'lxml')
    price1 = soup.find('span', class_='price has-text-danger')
    try:
        print('ixl' + ' ' + price1.text)
    except AttributeError as e:
        print('ixl' + ' ' + 'отсутствует')

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
#sea = s.post(url, data=datas)
#f = open('result.txt', 'w+')
# f.write(sea.text)
# requests.get(url)

#headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'


#pages = requests.get(url)


#soup = BeautifulSoup(sea.text, 'lxml')

# print(soup.div)
#price1 = soup.find('h2')
# print(soup.h2.text)
# print(''.join(price1.text.split()))
