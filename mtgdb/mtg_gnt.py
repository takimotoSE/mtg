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
             "values('Militant Angel','[\\'white\\']','[]','天使(Angel)','飛行、絆魂\n" \
             "Militant Angelが戦場に出た時、このターンにあなたが攻撃した対戦相手の数に等しい、\
              警戒を持つ白の2/2の騎士・クリーチャー・トークンを1体生成する。','72','creature','5','3','4','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Inspired Sphinx','[\\'blue\\']','[]','スフィンクス(Sphinx)','飛行\n" \
             "Inspired Sphinxが戦場に出た時、あなたの対戦相手の数に等しい枚数のカードを引く。" \
             "(３)(青)：飛行を持つ無色の1/1の飛行機械・アーティファクト・クリーチャー・トークン１体を生成する。','800','creature'," \
             "'7','5','5','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Rot Hulk','[\\'black\\']','[]','ゾンビ(Zombie)','威迫\n" \
             "Rot Hulkが戦場に出た時、あなたの墓地にあるゾンビ・カードをX体まで対象とし、" \
             "それを戦場に戻す。Xはあなたの対戦相手の数に等しい。','1568','creature','7','5','5','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Goblin Goliath','[\\'red\\']','[]','ゴブリン(Goblin)・ミュータント(Mutant)','Goblin Goliathが戦場に出た時、" \
             "あなたの対戦相手の数に等しい赤の1/1のゴブリン・クリーチャー・トークンを生成する。\n" \
             "(３)(赤), (Ｔ)：このターン、あなたのコントロールする発生源が対戦相手にダメージを与えるなら、" \
             "代わりにそれはその点数の2倍のダメージを与える。','1936','creature','6','5','4','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Avatar of Growth','[\\'green\\']','[]','エレメンタル(Elemental)・アバター(Avatar)'," \
             "'この呪文を唱えるためのコストは、あなたの対戦相手１人につき(１)少なくなる。\nトランプル\n" \
             "Avatar of Growthが戦場に出たとき、各プレイヤーは自身のライブラリーから基本土地・カードを最大２枚まで探し、" \
             "それらを戦場に出し、その後自身のライブラリーを切り直す。','2704','creature','6','4','4','  ','0',' ');"
        cursor.execute(sql)

        connection.commit()
finally:
    connection.close()