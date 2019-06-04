import requests
import re
from bs4 import BeautifulSoup

def out1(exp):
    #exp = 'nph'
    target_url = 'https://scryfall.com/search?as=full&order=name&page=1&q=set%3A' + exp + '&unique=prints'
    #target_url = 'https://scryfall.com/search?as=full&order=name&q=set%3Av17&unique=prints'
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')

    pagenum = soup.find_all(class_='search-info')
    print(pagenum)

    allcard = soup.find_all(class_="card-profile")
    allcardlist = []
    onelist = []
    for one in allcard:
        h1 = one.find_all(class_="card-text-title")
        #print(h1)
        #namelist = []
        for i in range(0, len(h1)):
            x = h1[i].get_text().split("\n")
            x = x[1].lstrip()
            #namelist.append(x)
            #onelist.append(namelist)
            onelist.append(x)
        imgs = one.find_all("img")
        #imglist = []
        for i in range(0, len(h1)):
            if not 'id="card-tooltip-img"' in imgs:
                #print(imgs[i])
                if imgs[i]["src"] == "":
                    #print(imgs[i]["data-src"])
                    #imglist.append(imgs[i]["data-src"])
                    #onelist.append(imglist)
                    onelist.append(imgs[i]["data-src"])
                if imgs[i]["src"] == "":
                    #print(imgs[i]["data-src"])
                    #imglist.append(imgs[i]["data-src"])
                    #onelist.append(imglist)
                    onelist.append(imgs[i]["data-src"])
                else:
                    #print(imgs[i]["src"])
                    #imglist.append(imgs[i]["src"])
                    #onelist.append(imglist)
                    onelist.append(imgs[i]["src"])
            #onelist.append(imglist)
        expans = one.find_all(class_="prints-current-set-name")
        for expan in expans:
            expan = expan.text
            expan = expan.split()
            expan = expan[-1]
            onelist.append(expan)
        col_rari = one.find_all(class_="prints-current-set-details")
        for c_r in col_rari:
            c_r = c_r.text
            c_r = c_r.strip()
            c_r = c_r.split(' · ')
            c_r = c_r[0:2]
            onelist.append(c_r)
        p = one.find_all('p')
        for i in p:
            herf = i.get_text()
            if 'Illustrated by' in herf:
                herf = herf.strip()
                herf = herf.replace('Illustrated by', '')
                herf = herf.strip()
                if '\n' in herf:
                    herf = herf.replace('\n','')
                    herf = herf.replace('           ','')
                    onelist.append(herf)
                else:
                    onelist.append(herf)
        #cardlanglist = []
        langlist = []
        langs = one.find_all(class_="print-langs-item")
        # print(langs)
        for lang in langs:
            lang = lang.text
            langlist.append(lang)
            if lang == '⋮':
                langlist.remove('⋮')
                #cardlanglist.append(langlist)
                onelist.append(langlist)
                langlist = []
            #else: #'⋮'がないときに入れる
            #    onelist.append(langlist) #同じく
            #    langlist = [] #同じく
        allcardlist.append(onelist)
        onelist = []
    #print(allcardlist)
        #onelist = []
    count = soup.find_all(class_="card-profile")
    #print(len(count))
    for i in range(len(count)):
        if 'https://' in allcardlist[i][2]:
            print(allcardlist[i][0])
            print(allcardlist[i][1])
            print(allcardlist[i][2])
            print(allcardlist[i][3])
            print(allcardlist[i][4])
            print(allcardlist[i][5])
            print(allcardlist[i][6])
            print(allcardlist[i][7])
        else:
            print(allcardlist[i][0])
            print(allcardlist[i][1])
            print(allcardlist[i][2])
            print(allcardlist[i][3])
            print(allcardlist[i][4])
            print(allcardlist[i][5])



