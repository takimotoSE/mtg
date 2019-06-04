# -*- coding: utf-8 -*-
import mtg_class
import mojimoji
import re
import requests
from bs4 import BeautifulSoup


def out(pagenum=1):
    cardlist = []
    txtlist = []
    target_url = 'http://whisper.wisdom-guild.net/search.php?display=version&set%5B0%5D=RNS&set%5B1%5D=PRM&set%5B2%5D=SPC&set%5B3%5D=PRO&page=' + str(pagenum)
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, 'lxml')
    supertypelist = ["伝説の","ワールド・","基本","氷雪","持続"]


    def collecternums(moji):
        moji = moji.split("(")
        moji = moji[1].split(")")[0]
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
                    package.set_rarity("")
                    package.set_version(cardtype[-1].replace(",", " ").split())
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
                        package.set_col_num(collecternums(divs[2].get_text()))
                        package.set_illustrator(illustrators(divs[2].get_text()))
                        card = mtg_class.artifactcreatures(package)


                    elif "クリーチャー・エンチャント"  == cardtype[0]:
                        package.set_subtype(cardtype[1])
                        package.set_col_num(collecternums(divs[2].get_text()))
                        package.set_illustrator(illustrators(divs[2].get_text()))
                        card = mtg_class.enchantcreatures(package)


                    elif "クリーチャー" == cardtype[0]:
                        if not "1996 World Champion" == y[0]:
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

                        if "機体" == cardtype[1]:
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
