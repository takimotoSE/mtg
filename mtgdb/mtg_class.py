class cardpackage():

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        return self

    @property
    def cost(self):
        return self._cost

    def set_cost(self, cost):
        self._cost = cost
        return self

    @property
    def cardtype(self):
        return self._cardtype

    def set_cardtype(self, cardtype):
        self._cardtype = cardtype
        return self

    @property
    def supertype(self):
        return self._supertype

    def set_supertype(self, supertype):
        self._supertype = supertype
        return self

    @property
    def subtype(self):
        return self._subtype

    def set_subtype(self, subtype):
        self._subtype = subtype
        return self

    @property
    def text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        return self

    @property
    def col_num(self):
        return self._col_num

    def set_col_num(self, col_num):
        self._col_num = col_num
        return self

    @property
    def rarity(self):
        return self._rarity

    def set_rarity(self, rarity):
        self._rarity = rarity
        return self

    @property
    def version(self):
        return self._version

    def set_version(self, version):
        self._version = version
        return self

    @property
    def illustrator(self):
        return self._illustrator

    def set_illustrator(self, illustrator):
        self._illustrator = illustrator
        return self

    @property
    def power(self):
        return self._power

    def set_power(self, power):
        self._power = power
        return self

    @property
    def toughness(self):
        return self._toughness

    def set_toughness(self, toughness):
        self._toughness = toughness
        return self

    @property
    def loyalty(self):
        return self._loyalty

    def set_loyalty(self, loyalty):
        self._loyalty = loyalty
        return self

    @property
    def basic(self):
        return self._basic

    def set_basic(self, basic):
        self._basic = basic
        return self

    @property
    def redirect_name(self):
        return self._redirect_name

    def set_redirect_name(self, redirect_name):
        self._redirect_name = redirect_name
        return self

