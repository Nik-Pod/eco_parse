from config import *
import requests
import fake_useragent
from bs4 import BeautifulSoup
user = fake_useragent.UserAgent().random
header = {'user-agent': user}


def get_html(url):
    return requests.get(url, headers=header, verify=False).text


def clover(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    product_list = soup.find('ul', id='product_list')
    links = []
    nicks = []
    cols = []
    try:
        for product in product_list.find_all('a', class_='galink'):
            name = product.find('span').text.lower().replace('ё', 'е')
            href = product.get('href')
            nicks.append(name)
            links.append(href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = soup.find('div', id="pb-left-column").find('p', class_="quan").find('strong').text[:-4]
                    break
            if hascol:
                if (len(col) > 6 and col[6:].isdigit()) or col.isdigit():
                    cols.append(col)
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


def dietka(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    product_list = soup.find('div', class_="row row-price")
    links = []
    nicks = []
    cols = []
    try:
        for product in product_list.find_all('div', class_='product-name'):
            product = product.find('a')
            name = product.text.lower().replace('ё', 'е')
            href = product.get('href')
            nicks.append(name)
            links.append(href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = soup.find('div', id="product").find('span', class_="stock-quantity_success").text
                    break
            if hascol:
                if col.isdigit():
                    cols.append(col)
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


def ecofood(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    product_list = soup.find('div', id='products_search_11').find('div', class_='grid-list')
    links = []
    nicks = []
    cols = []
    try:
        for product in product_list.find_all('div', class_='ty-column4'):
            product = product.find('a', class_='product-title')
            name = product.text.lower().replace('ё', 'е')
            href = product.get('href')
            nicks.append(name)
            links.append(href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = soup.find('span', id="qty_in_stock_10808").text[-4]
                    break
            if hascol:
                if col.isdigit():
                    cols.append(col)
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


def eco(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    pages = soup.find('div', class_="nums").find_all('a', class_="dark_link")[-1].text
    nicks = []
    links = []
    cols = []
    for page in range(1, int(pages) + 1):
        if page != 1:
            url += '&PAGEN_2=' + str(page)
        soup = BeautifulSoup(get_html(url), 'lxml')
        product_list = soup.find_all('div', class_="item_block col-4 col-md-3 col-sm-6 col-xs-6")
        for product in product_list:
            name = product.find('a', class_="dark_link").text.lower().replace('ё', 'е')
            weight = product.find('span', class_="cnt")
            if weight != None:
                weight = weight.text
            else:
                weight = '100'
            name += ' ' + weight
            col = product.find('span', class_="value").text.split()[-1][1:-1]
            nicks.append(name)
            links.append(col)
    for i in names:
        hascol = False
        for n, nick in enumerate(nicks):
            flag = False
            for x in i:
                if x in nick:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                hascol = True
                col = links[n]
                break
        if hascol:
            if col.isdigit():
                cols.append(col)
            else:
                cols.append('нет в наличии')
        else:
            cols.append('нет на сайте')
    return cols


def ecov(url):
    soup = BeautifulSoup(get_html(url + str(1)), 'lxml')
    pages = soup.find('ul', class_="pagination").find_all('li')[-3].text
    links = []
    nicks = []
    cols = []
    try:
        for page in range(1, int(pages) + 1):
            soup = BeautifulSoup(get_html(url + str(page)), 'lxml')
            product_list = soup.find('div', id="content").find_all('div', class_="row")[-2]
            for product in product_list.find_all('div', class_="product-layout"):
                product = product.find('div', class_="caption").find('a')
                name = product.text.lower().replace('ё', 'е')
                href = product.get('href')
                nicks.append(name)
                links.append(href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = soup.find('ul', class_="list-unstyled").find_all('li')[-1].text[12:]
                    break
            if hascol:
                if col.isdigit():
                    cols.append(col)
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


def super(url):
    cols = []
    for i in names:
        cols.append('нет на сайте')
    return cols


def store(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    product_list = soup.find('div', class_="search-page")
    links = []
    nicks = []
    cols = []
    try:
        for product in product_list.find_all('a'):
            if len(product.get('href')) > 10:
                name = product.text.lower().replace('ё', 'е')
                href = product.get('href')
                nicks.append(name)
                links.append('https://store-eco.ru' + href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                if flag and soup.find_all('div', class_="quantity") != []:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = int(soup.find_all('div', class_="quantity")[0].text[:-4])
                    col += int(soup.find_all('div', class_="quantity")[1].text[:-4])
                    col = str(col)
                    break
            if hascol:
                if col.isdigit():
                    cols.append(col)
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


def umnaya(url):
    soup = BeautifulSoup(get_html(url + str(1)), 'lxml')
    pages = soup.find('ul', class_="pagination").find_all('li')[-3].text
    links = []
    nicks = []
    cols = []
    try:
        for page in range(1, int(pages) + 1):
            soup = BeautifulSoup(get_html(url + str(page)), 'lxml')
            product_list = soup.find('div', class_="row grid-barb heighbox barb_quest")
            for product in product_list.find_all('div', class_="product-layout"):
                product = product.find('div', class_="caption").find('a')
                name = product.text.lower().replace('ё', 'е')
                href = product.get('href')
                nicks.append(name)
                links.append(href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = soup.find('li', class_="outstock").text
                    break
            if hascol:
                col = ['Q'] + col.strip().split(' ')
                if col[-2].isdigit():
                    cols.append(col[-2])
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


def zm(url):
    soup = BeautifulSoup(get_html(url), 'lxml')
    product_list = soup.find('ul', class_="thumbs product-list")
    links = []
    nicks = []
    cols = []
    try:
        for product in product_list.find_all('li'):
            product = product.find('a')
            name = product.get('title').lower().replace('ё', 'е')
            href = product.get('href')
            nicks.append(name)
            links.append('https://zm96.ru' + href)
            print(name, 'https://zm96.ru' + href)
        for i in names:
            hascol = False
            for n, nick in enumerate(nicks):
                flag = False
                for x in i[:-1]:
                    if x in nick:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    hascol = True
                    soup = BeautifulSoup(get_html(links[n]), 'lxml')
                    col = soup.find('strong', class_="stock-critical").text.split(' ')[-2]
                    break
            if hascol:
                if col.isdigit():
                    cols.append(col)
                else:
                    cols.append('нет в наличии')
            else:
                cols.append('нет на сайте')
    except AttributeError:
        for i in names:
            cols.append('нет на сайте')
    return cols


if __name__ == '__main__':
    n1 = clover(cloverclover)
    n2 = dietka(deietka_nn)
    n3 = ecofood(ecofoodkms)
    n4 = eco(ecopp)
    n5 = ecov(ecovmecte)
    n6 = super(superfood)
    n7 = store(storeeco)
    n8 = umnaya(umnayadieta)
    n9 = zm(zm96)
    for i in range(len(names)):
        print(f'{i} {fin_names[i]} | {n1[i]} | {n2[i]} | {n3[i]} | {n4[i]} | {n5[i]} | {n6[i]} | {n7[i]} | {n8[i]} | {n9[i]}')
