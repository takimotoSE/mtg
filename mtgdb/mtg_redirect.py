import pymysql.cursors
connection = pymysql.connect(host=#'hostname',
                            user=#'username',
                            password=#'password',
                            db=#'dbname',
                            charset=#'utf8',
                            cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()
cur.execute('select name from fixed_card_data where redirect_name not like ""')
names = cur.fetchall()
for name in names:
        #print(name)
        print(name["name"])
        cur.execute('select fixed_card_id from fixed_card_data where redirect_name =' + '"' + name["name"] + '"')
        cardid = cur.fetchall()
        #print(name[0]+"の裏面のidは"+str(cardid[0][0])+"です。")
        #print(cardid[0])
        print(cardid[0]["fixed_card_id"])
        cur.execute('update fixed_card_data set redirect_id='+str(cardid[0]["fixed_card_id"]) + ' where name ='+'"'+name["name"]+'"')
connection.commit()