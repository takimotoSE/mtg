import pymysql.cursors
import requests
import re
import uuid
from bs4 import BeautifulSoup
from time import sleep

connection = pymysql.connect(host='localhost',
                            user='root',
                            password='sato1122',
                            db='mtgdb',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)

cur = connection.cursor()
cur.execute('select * from new_variables_card_data;')
#cur.execute('select new_variables_card_id,image_uri,redirect_name_id,redirect_image_uri,col_num,version from new_variables_card_data;')
card = cur.fetchall()
#uri = cur.fetchall()
for i in range(1,39000):#カード枚数
    print(i)
    nameid = card[i]["new_variables_card_id"]
    uri = card[i]["image_uri"]
    col = card[i]["col_num"]
    exp = card[i]["version"]
    target_url1 = uri
    redirectid = card[i]["redirect_name_id"]
    redirecturi = card[i]["redirect_image_uri"]
    target_url2 = redirecturi
#print(target_url)
    print(nameid)
    print(exp)
    r = requests.get(target_url1)
    soup = BeautifulSoup(r.text, 'lxml')
#print(nameid)
#print(uri)
#print(redirecturi)
#if not uri==None:
    with open(str('/home/satokoichiro/ダウンロード/mtg_img/') + str(exp) + str(col) + str('f') + str('.jpeg'),'wb') as file:
        file.write(r.content)
    sleep(1)
    if redirecturi=='':
       pass
    elif not redirecturi==None:
        r = requests.get(target_url2)
        soup = BeautifulSoup(r.text, 'lxml')
        with open(str('/home/satokoichiro/ダウンロード/mtg_img/') + str(exp) + str(col) + str('b') + str('.jpeg'),'wb') as file:
            file.write(r.content)
        sleep(1)