def out2(exp,cur):#カード１枚用EXP
    #exp = 'nph'
    target_url = 'https://scryfall.com/search?as=full&order=name&page=1&q=set%3A' + exp + '&unique=prints'
    #target_url = 'https://scryfall.com/search?as=full&order=name&q=set%3Av17&unique=prints'
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')

    #pagenum = soup.find_all(class_='search-info')
    #num = pagenum[0]
    #num = num.text
    #num = re.sub(r'\D',' ',num)
    #page = num.split()
    #if int(page[0]) <= 20:
    #    pagenum = 1
    #else:
    #   pagenum = int(page[2])//20+1

    #for i in range(1,pagenum+1):
    #   target_url = 'https://scryfall.com/search?as=full&order=name&page=' + str(i) +'&q=set%3A' + exp + '&unique=prints'
    #    r = requests.get(target_url)
    #    soup = BeautifulSoup(r.text, 'lxml')
    #    print(i)


    allcard = soup.find_all(class_="card-profile")
    allcardlist = []
    onelist = []
    for one in allcard:
        h1 = one.find_all(class_="card-text-title")
        #print(h1)
        #namelist = []
        for i in range(0, len(h1)):
            x = h1[i].get_text().split("\n")
            x = x[1].lstrip()
            #namelist.append(x)
            #onelist.append(namelist)
            onelist.append(x)
        imgs = one.find_all("img")
        #imglist = []
        for i in range(0, len(h1)):
            if not 'id="card-tooltip-img"' in imgs:
                #print(imgs[i])
                if imgs[i]["src"] == "":
                    #print(imgs[i]["data-src"])
                    #imglist.append(imgs[i]["data-src"])
                    #onelist.append(imglist)
                    onelist.append(imgs[i]["data-src"])
                if imgs[i]["src"] == "":
                    #print(imgs[i]["data-src"])
                    #imglist.append(imgs[i]["data-src"])
                    #onelist.append(imglist)
                    onelist.append(imgs[i]["data-src"])
                else:
                    #print(imgs[i]["src"])
                    #imglist.append(imgs[i]["src"])
                    #onelist.append(imglist)
                    onelist.append(imgs[i]["src"])
            #onelist.append(imglist)
        expans = one.find_all(class_="prints-current-set-name")
        for expan in expans:
            expan = expan.text
            expan = expan.split()
            expan = expan[-1]
            onelist.append(expan)
        col_rari = one.find_all(class_="prints-current-set-details")
        for c_r in col_rari:
            c_r = c_r.text
            c_r = c_r.strip()
            c_r = c_r.split(' · ')
            c_r = c_r[0:2]
            onelist.append(c_r)
        p = one.find_all('p')
        for i in p:
            herf = i.get_text()
            if 'Illustrated by' in herf:
                herf = herf.strip()
                herf = herf.replace('Illustrated by', '')
                herf = herf.strip()
                if '\n' in herf:
                    herf = herf.replace('\n','')
                    herf = herf.replace('           ','')
                    onelist.append(herf)
                else:
                    onelist.append(herf)
        #cardlanglist = []
        langlist = []
        langs = one.find_all(class_="print-langs-item")
        # print(langs)
        for lang in langs:
            lang = lang.text
            langlist.append(lang)
                #print(langlist)
                #if lang == '⋮':
                #    langlist.remove('⋮')
                #    #onelist.append(langlist)
        onelist.append(langlist)
                #langlist = []
                #else: #'⋮'がないときに入れる
                #    onelist.append(langlist) #同じく
                #    langlist = [] #同じく
        allcardlist.append(onelist)
        onelist = []
        #print(allcardlist)
            #onelist = []
        count = soup.find_all(class_="card-profile")
        #print(len(count))
        for i in range(len(count)):
            if 'https://' in allcardlist[i][2]:
                #print(allcardlist[i][0])
                #print(allcardlist[i][1])
                #print(allcardlist[i][2])
                #print(allcardlist[i][3])
                #print(allcardlist[i][4])
                #print(allcardlist[i][5])
                #print(allcardlist[i][6])
                #print(allcardlist[i][7])

                cur.execute('select fixed_card_id from fixed_card_data where name =' + '"' + allcardlist[i][0] + '"')
                cardid = cur.fetchall()
                if len(cardid) == 0:
                    cur.execute(
                        'select fixed_card_id from fixed_card_data where name like ' + '"%/' + allcardlist[i][0] + '"')
                    cardid = cur.fetchall()
                    # print(cardid)
                name_id = cardid[0]["fixed_card_id"]
                print(name_id)
                cur.execute('select redirect_id from fixed_card_data where name =' + '"' + allcardlist[i][0] + '"')
                redirectcardid = cur.fetchall()
                if len(redirectcardid) == 0:
                    cur.execute(
                        'select redirect_id from fixed_card_data where name like ' + '"%/' + allcardlist[i][0] + '"')
                    redirectcardid = cur.fetchall()
                    # print(cardid)
                redirect_name_id = redirectcardid[0]["redirect_id"]
                print(redirect_name_id)
                img_uri = allcardlist[i][2]
                redirect_img_uri = allcardlist[i][3]
                version = allcardlist[i][4]
                col_num = allcardlist[i][5][0]
                rarity = allcardlist[i][5][1]
                illustrator = allcardlist[i][6]
                langflag = {}
                langflag["en"] = 0
                langflag["es"] = 0
                langflag["fr"] = 0
                langflag["de"] = 0
                langflag["it"] = 0
                langflag["pt"] = 0
                langflag["ja"] = 0
                langflag["ko"] = 0
                langflag["ru"] = 0
                langflag["cs"] = 0
                langflag["ct"] = 0
                langflag["sa"] = 0
                langflag["he"] = 0
                langflag["grc"] = 0
                langflag["la"] = 0
                langflag["ar"] = 0
                langflag["px"] = 0
                for langage in allcardlist[i][7]:
                    langflag[langage] = 1
                print(img_uri)
                print(redirect_img_uri)
                print(version)
                print(col_num)
                print(rarity)
                print(illustrator)
                print(langflag)
                sql = "insert into new_variables_card_data (illustrator,version,rarity,image_uri,col_num,name_id,lang_en,lang_es,lang_fr,lang_de,lang_it,lang_pt,lang_ja,lang_ko,lang_ru,lang_cs,lang_ct,lang_sa,lang_he,lang_grc,lang_la,lang_ar,lang_px,redirect_name_id,redirect_image_uri) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (illustrator, version, rarity, img_uri, col_num, name_id, langflag["en"], langflag["es"], langflag["fr"],langflag["de"], langflag["it"], langflag["pt"], langflag["ja"], langflag["ko"], langflag["ru"],langflag["cs"], langflag["ct"], langflag["sa"], langflag["he"], langflag["grc"], langflag["la"],langflag["ar"], langflag["px"],redirect_name_id,redirect_img_uri)
                cur.execute(sql)
            else:
                #print(allcardlist[i][0])
                #print(allcardlist[i][1])
                #print(allcardlist[i][2])
                #print(allcardlist[i][3])
                #print(allcardlist[i][4])
                #print(allcardlist[i][5])

                cur.execute('select fixed_card_id from fixed_card_data where name =' + '"' + allcardlist[i][0] + '"')
                cardid = cur.fetchall()
                if len(cardid) ==0:
                    cur.execute('select fixed_card_id from fixed_card_data where name like ' + '"%/' + allcardlist[i][0] + '"')
                    cardid = cur.fetchall()
                    #print(cardid)
                name_id = cardid[0]["fixed_card_id"]
                print(name_id)
                img_uri = allcardlist[i][1]
                version = allcardlist[i][2]
                col_num = allcardlist[i][3][0]
                rarity = allcardlist[i][3][1]
                illustrator = allcardlist[i][4]
                langflag = {}
                langflag["en"] = 0
                langflag["es"] = 0
                langflag["fr"] = 0
                langflag["de"] = 0
                langflag["it"] = 0
                langflag["pt"] = 0
                langflag["ja"] = 0
                langflag["ko"] = 0
                langflag["ru"] = 0
                langflag["cs"] = 0
                langflag["ct"] = 0
                langflag["sa"] = 0
                langflag["he"] = 0
                langflag["grc"] = 0
                langflag["la"] = 0
                langflag["ar"] = 0
                langflag["px"] = 0
                for langage in  allcardlist[i][5]:
                    langflag[langage] = 1
                print(img_uri)
                print(version)
                print(col_num)
                print(rarity)
                print(illustrator)
                print(langflag)
                sql = "insert into new_variables_card_data (illustrator,version,rarity,image_uri,col_num,name_id,lang_en,lang_es,lang_fr,lang_de,lang_it,lang_pt,lang_ja,lang_ko,lang_ru,lang_cs,lang_ct,lang_sa,lang_he,lang_grc,lang_la,lang_ar,lang_px) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (illustrator, version, rarity, img_uri, col_num, name_id,langflag["en"],langflag["es"],langflag["fr"],langflag["de"],langflag["it"],langflag["pt"],langflag["ja"],langflag["ko"],langflag["ru"],langflag["cs"],langflag["ct"],langflag["sa"],langflag["he"],langflag["grc"],langflag["la"],langflag["ar"],langflag["px"])
                print(sql)
                cur.execute(sql)


