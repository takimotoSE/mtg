import mtg_scr2
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='sato1122',
                            db='mtgdb',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)
#exit(1)
for i in range(1,4):
    hoge = mtg_scr2.out(i)
    #exit(1)
    cur = connection.cursor()
    #exit(1)
    for card in hoge:
        card.save(cur)
        #exit(1)
    print(i)
connection.commit()