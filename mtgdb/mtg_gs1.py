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
             "values('Aggressive Instinct','[\\'green\\']','[]','','Target creature you control deals damage equal" \
             " to its power to target creature you don’t control.','26','sorcery','2','','','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Ancestor Dragon','[\\'white\\']','[]','Dragon','Flying\n" \
             "Whenever one or more creatures you control attack, you gain 1 life for each attacking creature.'" \
             ",'144','creature','6','5','6','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Armored Whirl Turtle','[\\'blue\\']','[]','Turtle','','20','creature','3','0','5','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Breath of Fire','[\\'red\\']','[]','','Breath of Fire deals 2 damage to target creature.'," \
             "'22','instant','2','','','','0','');"
        cursor.execute(sql)
        sql ="insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
             "redirect_name,redirect_id,loyalty) " \
             "values('Cleansing Screech','[\\'red\\']','[]',''," \
             "'Cleansing Screech deals 4 damage to any target.','176','sorcery','5','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Colorful Feiyi Sparrow','[\\'white\\']','[]','Bird'," \
              "'Flying','6','creature','2','1','3','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Confidence from Strength','[\\'green\\']','[]',''," \
              "'Target creature gets +4/+4 and gains trample until end of turn.','52','sorcery','3','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Dragon\\'s Presence','[\\'white\\']','[]',''," \
              "'Dragon’s Presence deals 5 damage to target attacking or blocking creature.','12','instant','3','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Drown in Shapelessness','[\\'blue\\']','[]',''," \
              "'Return target creature to its owner’s hand.','10','instant','2','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Earth-Origin Yak','[\\'white\\']','[]','Ox'," \
              "'When Earth-Origin Yak enters the battlefield, creatures you control get +1/+1 until end of turn.'," \
              "'24','creature','4','2','4','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Earthshaking Si','[\\'green\\']','[]','Beast'," \
              "'Trample','416','creature','6','5','5','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Feiyi Snake','[\\'green\\']','[]','Snake'," \
              "'Reach','26','creature','2','2','1','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Ferocious Zheng','[\\'green\\']','[]','Cat・Beast'," \
              "'','676','creature','4','4','4','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Fire-Omen Crane','[\\'red\\']','[]','Bird・Spirit'," \
              "'Flying\nWhenever Fire-Omen Crane attacks, it deals 1 damage to target creature an opponent controls.'," \
              "'968','creature','5','3','3','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Hardened-Scale Armor','[\\'green\\']','[]','Aura'," \
              "'Enchant creature\nEnchanted creature gets +3/+3.','52','enchantment','3','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Heavenly Qilin','[\\'white\\']','[]','Kirin'," \
              "'Flying\nWhenever Heavenly Qilin attacks, another target creature you control gains flying until" \
              " end of turn.','12','creature','3','2','2','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Jiang Yanggu','[\\'green\\']','[legendary]','Yanggu'," \
              "'+1: Target creature gets +2/+2 until end of turn.\n" \
              "−1: If you don’t control a creature named Mowu, create a legendary 3/3 green Hound creature token named Mowu.\n" \
              "−5: Until end of turn, target creature gains trample and gets +X/+X, where X is the number of lands you control.'," \
              "'208','planeswalker','5','','','','0','4');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Journey for the Elixir','[\\'green\\']','[]',''," \
              "'Search your library and graveyard for a basic land card and a card named Jiang Yanggu, reveal them," \
              " put them into your hand, then shuffle your library.','52','sorcery','3','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Leopard-Spotted Jiao','[\\'red\\']','[]','Beast'," \
              "'','26','creature','2','3','1','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Moon-Eating Dog','[\\'blue\\']','[]','Hound'," \
              "'As long as you control a Yanling planeswalker, Moon-Eating Dog has flying.'," \
              "'40','creature','4','3','3','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Mu Yanling','[\\'blue\\']','[legendary]','Yanling'," \
              "'+2: Target creature can’t be blocked this turn.\n−3: Draw two cards.\n" \
              "−10: Tap all creatures your opponents control. You take an extra turn after this one.'," \
              "'400','planeswalker','6','','','','0','5');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Nine-Tail White Fox','[\\'blue\\']','[]','Fox・Spirit'," \
              "'Whenever Nine-Tail White Fox deals combat damage to a player, draw a card.'," \
              "'20','creature','3','2','2','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Purple-Crystal Crab','[\\'blue\\']','[]','Crab'," \
              "'When Purple-Crystal Crab dies, draw a card.'," \
              "'10','creature','2','1','1','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Qilin\\'s Blessing','[\\'white\\']','[]','','Target creature gets +2/+2 until end of turn.'," \
              "'3','instant','1','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Reckless Pangolin','[\\'green\\']','[]','Pangolin'," \
              "'Whenever Reckless Pangolin attacks, it gets +1/+1 until end of turn.'," \
              "'52','creature','3','2','2','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Rhythmic Water Vortex','[\\'blue\\']','[]',''," \
              "'Return up to two target creatures to their owner’s hand.\n" \
              "Search your library and/or graveyard for a card named Mu Yanling, reveal it, and put it into your hand. " \
              "If you searched your library this way, shuffle it.','200','sorcery','5','','','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Sacred White Deer','[\\'green\\']','[]','Elk'," \
              "'{3}{G}, {T}: You gain 4 life. Activate this ability only if you control a Yanggu planeswalker.'," \
              "'26','creature','2','2','2','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Screeching Phoenix','[\\'red\\']','[]','Phoenix'," \
              "'Flying\n{2}{R}: Creatures you control get +1/+0 until end of turn.'," \
              "'1936','creature','6','4','4','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Stormcloud Spirit','[\\'blue\\']','[]','Spirit'," \
              "'Flying','200','creature','5','4','4','','0','');"
        cursor.execute(sql)
        sql = "insert into fixed_card_data (name,color,supertype,subtype,text,cost,cardtype,cmc,power,toughness," \
              "redirect_name,redirect_id,loyalty) " \
              "values('Vivid Flying Fish','[\\'blue\\']','[]','Fish・Lizard'," \
              "'Vivid Flying Fish has flying as long as it’s attacking.','10','creature','2','1','1','','0','');"
        cursor.execute(sql)

        connection.commit()
finally:
    connection.close()