def out3(exp,cur):
    #exp = 'nph'
    target_url = 'https://scryfall.com/search?as=full&order=name&page=1&q=set%3A' + exp + '&unique=prints'
    #target_url = 'https://scryfall.com/search?as=full&order=name&q=set%3Av17&unique=prints'
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')

    pagenum = soup.find_all(class_='search-info')
    num = pagenum[0]
    num = num.text
    num = re.sub(r'\D',' ',num)
    page = num.split()
    if len(page) >= 3:
        print(page)
        pagenum = int(page[2]) // 20 + 1
    else:
        pagenum = 1

    for i in range(1,pagenum+1):
        target_url = 'https://scryfall.com/search?as=full&order=name&page=' + str(i) +'&q=set%3A' + exp + '&unique=prints'
        r = requests.get(target_url)
        soup = BeautifulSoup(r.text, 'lxml')
        print(target_url)


        allcard = soup.find_all(class_="card-profile")
        allcardlist = []
        onelist = []
        #return allcard
        for one in allcard:
            #名前の取得
            doublename = False
            imgs = one.find_all("img")
            namestring  = imgs[0]["title"]
            if len(namestring.split("//")) ==2:#ここに入ったら両面反転分割
                doublename = True
                name1 = namestring.split("//")[0].rstrip()
                name2 = namestring.split("//")[1].split("(")[0].rstrip()
                onelist.append(name1)
                onelist.append(name2)
            else:
                onelist.append(namestring.split("(")[0].rstrip())
            #画像の取得
            imgs = one.find_all("img")
            for img in imgs:
                if img["src"] == "":
                    #print(imgs[i]["data-src"])
                    #imglist.append(imgs[i]["data-src"])
                    #onelist.append(imglist)
                    onelist.append(img["data-src"])
                else:
                    #print(imgs[i]["src"])
                    #imglist.append(imgs[i]["src"])
                    #onelist.append(imglist)
                    onelist.append(img["src"])
            if doublename == True and len(imgs)==1:#ダブルネームなのに画像が一枚の時は反転もしくは分割なのでリダイレクト画像に空文字を入れておく。
                onelist.append("")
            #エキスパンションなどをこの後取る
            #onelist.append(imglist)
            expans = one.find_all(class_="prints-current-set-name")
            for expan in expans:
                expan = expan.text
                expan = expan.split()
                expan = expan[-1]
                onelist.append(expan)
            col_rari = one.find_all(class_="prints-current-set-details")
            for c_r in col_rari:
                c_r = c_r.text
                c_r = c_r.strip()
                c_r = c_r.split(' · ')
                c_r = c_r[0:2]
                onelist.append(c_r)
            p = one.find_all('p')
            for i in p:
                herf = i.get_text()
                if 'Illustrated by' in herf:
                    herf = herf.strip()
                    herf = herf.replace('Illustrated by', '')
                    herf = herf.strip()
                    if '\n' in herf:
                        herf = herf.replace('\n','')
                        herf = herf.replace('           ','')
                        onelist.append(herf)
                    else:
                        onelist.append(herf)
            #cardlanglist = []
            langlist = []
            langs = one.find_all(class_="print-langs-item")
            #la = langs[0]
            #print(la.text)
            for lang in langs:
                lang = lang.text
                langlist.append(lang)
                #print(langlist)
                #if lang == '⋮':
                #    langlist.remove('⋮')
                #    #onelist.append(langlist)
            onelist.append(langlist)
                #langlist = []
                #else: #'⋮'がないときに入れる
                #    onelist.append(langlist) #同じく
                #    langlist = [] #同じく
            allcardlist.append(onelist)
            onelist = []
        #print(allcardlist)
            #onelist = []
        count = soup.find_all(class_="card-profile")
        #print(len(count))
        for i in range(len(count)):
            if 'https://' in allcardlist[i][2]:
                #print(allcardlist[i][0])
                #print(allcardlist[i][1])
                #print(allcardlist[i][2])
                #print(allcardlist[i][3])
                #print(allcardlist[i][4])
                #print(allcardlist[i][5])
                #print(allcardlist[i][6])
                #print(allcardlist[i][7])
                print(allcardlist[i])
                try:
                    cur.execute('select fixed_card_id from fixed_card_data where name =' + '"' + allcardlist[i][0] + '"')
                    cardid = cur.fetchall()
                    if len(cardid) == 0:
                        cur.execute(
                            'select fixed_card_id from fixed_card_data where name like ' + '"%/' + allcardlist[i][0] + '"')
                        cardid = cur.fetchall()
                        #print(cardid)
                    name_id = cardid[0]["fixed_card_id"]
                    #print(name_id)
                    cur.execute('select redirect_id from fixed_card_data where name =' + '"' + allcardlist[i][0] + '"')
                    redirectcardid = cur.fetchall()
                    if len(redirectcardid) == 0:
                        cur.execute(
                            'select redirect_id from fixed_card_data where name like ' + '"%/' + allcardlist[i][0] + '"')
                        redirectcardid = cur.fetchall()
                    # print(cardid)
                    redirect_name_id = redirectcardid[0]["redirect_id"]
                    #print(redirect_name_id)
                    img_uri = allcardlist[i][2]
                    redirect_img_uri = allcardlist[i][3]
                    version = allcardlist[i][4]
                    col_num = allcardlist[i][5][0]
                    rarity = allcardlist[i][5][1]
                    illustrator = allcardlist[i][6]
                    langflag = {}
                    langflag["en"] = 0
                    langflag["es"] = 0
                    langflag["fr"] = 0
                    langflag["de"] = 0
                    langflag["it"] = 0
                    langflag["pt"] = 0
                    langflag["ja"] = 0
                    langflag["ko"] = 0
                    langflag["ru"] = 0
                    langflag["汉语"] = 0
                    langflag["漢語"] = 0
                    langflag["sa"] = 0
                    langflag["he"] = 0
                    langflag["grc"] = 0
                    langflag["la"] = 0
                    langflag["ar"] = 0
                    langflag["px"] = 0
                    for langage in allcardlist[i][7]:
                        langflag[langage] = 1
                    #print("img_uri=",img_uri)
                    #print("redirect_img_uri=",redirect_img_uri)
                    print("version= ",version)
                    #print("col_num=",col_num)
                    #print("rarity=",rarity)
                    #print("illustrator=",illustrator)
                    #print("langflag=",langflag)
                    sql = "insert into new_variables_card_data (illustrator,version,rarity,image_uri,col_num,name_id,lang_en,lang_es,lang_fr,lang_de,lang_it,lang_pt,lang_ja,lang_ko,lang_ru,lang_cs,lang_ct,lang_sa,lang_he,lang_grc,lang_la,lang_ar,lang_px,redirect_name_id,redirect_image_uri) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (illustrator, version, rarity, img_uri, col_num, name_id, langflag["en"], langflag["es"], langflag["fr"],langflag["de"], langflag["it"], langflag["pt"], langflag["ja"], langflag["ko"], langflag["ru"],langflag["汉语"], langflag["漢語"], langflag["sa"], langflag["he"], langflag["grc"], langflag["la"],langflag["ar"], langflag["px"],redirect_name_id,redirect_img_uri)
                    cur.execute(sql)
                except:
                    print("This is token or Unset!")
            else:
                print(allcardlist[i][0])
                #print(allcardlist[i][1])
                #print(allcardlist[i][2])
                #print(allcardlist[i][3])
                #print(allcardlist[i][4])
                #print(allcardlist[i][5])
                try:
                    cur.execute('select fixed_card_id from fixed_card_data where name =' + '"' + allcardlist[i][0].replace("\"","\\\"") + '"')
                    cardid = cur.fetchall()
                    if len(cardid) ==0:
                        cur.execute('select fixed_card_id from fixed_card_data where name like ' + '"%/' + allcardlist[i][0].replace("\"","\\\"") + '"')
                        cardid = cur.fetchall()
                    #print(cardid)

                    name_id = cardid[0]["fixed_card_id"]
                    #print(name_id)
                    img_uri = allcardlist[i][1]
                    version = allcardlist[i][2]
                    col_num = allcardlist[i][3][0]
                    rarity = allcardlist[i][3][1]
                    illustrator = allcardlist[i][4]
                    langflag = {}
                    langflag["en"] = 0
                    langflag["es"] = 0
                    langflag["fr"] = 0
                    langflag["de"] = 0
                    langflag["it"] = 0
                    langflag["pt"] = 0
                    langflag["ja"] = 0
                    langflag["ko"] = 0
                    langflag["ru"] = 0
                    langflag["汉语"] = 0
                    langflag["漢語"] = 0
                    langflag["sa"] = 0
                    langflag["he"] = 0
                    langflag["grc"] = 0
                    langflag["la"] = 0
                    langflag["ar"] = 0
                    langflag["px"] = 0
                    for langage in  allcardlist[i][5]:
                        langflag[langage] = 1
                    #print("img_uri=",img_uri)
                    print("version=",version)
                    #print("col_num=",col_num)
                    #print("rarity=",rarity)
                    #print("illustraotr=",illustrator)
                    #print("langflag=",langflag)
                    sql = "insert into new_variables_card_data (illustrator,version,rarity,image_uri,col_num,name_id,lang_en,lang_es,lang_fr,lang_de,lang_it,lang_pt,lang_ja,lang_ko,lang_ru,lang_cs,lang_ct,lang_sa,lang_he,lang_grc,lang_la,lang_ar,lang_px) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (illustrator, version, rarity, img_uri, col_num, name_id,langflag["en"],langflag["es"],langflag["fr"],langflag["de"],langflag["it"],langflag["pt"],langflag["ja"],langflag["ko"],langflag["ru"],langflag["汉语"],langflag["漢語"],langflag["sa"],langflag["he"],langflag["grc"],langflag["la"],langflag["ar"],langflag["px"])
                    #print(sql)
                    cur.execute(sql)
                except:
                    print("This is token or Unset!")
