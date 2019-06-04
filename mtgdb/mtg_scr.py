# -*- coding: utf-8 -*-

import mtg_class
import requests
import re
import mojimoji
from bs4 import BeautifulSoup

def out(x=1):
    cardlist = []
    txtlist = []
    #target_url = 'http://whisper.wisdom-guild.net/search.php?display=version&set%5B0%5D=DOM&set%5B1%5D=RIX&set%5B2%5D=XLN&set%5B3%5D=HOU&set%5B4%5D=AKH&set%5B5%5D=AER&set%5B6%5D=KLD&set%5B7%5D=EMN&set%5B8%5D=SOI&set%5B9%5D=OGW&set%5B10%5D=BFZ&set%5B11%5D=DTK&set%5B12%5D=FRF&set%5B13%5D=KTK&set%5B14%5D=JOU&set%5B15%5D=BNG&set%5B16%5D=THS&set%5B17%5D=DGM&set%5B18%5D=GTC&set%5B19%5D=RTR&set%5B20%5D=AVR&set%5B21%5D=DKA&set%5B22%5D=ISD&set%5B23%5D=NPH&set%5B24%5D=MBS&set%5B25%5D=SOM&set%5B26%5D=ROE&set%5B27%5D=WWK&set%5B28%5D=ZEN&set%5B29%5D=ARB&set%5B30%5D=CON&set%5B31%5D=ALA&set%5B32%5D=EVE&set%5B33%5D=SHM&set%5B34%5D=MOR&set%5B35%5D=LRW&set%5B36%5D=FUT&set%5B37%5D=PLC&set%5B38%5D=TSP&set%5B39%5D=TSB&set%5B40%5D=DIS&set%5B41%5D=GPT&set%5B42%5D=RAV&set%5B43%5D=SOK&set%5B44%5D=BOK&set%5B45%5D=CHK&set%5B46%5D=5DN&set%5B47%5D=DST&set%5B48%5D=MRD&set%5B49%5D=SCG&set%5B50%5D=LGN&set%5B51%5D=ONS&set%5B52%5D=JUD&set%5B53%5D=TOR&set%5B54%5D=ODY&set%5B55%5D=APC&set%5B56%5D=PLS&set%5B57%5D=INV&set%5B58%5D=PCY&set%5B59%5D=NEM&set%5B60%5D=MMQ&set%5B61%5D=UDS&set%5B62%5D=ULG&set%5B63%5D=USG&set%5B64%5D=EXO&set%5B65%5D=STH&set%5B66%5D=TMP&set%5B67%5D=WTH&set%5B68%5D=VIS&set%5B69%5D=MIR&set%5B70%5D=CSP&set%5B71%5D=ALL&set%5B72%5D=ICE&set%5B73%5D=HML&set%5B74%5D=FEM&set%5B75%5D=DRK&set%5B76%5D=LEG&set%5B77%5D=ATQ&set%5B78%5D=ARN&set%5B79%5D=M19&set%5B80%5D=ORI&set%5B81%5D=M15&set%5B82%5D=M14&set%5B83%5D=M13&set%5B84%5D=M12&set%5B85%5D=M11&set%5B86%5D=M10&set%5B87%5D=10E&set%5B88%5D=9ED&set%5B89%5D=8ED&set%5B90%5D=7ED&set%5B91%5D=6ED&set%5B92%5D=5ED&set%5B93%5D=4ED&set%5B94%5D=3ED&set%5B95%5D=2ED&set%5B96%5D=LEB&set%5B97%5D=LEA&set%5B98%5D=S00&set%5B99%5D=S99&set%5B100%5D=PTK&set%5B101%5D=P02&set%5B102%5D=POR&set%5B103%5D=A25&set%5B104%5D=IMA&set%5B105%5D=MM3&set%5B106%5D=EMA&set%5B107%5D=MM2&set%5B108%5D=MMA&set%5B109%5D=CHR&set%5B110%5D=HOP&set%5B111%5D=PC2&set%5B112%5D=CMD&set%5B113%5D=C13&set%5B114%5D=C14&set%5B115%5D=C15&set%5B116%5D=C16&set%5B117%5D=C18&set%5B118%5D=C17&set%5B119%5D=BBD&set%5B120%5D=E02&set%5B121%5D=ANN&set%5B122%5D=ARC&set%5B123%5D=CNS&set%5B124%5D=CN2&set%5B125%5D=DDQ&set%5B126%5D=DDP&set%5B127%5D=DDO&set%5B128%5D=DDN&set%5B129%5D=DDM&set%5B130%5D=DDL&set%5B131%5D=DDK&set%5B132%5D=DDJ&set%5B133%5D=DDI&set%5B134%5D=DDH&set%5B135%5D=DDG&set%5B136%5D=DDF&set%5B137%5D=DDE&set%5B138%5D=DDD&set%5B139%5D=DDC&set%5B140%5D=DD2&set%5B141%5D=EVG&set%5B142%5D=V13&set%5B143%5D=V12&set%5B144%5D=V11&set%5B145%5D=V10&set%5B146%5D=V09&set%5B147%5D=V08&set%5B148%5D=_BD&set%5B149%5D=_BR&set%5B150%5D=PD3&set%5B151%5D=PD2&set%5B152%5D=H09&page=' + str(x)
    #target_url = 'http://whisper.wisdom-guild.net/search.php?display=version&set%5B0%5D=GRN&set%5B1%5D=UMA&set%5B2%5D=C18&page=' + str(x)
    target_url = 'http://whisper.wisdom-guild.net/search.php?display=version&set%5B0%5D=RNA&page='+str(x)
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    supertypelist = ["伝説の","ワールド・","基本","氷雪","持続"]


    def collecternums(moji):
        #print(moji)
        moji = moji.split("(")
        #print(moji)
        moji = moji[1].split(")")[0]
        #print(moji)
        return moji

    def illustrators(illust):
        illust = illust.split("Illus.")
        illust = illust[1].split("(")[0]
        return illust

    for d in soup.find_all('div'):
            tmp = d.get('class')
            if tmp != None and "card" in tmp:
                divs = d.find_all('div')
                x = []
                y = []
                x = d.find_all('a')
                for i in x:
                    y.append(i.get_text())
                cardtype = divs[0].get_text()
                manacost = d.get_text().split("\u3000")[1].split("\t")[0]
                #print(manacost)
                manacostnonkakko = re.sub('[()]', '', manacost)
                manacosthan = mojimoji.zen_to_han(manacostnonkakko, ascii=False)
                if "白/青" in manacosthan:
                    manacosthan = manacosthan.replace("白/青","A")
                if "青/黒" in manacosthan:
                    manacosthan = manacosthan.replace("青/黒","B")
                if "黒/赤" in manacosthan:
                    manacosthan = manacosthan.replace("黒/赤","C")
                if "赤/緑" in manacosthan:
                    manacosthan = manacosthan.replace("赤/緑","D")
                if "緑/白" in manacosthan:
                    manacosthan = manacosthan.replace("緑/白","E")
                if "白/黒" in manacosthan:
                    manacosthan = manacosthan.replace("白/黒","F")
                if "青/赤" in manacosthan:
                    manacosthan = manacosthan.replace("青/赤","G")
                if "黒/緑" in manacosthan:
                    manacosthan = manacosthan.replace("黒/緑","H")
                if "赤/白" in manacosthan:
                    manacosthan = manacosthan.replace("赤/白","I")
                if "緑/青" in manacosthan:
                    manacosthan = manacosthan.replace("緑/青","J")
                if "2/白" in manacosthan:
                    manacosthan = manacosthan.replace("2/白","K")
                if "2/青" in manacosthan:
                    manacosthan = manacosthan.replace("2/青","L")
                if "2/黒" in manacosthan:
                    manacosthan = manacosthan.replace("2/黒","M")
                if "2/赤" in manacosthan:
                    manacosthan = manacosthan.replace("2/赤","N")
                if "2/緑" in manacosthan:
                    manacosthan = manacosthan.replace("2/緑","O")
                manacostmath = re.sub(r'\D', '', manacosthan)
                if cardtype != None:
                    package = mtg_class.cardpackage()
                    cardtype = cardtype.split()
                    if "―" in cardtype:
                            cardtype.remove("―")
                    card = None
                    if manacostmath == "":
                        manacostmathgodel = 23
                    else:
                        manacostmathgodel = 2 ** int(manacostmath)
                    if "〔白〕" in cardtype:
                        manacostmathgodel = 3*29
                        cardtype.remove(cardtype[0])
                    if "〔青〕" in cardtype:
                        manacostmathgodel = 5*29
                        cardtype.remove(cardtype[0])
                    if "〔黒〕" in cardtype:
                        manacostmathgodel = 7*29
                        cardtype.remove(cardtype[0])
                    if "〔赤〕" in cardtype :
                        manacostmathgodel = 11*29
                        cardtype.remove(cardtype[0])
                    if "〔緑〕" in cardtype:
                        manacostmathgodel = 13*29
                        cardtype.remove(cardtype[0])
                    if "〔白/青〕" in cardtype:
                        manacostmathgodel = 37*29
                        cardtype.remove(cardtype[0])
                    if "〔青/黒〕" in cardtype:
                        manacostmathgodel = 41*29
                        cardtype.remove(cardtype[0])
                    if "〔黒/赤〕" in cardtype:
                        manacostmathgodel = 43*29
                        cardtype.remove(cardtype[0])
                    if "〔赤/緑〕" in cardtype:
                        manacostmathgodel = 47*29
                        cardtype.remove(cardtype[0])
                    if "〔緑/白〕" in cardtype:
                        manacostmathgodel = 53*29
                        cardtype.remove(cardtype[0])
                    if "〔白/黒〕" in cardtype:
                        manacostmathgodel = 59*29
                        cardtype.remove(cardtype[0])
                    if "〔青/赤〕" in cardtype:
                        manacostmathgodel = 61*29
                        cardtype.remove(cardtype[0])
                    if "〔黒/緑〕" in cardtype:
                        manacostmathgodel = 67*29
                        cardtype.remove(cardtype[0])
                    if "〔赤/白〕" in cardtype:
                        manacostmathgodel = 71*29
                        cardtype.remove(cardtype[0])
                    if "〔緑/青〕" in cardtype:
                        manacostmathgodel = 73*29
                        cardtype.remove(cardtype[0])
                    if "〔青/黒/赤〕" in cardtype:
                        manacostmathgodel = 5*7*11*29
                        cardtype.remove(cardtype[0])
                    if "〔白/青/黒/赤/緑〕" in cardtype:
                        manacostmathgodel = 103
                        cardtype.remove(cardtype[0])
                    if "〔白/青/黒/赤/緑〕" in cardtype:
                        manacostmathgodel = 107
                        cardtype.remove(cardtype[0])
                    for i in manacosthan:
                        if "白" == i:
                            manacostmathgodel *= 3
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 3
                        elif "青" == i:
                            manacostmathgodel *= 5
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 5
                        elif "黒" == i:
                            manacostmathgodel *= 7
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 7
                        elif "赤" == i:
                            manacostmathgodel *= 11
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 11
                        elif "緑" == i:
                            manacostmathgodel *= 13
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 13
                        elif "◇" == i:
                            manacostmathgodel *= 17
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 17
                        elif "Ｘ" == i:
                            manacostmathgodel *= 19
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 19
                        elif "A" == i:
                            manacostmathgodel *= 37
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 37
                        elif "B" == i:
                            manacostmathgodel *= 41
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 41
                        elif "C" == i:
                            manacostmathgodel *= 43
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 43
                        elif "D" == i:
                            manacostmathgodel *= 47
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 47
                        elif "E" == i:
                            manacostmathgodel *= 53
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 53
                        elif "F" == i:
                            manacostmathgodel *= 59
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 59
                        elif "G" == i:
                            manacostmathgodel *= 61
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 61
                        elif "H" == i:
                            manacostmathgodel *= 67
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 67
                        elif "I" == i:
                            manacostmathgodel *= 71
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 71
                        elif "J" == i:
                            manacostmathgodel *= 73
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 73
                        elif "K" == i:
                            manacostmathgodel *= 79
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 79
                        elif "L" == i:
                            manacostmathgodel *= 83
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 83
                        elif "M" == i:
                            manacostmathgodel *= 89
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 89
                        elif "N" == i:
                            manacostmathgodel *= 97
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 97
                        elif "O" == i:
                            manacostmathgodel *= 101
                            if manacostmathgodel % 23 == 0:
                                manacostmathgodel = 101
                    discoverlist = []
                    for key in supertypelist:
                        discover = re.findall(key,cardtype[0])
                        if key in cardtype[0]:
                                discoverlist.append(key)
                                cardtype[0] = cardtype[0].replace(key,'')
                        package.set_name(y[0])
                        package.set_rarity(cardtype[-1])
                        package.set_version(cardtype[-2].replace(",", " ").split())
                        package.set_cost(manacostmathgodel)
                        package.set_supertype(discoverlist)
                        if not  "Illus." in divs[1].get_text() and "/" in divs[1].get_text():
                            pt = divs[1].get_text().split("/")
                            package.set_power(pt[0].split("(")[0])
                            package.set_toughness(pt[1].split(")")[0])
                        else:
                            package.set_power('')
                            package.set_toughness('')
                        for x in ['',0,1,2,3,4,5,6,7,8,9,10]:
                            if not "/" in divs[1].get_text():
                                if str(x) in divs[1].get_text():
                                    package.set_loyalty(divs[1].get_text())
                            else:
                                package.set_loyalty('')
                        text = ""
                        k = d.find_next()
                        count = 0
                        while True:
                            k = k.find_next()
                            l = k.name
                            if "div" == l:
                                count += 1
                                if count >= 2:
                                    break
                            if count == 1 and l == "p":
                                text += k.get_text() + "\n"
                        package.set_text(text)
                        if len(y) == 2:
                            package.set_redirect_name(y[1])
                        else:
                            package.set_redirect_name('')

                        if "アーティファクト・クリーチャー" == cardtype[0]:
                            package.set_subtype(cardtype[1])
                            #print(divs)
                            package.set_col_num(collecternums(divs[2].get_text()))
                            package.set_illustrator(illustrators(divs[2].get_text()))
                            card = mtg_class.artifactcreatures(package)


                        elif "クリーチャー・エンチャント"  == cardtype[0]:
                            package.set_subtype(cardtype[1])
                            package.set_col_num(collecternums(divs[2].get_text()))
                            package.set_illustrator(illustrators(divs[2].get_text()))
                            card = mtg_class.enchantcreatures(package)


                        elif "クリーチャー" == cardtype[0]:
                            if not "Nameless Race" == y[0]:
                                package.set_subtype(cardtype[1])
                            else:
                                package.set_subtype('')
                            if "Illus." in divs[2].get_text():
                                package.set_col_num(collecternums(divs[2].get_text()))
                                package.set_illustrator(illustrators(divs[2].get_text()))
                            else:
                                package.set_col_num(collecternums(divs[4].get_text()))
                                package.set_illustrator(illustrators(divs[4].get_text()))
                            card = mtg_class.creatures(package)


                        elif "土地・クリーチャー" == cardtype[0]:
                            package.set_subtype(cardtype[1])
                            package.set_col_num(collecternums(divs[2].get_text()))
                            package.set_illustrator(illustrators(divs[2].get_text()))
                            card = mtg_class.creaturelands(package)

                        elif "インスタント" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            package.set_subtype("")
                            card = mtg_class.instants(package)

                        elif "部族インスタント" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            package.set_subtype(cardtype[1])
                            card = mtg_class.tribalinstants(package)

                        elif "ソーサリー" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            package.set_subtype("")
                            card = mtg_class.sorceries(package)

                        elif "部族ソーサリー" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            package.set_subtype(cardtype[1])
                            card = mtg_class.tribalsorceries(package)

                        elif "アーティファクト・土地" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            if len(cardtype) == 4:
                                subtype = cardtype[1]
                            else:
                                subtype = ""
                            package.set_subtype(subtype)
                            package.set_basic("基本" in cardtype[0])
                            card = mtg_class.artifactlands(package)

                        elif "土地" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            if len(cardtype) == 4:
                                subtype = cardtype[1]
                            else:
                                subtype = ""
                            package.set_subtype(subtype)
                            package.set_basic("基本" in cardtype[0])
                            card = mtg_class.lands(package)

                        elif "アーティファクト" == cardtype[0]:

                            if "機体" in cardtype[1]:
                                package.set_subtype(cardtype[1])
                                package.set_col_num(collecternums(divs[2].get_text()))
                                package.set_illustrator(illustrators(divs[2].get_text()))
                                card = mtg_class.artifactsVehicle(package)

                            else:
                                package.set_col_num(collecternums(divs[1].get_text()))
                                package.set_illustrator(illustrators(divs[1].get_text()))
                                if len(cardtype) <= 3:
                                    package.set_subtype("")
                                else:
                                    package.set_subtype(cardtype[1])
                            card = mtg_class.artifacts(package)

                        elif "部族アーティファクト" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            if len(cardtype) <= 3:
                                package.set_subtype("")
                            else:
                                package.set_subtype(cardtype[1])
                            card = mtg_class.tribalartifacts(package)

                        elif "エンチャント・アーティファクト" == cardtype[0]:
                            try:
                                package.set_col_num(collecternums(divs[1].get_text()))
                                package.set_illustrator(illustrators(divs[1].get_text()))
                                if len(cardtype) <= 3:
                                    package.set_subtype("")
                                else:
                                    package.set_subtype(cardtype[1])
                            except:
                                package.set_col_num(collecternums(divs[2].get_text()))
                                package.set_illustrator(illustrators(divs[2].get_text()))
                                if len(cardtype) <= 3:
                                    package.set_subtype("")
                                else:
                                    package.set_subtype(cardtype[1])
                            card = mtg_class.enchantartifacts(package)

                        elif "エンチャント" == cardtype[0]:
                            try:
                                package.set_col_num(collecternums(divs[1].get_text()))
                                package.set_illustrator(illustrators(divs[1].get_text()))
                                if len(cardtype) <= 3:
                                    package.set_subtype("")
                                else:
                                    package.set_subtype(cardtype[1])
                            except:
                                package.set_col_num(collecternums(divs[2].get_text()))
                                package.set_illustrator(illustrators(divs[2].get_text()))
                                if len(cardtype) <= 3:
                                    package.set_subtype("")
                                else:
                                    package.set_subtype(cardtype[1])
                            card = mtg_class.enchantments(package)

                        elif "部族エンチャント" == cardtype[0]:
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            if len(cardtype) <= 3:
                                package.set_subtype("")
                            else:
                                package.set_subtype(cardtype[1])
                            card = mtg_class.tribalenchantments(package)

                        elif "プレインズウォーカー" == cardtype[0]:
                            package.set_subtype(cardtype[1])
                            package.set_col_num(collecternums(divs[2].get_text()))
                            package.set_illustrator(illustrators(divs[2].get_text()))
                            card = mtg_class.planeswalkers(package)

                        elif "次元" == cardtype[0]:
                            package.set_subtype(cardtype[1])
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            card = mtg_class.dimensions(package)

                        elif "策略" == cardtype[0]:
                            package.set_subtype('')
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            card = mtg_class.conspiracies(package)

                        elif "現象" == cardtype[0]:
                            package.set_subtype('')
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            card = mtg_class.phenomenons(package)

                        elif "計略" == cardtype[0]:
                            package.set_subtype('')
                            package.set_col_num(collecternums(divs[1].get_text()))
                            package.set_illustrator(illustrators(divs[1].get_text()))
                            card = mtg_class.schemes(package)

                    #cardlist.append(card.to_dir)
                    cardlist.append(card)
    return(cardlist)

if __name__=='__main__':
    print(out())