class MTGCard:
    def calc_color(self, cost):
        total = []
        lists = {3: "white", 5: "blue", 7: "black", 11: "red", 13: "green",37:"white,blue",41:"blue,black",43:"black,red",47:"red,green",53:"green,white",59:"white,brack",61:"blue,red",67:"black,green",71:"red,white",73:"green,blue",79:"white",83:"blue",89:"black",97:"red",101:"green",103:"white,blue,black,red,green",107:"white,blue,black,red,green"}
        for k, v in lists.items():
            if cost % k == 0:
                total.append(v)
        if len(total) == 0:
            total.append("colorless")
        return total

    def calc_cmc(self, cost):
        cmc = 0
        lists = [2, 3, 5, 7, 11, 13, 19, 17, 29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101,103,107]
        cost = int(cost)
        if cost == 23 or cost == 0 or cost % 29 == 0:
            return cmc
        while cost != 1:
            for i in lists:
                if cost % i == 0:
                    if cost % 103 == 0:
                        cmc = 4
                        cost = 1
                    elif cost % 107 == 0:
                        cmc = 7
                        cost = 1
                    elif cost % 79 == 0 or cost % 83 == 0 or cost % 89 == 0 or cost % 97 == 0 or cost % 101 == 0:
                        cmc += 2
                        cost = cost / i
                    elif cost % 19 == 0:
                        cost = cost / 19
                    else:
                        cmc += 1
                        cost = cost / i
        return cmc

    def __init__(self, args):
        self._name = args.name
        self._cost = args.cost
        self._color = self.calc_color(args.cost)
        self._cmc = self.calc_cmc(args.cost)
        self._image_uri = ""
        self._cardtype = ""
        self._supertype = args.supertype
        self._subtype = args.subtype
        self._text = args.text
        self._col_num = args.col_num
        self._rarity = args.rarity
        self._illustrator = args.illustrator
        self._version = args.version
        self._redirect_name = args.redirect_name
        self._power = args.power
        self._toughness = args.toughness
        self._loyalty = args.loyalty

    def save(self,cursor):
        #exit(1)
        sql = "select count(name) as name from fixed_card_data where name=%s"
        #cursor.execute(sql,(self._name,))
        cursor.execute(sql,(self._name,))
        results = cursor.fetchone()["name"]
        #exit(1)
        #print(results)
        #print((self._name,self._color,self._subtype,self._supertype,self._text,self._cost,
                                #self._cardtype,self._power,self._toughness,self._loyalty,self._redirect_name,self._cmc))
        if results == 0:
            sql = "insert into fixed_card_data (name,color,subtype,supertype,text,cost,cardtype,power,toughness,loyalty," \
                  "redirect_name,cmc) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" \
                  % (self._name.replace("\"","\\\""),self._color,self._subtype,self._supertype,self._text,self._cost,self._cardtype,self._power,self._toughness,self._loyalty,self._redirect_name,self._cmc)
            #print(sql)
            cursor.execute(sql)
            sql = "select fixed_card_id from fixed_card_data where name=\"%s\"" % (self._name.replace("\"","\\\""))
            #print(sql)
            cursor.execute(sql)
            cardid = cursor.fetchone()["fixed_card_id"]
            #print(cardid)
            sql = "insert into variables_card_data (illustrator,version,rarity,image_uri,col_num,name_id) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (self._illustrator, self._version, self._rarity, self._image_uri, self._col_num,cardid)
            cursor.execute(sql)
            #sql = "insert into variables_card_data (name_id) values()"
            #cursor.execute(sql)
        else:
            sql = "select fixed_card_id from fixed_card_data where name=\"%s\"" % (self._name.replace("\"", "\\\""))
            #print(sql)
            cursor.execute(sql)
            cardid = cursor.fetchone()["fixed_card_id"]
            #print(cardid)
            sql = "insert into variables_card_data (illustrator,version,rarity,image_uri,col_num,name_id) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
            self._illustrator, self._version, self._rarity, self._image_uri, self._col_num, cardid)
            cursor.execute(sql)

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def supertype(self):
        return self._supertype

    @property
    def subtype(self):
        return self._subtype

    @property
    def text(self):
        return self._text

    @property
    def col_num(self):
        return self._col_num

    @property
    def cost(self):
        return self._cost

    @property
    def rarity(self):
        return self._rarity

    @property
    def cardtype(self):
        return self._cardtype

    @property
    def cmc(self):
        return self._cmc

    @property
    def image_uri(self):
        return self._image_uri

    @property
    def illustrator(self):
        return self._illustrator

    @property
    def version(self):
        return self._version


    @property
    def redirect_name(self):
        return self._redirect_name

    @property
    def power(self):
        return self._power

    @property
    def toughness(self):
        return self._toughness

    @property
    def loyalty(self):
        return self._loyalty

    @property
    def to_dir(self):
        tmp = {
            'name': self._name,
            'color': self._color,
            'supertype': self._supertype,
            'subtype': self._subtype,
            'text': self._text,
            'col_num': self._col_num,
            'cost': self._cost,
            'rarity': self._rarity,
            'cardtype': self._cardtype,
            'cmc': self.cmc,
            'illustrator': self._illustrator,
            'version': self._version,
            'redirect_name': self._redirect_name,
            'power':self._power,
            'toughness':self._toughness,
            'loyalty':self._loyalty,
            'image_uri': self._image_uri
        }
        return tmp



class lands(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "land"

class creatures(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "creature"


class artifacts(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "artifact"

class artifactsVehicle(creatures):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "artifact"


class enchantments(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "enchant"


class artifactcreatures(creatures):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "artifact creature"


class enchantcreatures(creatures):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "creature enchant"


class instants(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "instant"


class sorceries(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "sorcery"


class tribalsorceries(sorceries):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "tribal sorcery"


class tribalinstants(instants):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "tribal instant"


class tribalartifacts(artifacts):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "tribal artifact"


class tribalenchantments(enchantments):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "tribal enchant"


class enchantartifacts(enchantments , artifacts):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "enchant artifact"


class artifactlands(lands , artifacts):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "artifact land"


class creaturelands(creatures , lands):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "creature land"


class planeswalkers(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "planeswalker"

class dimensions(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "dimension"


class phenomenons(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "phenomenon"


class conspiracies(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "conspiracy"


class schemes(MTGCard):
    def __init__(self, args):
        super().__init__(args)
        self._cardtype = "scheme"
