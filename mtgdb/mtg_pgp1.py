import pymysql.cursors
connection = pymysql.connect(host=#'hostname',
                            user=#'username',
                            password=#'password',
                            db=#'dbname',
                            charset=#'utf8',
                            cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Angelic Guardian','[\\'white\\']','[]','天使(Angel)','飛行\n" \
             "あなたがコントロールしているクリーチャーが１体以上攻撃するたび、ターン終了時までそれらは破壊不能を得る。'," \
             "'144','creature','6','5','5','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Angler Turtle','[\\'blue\\']','[]','海亀(Turtle)','呪禁\n" \
             "各戦闘で、対戦相手がコントロールするクリーチャーは可能なら攻撃する。','800','creature'," \
             "'7','5','7','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Vengeant Vampire','[\\'black\\']','[]','吸血鬼(Vampire)','絆魂\n" \
             "Vengeant Vampireが死亡したとき、対戦相手のコントロールするクリーチャー１体を対象とする。それを破壊し、あなたは４点のライフを得る。'," \
             "'784','creature','6','4','4','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Immortal Phoenix','[\\'red\\']','[]','フェニックス(Phoenix)','飛行\n" \
             "Immortal Phoenixが死亡したとき、これをオーナーの手札に戻す。','1936','creature','6','5','3','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Rampaging Brontodon','[\\'green\\']','[]','恐竜(Dinosaur)'," \
             "'トランプル\nRampaging Brontodonが攻撃するたび、ターン終了時までこれはあなたがコントロールする土地１つにつき+1/+1の修整を受ける。'," \
             "'5408','creature','7','7','7','  ','0',' ');"
        cursor.execute(sql)

        connection.commit()
finally:
    connection.close()