import requests
import re
from bs4 import BeautifulSoup
exp = 'lea'
target_url = 'https://scryfall.com/search?as=full&order=name&page=1&q=set%3A' + exp + '&unique=prints'
r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml')

#名前
def name ():
    h1 = soup.find_all(class_="card-text-title")
    for i in range(0,len(h1)):
        x = h1[i].get_text().split("\n")
        x = x[1].lstrip()
        print(x)

#画像uri
def img ():
    h1 = soup.find_all(class_="card-text-title")
    imgs = soup.find_all("img")
    for i in range(0,len(h1)):
        if not 'id="card-tooltip-img"' in imgs:
            if imgs[i]["src"]=="":
                print(imgs[i]["data-src"])
            if imgs[i]["src"]=="":
                print(imgs[i]["data-src"])
            else:
                print(imgs[i]["src"])


#エキスパンション、番号、レアリティ
def version ():
    expans= soup.find_all(class_="prints-current-set-name")
    for expan in expans:
        expan = expan.text
        expan = expan.split()
        expan = expan[-1]
        print(expan)
    col_rari = soup.find_all(class_="prints-current-set-details")
    for c_r in col_rari:
        c_r = c_r.text
        c_r = c_r.strip()
        c_r = c_r.split(' · ')
        c_r = c_r[0:2]
        print(c_r)


#イラストレーター
def illust ():
    p = soup.find_all('p')
    for i in p:
        herf = i.get_text()
        if 'Illustrated by' in herf:
            herf = herf.strip()
            herf = herf.replace('Illustrated by','')
            herf = herf.strip()
            print(herf)

#言語
def language ():
    cardlanglist = []
    langlist = []
    langs = soup.find_all(class_="print-langs-item")
    #print(langs)
    for lang in langs:
        lang = lang.text
        langlist.append(lang)
        if lang == '⋮':
            langlist.remove('⋮')
            cardlanglist.append(langlist)
            langlist = []
        #else: #'⋮'がないときに入れる
        #    cardlanglist.append(langlist) #同じく
        #    langlist = [] #同じく
    print(cardlanglist)
