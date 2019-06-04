import mtg_scr
import pymysql.cursors
connection = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='sato1122',
                            db='mtgdb',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)

#exit(1)
for i in range(1,7):
    hoge = mtg_scr.out(i)
    #exit(1)
    cur = connection.cursor()
    #exit(1)
    for card in hoge:
        card.save(cur)
        #print(card)
    print(i)
connection.commit()