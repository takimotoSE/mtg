import BFZ
import requests
import re
import mojimoji 
from bs4 import BeautifulSoup
cardlist = []
txtlist = []
target_url = 'http://whisper.wisdom-guild.net/search.php?name=&name_ope=and&mcost=&mcost_op=able&mcost_x=may&ccost_more=0&ccost_less=&msw_gt=0&msw_lt=&msu_gt=0&msu_lt=&msb_gt=0&msb_lt=&ms_ope=and&msr_gt=0&msr_lt=&msg_gt=0&msg_lt=&msc_gt=0&msc_lt=&msp_gt=0&msp_lt=&msh_gt=0&msh_lt=&color_multi=able&color_ope=and&rarity_ope=or&text=&text_ope=and&oracle=&oracle_ope=and&p_more=&p_less=&t_more=&t_less=&l_more=&l_less=&display=cardname&supertype_ope=or&cardtype_ope=or&subtype_ope=or&format=all&exclude=no&set%5B%5D=BFZ&set_ope=or&illus_ope=or&illus_ope=or&flavor=&flavor_ope=and&sort=name_en&sort_op=&output='
r = requests.get(target_url)
soup = BeautifulSoup(r.text,'lxml')

def collecternums(moji):
	moji = moji.split("(")
	moji = moji[1].split(")")[0]
	return moji

for d in soup.find_all('div'):
	tmp = d.get('class')
	if tmp != None and "card" in tmp:
		divs = d.find_all('div')
		cardtype = divs[0].get_text()
		manacost = d.get_text().split("\u3000")[1].split("\t")[0]
		manacostnonkakko = re.sub('[()]','',manacost)
		manacosthan = mojimoji.zen_to_han(manacostnonkakko,ascii=False)
		manacostmath = re.sub(r'\D','',manacosthan)
		if manacostmath == "":
			manacostmathgodel = 23
		else:
			manacostmathgodel = 2**int(manacostmath)
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
			elif "◇ " == i:
				manacostmathgodel *= 17
				if manacostmathgodel % 23 == 0:
					manacostmathgodel = 17
			elif "Ｘ" == i:
				manacostmathgodel *= 19
				if manacostmathgodel % 23 == 0:
					manacostmathgodel = 19
		if cardtype != None:
			package = BFZ.cardpackage()
			cardtype = cardtype.split()
			if "―" in cardtype:
				cardtype.remove("―")
			card = None 
			package.set_name(d.b.get_text())
			package.set_rarity(cardtype[-1])
			package.set_cost(manacostmathgodel)
			text = ""
			package.set_illustrator("sho uchida")
			for p in d.find_all('p'):
				text += p.get_text() + "\n"
			package.set_text(text) 
			if "クリーチャー"  == cardtype[0]:
				package.set_subtype(cardtype[1])
				package.set_col_num(collecternums(divs[2].get_text()))
				pt = divs[1].get_text().split("/")
				package.set_power(pt[0].split("(")[0])
				package.set_toughness(pt[1].split(")")[0])
				card =BFZ.creatures(package)
			
			elif "インスタント" == cardtype[0]:
				package.set_col_num(collecternums(divs[1].get_text()))
				package.set_subtype("")				
				card = BFZ.instants(package)
			
			elif "ソーサリー" == cardtype[0]:
				package.set_col_num(collecternums(divs[1].get_text()))
				package.set_subtype("")
				card = BFZ.sorceries(package)
			elif "土地" in cardtype[0]:
				package.set_col_num(collecternums(divs[1].get_text()))
				if len(cardtype) == 4:
					subtype = cardtype[1]
				else:
					subtype = ""
				package.set_subtype(subtype)
				package.set_basic("基本" in cardtype[0])
				card = BFZ.lands(package)
			elif "アーティファクト" in cardtype[0]:
				package.set_col_num(collecternums(divs[1].get_text()))
				package.set_subtype(cardtype[1])
				card = BFZ.artifacts(package)
			elif "エンチャント" in cardtype[0]:
				package.set_col_num(collecternums(divs[1].get_text()))
				package.set_subtype(cardtype[1])
				card = BFZ.enchantments(package)
			print(card.to_dir)
