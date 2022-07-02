import requests
from bs4 import BeautifulSoup
import csv

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}

link = "https://www.bookvoed.ru/books?genre=1585"


# with open('mangalist.csv', 'w', newline = '') as csvfile:
def findAllBookv():
    allmanga = "https://www.bookvoed.ru/books?genre=1585&offset="
    global header
    f = open('data/bookvojyi.txt', 'w+')
    offset = 0
    names = [0]
    allnames = []
    while len(names) != 0:

        responce = requests.get(allmanga + str(offset), headers=header)
        offset += 60
        soup = BeautifulSoup(responce.text, 'lxml')

        names = soup.find_all('a', class_='TUb os')
        prices = soup.find_all('div', class_='Ag')
        for name, price in zip(names, prices):
            allnames.append(name.text + '' + price.text[1:])
            # f.write(name.text + '' + price.text[1:])
    allnames.sort()
    for name in allnames:
        f.write(name)


def findAllXlm():
    url = 'https://xlm.ru/manga?page='
    page = 1
    global header
    f = open('data/xlmedia.txt', 'w+')
    names = [0]
    allnames = []
    while len(names) != 0:
        responce = requests.get(url + str(page), headers=header)
        page += 1
        soup = BeautifulSoup(responce.text, 'lxml')

        names = soup.find_all('a', class_='product-name')
        prices = soup.find_all('span', class_='price')
        for name, price in zip(names, prices):
            allnames.append(name.text.strip() + ' ' +
                            ''.join(price.text.split()) + '\n')
            # f.write(name.text.strip() + ' ' +
            #        ''.join(price.text.split()) + '\n')
    allnames.sort()
    for name in allnames:
        f.write(name)

# print(name.text)
# ''.join(price.text.split())


findAllXlm()
findAllBookv()

# f.write(responce.text)
# print(soup.find('div', id='user_agent').text)
