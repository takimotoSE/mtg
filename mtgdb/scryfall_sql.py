import pymysql.cursors
import mtg_scryfall
from time import sleep
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='sato1122',
                            db='mtgdb',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)



explist =      ['lea','leb','2ed','arn','atq','3ed','leg','drk','fem','4ed','ice','chr','hml','all','mir','vis','5ed',
                'por','wth','tmp','sth','p02','exo','usg','ath','ulg','6ed','ptk','uds','s99','mmq','nem','s00','pcy',
                'btd','inv','pls','7ed','apc','ody','dkm','tor','jud','ons','lgn','scg','8ed','mrd','dst','5dn','chk',
                'bok','sok','9ed','rav','gpt','dis','csp','tsp','plc','fut','10e','lrw','dd1','mor','shm','eve','drb',
                'ala','dd2','con','ddc','arb','m10','v09','zen','ddd','h09','wwk','dde','roe','m11','v10','ddf','som',
                'pd2','mbs','ddg','nph','cmd','m12','v11','ddh','isd','pd3','dka','ddi','avr','m13','v12','ddj','rtr',
                'cm1','gtc','ddk','dgm','mma','m14','v13','ddl','ths','c13','bng','ddm','jou','md1','m15','v14','ddn',
                'ktk','c14','evg','dvd','gvl','jvc','frf','dtk','mm2','ori','v15','bfz','c15','ogw','w16','soi','ema',
                'v16','kld','c16','aer','mm3','dds','w17','akh','hou','c17','xln','ddt','ima','v17','rix','a25','dom',
                'bbd','cm2','ss1','gs1','m19','hop','arc','pc2','cns','ddo','ddp','ddq','emn','cn2','ddr','pca','e01',
                'e02','phpr','sum','pmei','plgm','parl','ppod','jgp','palp','pal99','pgru','psus','g00','pal00','pelp',
                'g01','f01','pal01','g02','f02','pal02','f03','g03','pal03','pjjt','f04','g04','g05','f05','p05','pjse',
                'pal05','pmps','pgtw','g06','p06','f06','pjas','pmps06','pal06','pcmp','p07','g07','f07','pmps07',
                'pg07','pres','ppro','pgpx','psum','g08','p08','f08','pg08','pmps08','plpa','p15a','pwpn','g09','f09',
                'p09','pmps09','pwp09','pm10','pzen','g10','f10','p10','pmps10','pwp10','pdp10','pwwk','proe','pm11',
                'psom','p11','g11','f11','pwp11','pdp11','pmps11','pmbs','pnph','pm12','pisd','j12','f12','pdp12',
                'pwp12','pidw','pdka','pavr','pm13','prtr','f13','pi13','pdp13','pgtc','pwcq','pdgm','psdc','pm14',
                'pths','j14','f14','pi14','pdp14','pbng','pjou','ps14','pm15','pktk','f15','j15','ugin','pfrf','ptkdf',
                'potk','ps15','pori','pss1','pbfz','exp','f16','j16','pogw','psoi','pkld','mps','ps16','j17','paer',
                'pakh','mp2','phou','ps17','pss2','pxtc','pxln','j18','prix','pdom','pbbd','pss3','pm19','ps18','prwk',
                'mpr', 'pr2', 'p03', 'p04', 'pal04', 'j13', 'pemn', 'f17','ps11','psal','rin','ren','ppre','purl','prel'
                'c18','grn', 'cp3', 'gk1', 'pgrn','uma','pf19','puma','med','cp1','cp2','pdtk','brb','fnm',
                'phuk','cst','tsb','pdd2','dpa','cma','pgp17','ddu']#out3

onepromo = ['pdrc','g99','pwor','p2hg','p10e','pdtp','pbok','pnat']#out2

tuika = ['gnt']#out3

gs = ['gs1']

pgp1 = ['pgp1']

kairyo = ['isd','dka']

nakatta = ['c18','gk2','prw2']

betu = ['prel']

pmei = ['pmei']

RNA = ['rna','prna']

pred = ['pred']#out2
for i in pred:
    cur = connection.cursor()
    hoge =  mtg_scryfall.out2(i,cur)
    connection.commit()
    sleep(1)
