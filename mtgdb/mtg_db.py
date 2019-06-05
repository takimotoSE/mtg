# -*- coding: utf-8 -*-
import pymysql.cursors

connection = pymysql.connect(host=#'hostname',
                            user=#'username',
                            password=#'password',
                            db=#'dbname',
                            charset=#"'utf8',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql=  "create table fixed_card_data(fixed_card_id int auto_increment primary key,name varchar(300)," \
              "color varchar(50),supertype varchar(30),subtype varchar(50),text varchar(2000),cost varchar(20)," \
              "cardtype varchar(50),cmc varchar(10),redirect_name varchar(300),redirect_id int(10) unsigned default 0,"\
              "power varchar(10),toughness varchar(10),loyalty varchar(10),index(fixed_card_id))"
        cursor.execute(sql)
        sql=  "create table variables_card_data(variables_card_id int auto_increment primary key,name_id int," \
              "col_num varchar(10),rarity varchar(10),illustrator varchar(100),version varchar(10)," \
              "language varchar(200),image_uri varchar(100)," \
              "foreign key (name_id) references fixed_card_data(fixed_card_id) on delete cascade," \
              "index(variables_card_id))"
        cursor.execute(sql)
        sql = "create table new_variables_card_data (new_variables_card_id int auto_increment primary key , " \
              "name_id int , col_num varchar(10) , rarity varchar(20), illustrator varchar(100),version varchar(10)," \
              "image_uri varchar(100),redirect_name_id int(10) unsigned default 0,redirect_iamge_uri varchar(100)," \
              "lang_en boolean,lang_es boolean,lang_fr boolean,lang_de boolean,lang_it boolean,lang_pt boolean," \
              "lang_ja boolean,lang_ko boolean,lang_ru boolean,lang_cs boolean,lang_ct boolean,lang_sa boolean," \
              "lang_he boolean,lang_grc boolean,lang_la boolean,lang_ar boolean,lang_px boolean," \
              "foreign key (name_id) references fixed_card_data(fixed_card_id) on delete cascade," \
              "index(new_variables_card_id));"
        cursor.execute(sql)

        sql="show tables"
        cursor.execute(sql)
        dbdata = cursor.fetchall()
        for rows in dbdata:
            print(rows)

finally:
    connection.close()



1
