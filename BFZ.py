class cardpackage():
	
	@property
	def name(self):
		return self._name
	def set_name(self,name):
		self._name = name
		return self

	@property
	def cost(self):
		return self._cost
	def set_cost(self,cost):
		self._cost = cost
		return self

	@property
	def subtype(self):
		return self._subtype
	def set_subtype(self,subtype):
		self._subtype = subtype
		return self
	
	@property
	def text(self):
		return self._text
	def set_text(self,text):
		self._text = text
		return self

	@property
	def col_num(self):
		return self._col_num
	def set_col_num(self,col_num):
		self._col_num = col_num
		return self

	@property
	def rarity(self):
		return self._rarity
	def set_rarity(self,rarity):
		self._rarity = rarity
		return self

	@property
	def illustrator(self):
		return self._illustrator
	def set_illustrator(self,illustrator):
		self._illustrator = illustrator
		return self

	@property
	def power(self):
		return self._power
	def set_power(self,power):
		self._power = power
		return self

	@property
	def toughness(self):
		return self._toughness
	def set_toughness(self,toughness):
		self._toughness = toughness
		return self

	@property
	def loyalty(self):
		return self._loyalty
	def set_loyalty(self,loyalty):
		self._loyalty = loyalty
		return self
	
	@property
	def basic(self):
		return self._basic
	def set_basic(self,basic):
		self._basic = basic
		return self 

class MTGCard:
	def calc_color(self,cost):
		total = []
		lists = {3:"white",5:"blue",7:"black",11:"red",13:"green"}
		for k,v in lists.items():
        		if cost % k == 0:
                		total.append(v)
		if len(total) == 0:
        		total.append("colorless")
		return total

	def calc_cmc(self,cost):
		cmc = 0
		lists = [2,3,5,7,11,13,17]
		cost = int(cost)
		if cost == 23 or cost == 0:
			return cmc
		while cost % 19 == 0:
			cost = cost / 19
		while cost != 1:
			for i in lists:
				if cost % i == 0:
					cmc += 1
					cost = cost / i
		return cmc

	def __init__(self,args):
		self._name = args.name
		self._cost = args.cost
		self._color = self.calc_color(args.cost)
		self._cmc = self.calc_cmc(args.cost)
		self._imageURI = ""
		self._cardtype = "" 
		self._subtype = args.subtype
		self._text = args.text
		self._col_num = args.col_num
		self._rarity = args.rarity
		self._illustrator = args.illustrator
		self._version = "BFZ"
		self._lang = "jpn"

	@property
	def name(self):
		return self._name

	@property
	def color(self):
		return self._color

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
	def imageURI(self):
		return self._imageURI

	@property
	def illustrator(self):
		return self._illustrator

	@property
	def version(self):
		return self._version

	@property
	def lang(self):
		return self._lang
	
	@property	
	def to_dir(self):
		tmp = {
		'name':self._name,
		'color':self._color,
		'subtype':self._subtype,
		'text':self._text,
		'col_num':self._col_num,
		'cost':self._cost,
		'rarity':self._rarity,
		'cardtype':self._cardtype,
		'cmc':self.cmc,
		'illustrator':self._illustrator,
		'version':self._version,
		'lang':self._lang,
		'imageURI':self._imageURI
		}
		return tmp

class lands(MTGCard):
	def __init__(self,args):
		super().__init__(args)
		self._basic = args.basic
		self._cardtype = "land"
	
	@property
	def basic(self):
		return self._basic

	def to_dict(self):
		tmp = super().to_dir()
		tmp['basic'] = self._basic
		return tmp

class creatures(MTGCard):
	def __init__(self,args):
		super().__init__(args)
		self._power = args.power
		self._toughness = args.toughness
		self._cardtype = "creature"
	
	@property
	def power(self):
		return self._power

	@property 
	def toughness(self):
		return self._toughness
	
	def to_dict(self):
		tmp = super().to_dir()
		tmp['power'] = self._power
		tmp['toughness'] = self._toughness
		return tmp

class artifacts(MTGCard):
	def __init__(self,args):
		super().__init__(args)
		self._cardtype = "artifact"
	
class enchantments(MTGCard):
	def __init__(self,args):
		super().__init__(args)
		self._cardtype = "enchant"

class artifactcreatures(creatures):
	def __init__(self,args):
		super().__init__(args)
		self._cardtype = "artifact creature"

class instants(MTGCard):
	def __init__(self,args):
		super().__init__(args)
		self._cardtype = "instant"

class sorceries(MTGCard):
	def __init__(self,args):
		super().__init__(args)
		self._cardtype = "sorcery"

class planeswalkers(MTGCard):               
	def __init__(self,args):
		super().__init__(args)
		self._loyalty = args.loyalty
		self._cardtype = "planeswalker"

	@property
	def loyalty(self):
		return self._loyalty

	def to_dict(self):
		tmp = super().to_dir()
		tmp['loyalty'] = self._loyalty
		return tmp



