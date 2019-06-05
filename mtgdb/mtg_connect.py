import mtg_scr
import pymysql.cursors
connection = pymysql.connect(
                            host=#'hostname',
                            user=#'username',
                            password=#'password',
                            db=#'dbname',
                            charset=#'utf8',
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