# -*- coding: UTF-8 -*-
import os
import json
import gettext
import urllib

os.environ["LANGUAGE"] = 'ru'
tr = gettext.translation('global', 'C:\\Games\\World_of_Warships\\res\\texts')

f = open('..\\db\\ship.json')
ships = json.load(f)
f.close()

links = {}
for ship_id in ships:
    ship = ships[ship_id]
    if ship["type"] == "Auxiliary":
        continue
    if ship["nation"] == "events":
        continue
    ship_name = tr.gettext('IDS_' + ship['id_str']).decode('utf8')
    links[ship_id] = {
        "ship_id": ship_id,
        "id_str": ship['id_str'],
        "nation": ship['nation'],
        "tier": ship['tier'],
        "type": ship['type'],
        "ship_name": ship_name,
        "title": u"Wiki",
        "url": "http://wiki.wargaming.net/ru/Ship:" + urllib.quote(ship_name.encode('utf8')),
    }

# PASA905	usa	AirCarrier	5	3345987568	IDS_PASA905
del links['3345987568']
# PASA915	usa	AirCarrier	10	3335501808	[Midway]
links['3335501808']["url"] = "http://wiki.wargaming.net/ru/Ship:Midway"
# PASB001	usa	Battleship	3	4293867504	S. Carolina
links['4293867504']["url"] = "http://wiki.wargaming.net/ru/Ship:South_Carolina"
# PASB012	usa	Battleship	8	4282333168	N. Carolina
links['4282333168']["url"] = "http://wiki.wargaming.net/ru/Ship:North_Carolina"
# PASB013	usa	Battleship	4	4281284592	Arkansas B
links['4281284592']["url"] = "http://wiki.wargaming.net/ru/Ship:Arkansas_Beta"
# PASB802	usa	Battleship	3	3453958128	Michigan
del links['3453958128']
# PASB917	usa	Battleship	10	3333371888	[Montana]
links['3333371888']["url"] = "http://wiki.wargaming.net/ru/Ship:Montana"
# PASC045	usa	Cruiser	5	4247697392	Marblehead L
links['4247697392']["url"] = "http://wiki.wargaming.net/ru/Ship:Marblehead_Lima"
# PASD913	usa	Destroyer	10	3337500656	[Gearing]
links['3337500656']["url"] = "http://wiki.wargaming.net/ru/Ship:Gearing"
# PASC802	usa	Cruiser	5	3453925360	Cimarron
del links['3453925360']
# PASC803	usa	Cruiser	5	3452876784	Cimarron
del links['3452876784']
# PASC907	usa	Cruiser	4	3343824880	IDS_PASC907
del links['3343824880']
# PBSB207	uk	Battleship	7	4077860816	IDS_PBSB207
del links['4077860816']
# PBSB910	uk	Battleship	10	3340711888	[Conqueror]
links['3340711888']["url"] = "http://wiki.wargaming.net/ru/Ship:Conqueror"
# PBSD605	uk	Destroyer	5	3660462032	Anthony
del links['3660462032']
# PFSC102	france	Cruiser	2	4187928400	Jurien
links['4187928400']["url"] = "http://wiki.wargaming.net/ru/Ship:Jurien_de_la_Gravi%C3%A8re"
# PGSA509	germany	AirCarrier	8	3761223472	IDS_PGSA509
del links['3761223472']
# PGSA510	germany	AirCarrier	8	3760174896	IDS_PGSA510
del links['3760174896']
# PGSB109	germany	Battleship	9	4180621104	F. der Große
links['4180621104']["url"] = "http://wiki.wargaming.net/ru/Ship:Friedrich_der_Gro%C3%9Fe"
# PGSB110	germany	Battleship	10	4179572528	G. Kurfürst
links['4179572528']["url"] = "http://wiki.wargaming.net/ru/Ship:Gro%C3%9Fer_Kurf%C3%BCrst"
# PGSB503	germany	Battleship	3	3767482160	K. Albert
links['3767482160']["url"] = "http://wiki.wargaming.net/ru/Ship:K%C3%B6nig_Albert"
# PGSB910	germany	Battleship	10	3340711728	[G. Kurfürst]
links['3340711728']["url"] = "http://wiki.wargaming.net/ru/Ship:Gro%C3%9Fer_Kurf%C3%BCrst"
# PGSC108	germany	Cruiser	8	4181636912	Hipper
links['4181636912']["url"] = "http://wiki.wargaming.net/ru/Ship:Admiral_Hipper"
# PGSC506	germany	Cruiser	6	3764303664	Graf Spee
links['3764303664']["url"] = "http://wiki.wargaming.net/ru/Ship:Admiral_Graf_Spee"
# PGSC706	germany	Cruiser	6	3554588464	HSF Graf Spee
links['3554588464']["url"] = "http://wiki.wargaming.net/ru/Ship:Admiral_Graf_Spee"
# PGSC910	germany	Cruiser	10	3340678960	[Hindenburg]
links['3340678960']["url"] = "http://wiki.wargaming.net/ru/Ship:Hindenburg"
# PGSD106	germany	Destroyer	6	4183701296	Gaede
links['4183701296']["url"] = "http://wiki.wargaming.net/ru/Ship:Ernst_Gaede"
# PGSD107	germany	Destroyer	7	4182652720	Maass
links['4182652720']["url"] = "http://wiki.wargaming.net/ru/Ship:Leberecht_Maass"
# PISC507	italy	Cruiser	7	3763255024	Abruzzi
links['3763255024']["url"] = "http://wiki.wargaming.net/ru/Ship:Duca_degli_Abruzzi"
# PJSA917	japan	AirCarrier	10	3333404368	[Hakuryu]
links['3333404368']["url"] = "http://wiki.wargaming.net/ru/Ship:Hakuryu"
# PJSB918	japan	Battleship	10	3332323024	[Yamato]
links['3332323024']["url"] = "http://wiki.wargaming.net/ru/Ship:Yamato"
# PJSC018	japan	Cruiser	7	4276008656	Tone
del links['4276008656']
# PJSC026	japan	Cruiser	4	4267620048	Iwaki A
links['4267620048']["url"] = "http://wiki.wargaming.net/ru/Ship:Iwaki_Alpha"
# PJSC717	japan	Cruiser	7	3543054032	S. Dragon
links['3543054032']["url"] = "http://wiki.wargaming.net/ru/Ship:Southern_Dragon"
# PJSC727	japan	Cruiser	7	3532568272	E. Dragon
links['3532568272']["url"] = "http://wiki.wargaming.net/ru/Ship:Eastern_Dragon"
# PJSC934	japan	Cruiser	10	3315513040	[Zao]
links['3315513040']["url"] = "http://wiki.wargaming.net/ru/Ship:Zao"
# PJSC999	japan	Cruiser	10	3247355600	IDS_PJSC999
del links['3247355600']
# PJSD005	japan	Destroyer	6	4289607376	Mutsuki (old)
links['4289607376']["url"] = "http://wiki.wargaming.net/ru/Ship:Mutsuki"
# PJSD006	japan	Destroyer	7	4288558800	Hatsuharu (old)
links['4288558800']["url"] = "http://wiki.wargaming.net/ru/Ship:Hatsuharu"
# PJSD007	japan	Destroyer	8	4287510224	Fubuki (old)
links['4287510224']["url"] = "http://wiki.wargaming.net/ru/Ship:Fubuki"
# PJSD010	japan	Destroyer	9	4284364496	Kagero (old)
links['4284364496']["url"] = "http://wiki.wargaming.net/ru/Ship:Kagero"
# PJSD014	japan	Destroyer	2	4280170192	Tachibana L
links['4280170192']["url"] = "http://wiki.wargaming.net/ru/Ship:Tachibana_Lima"
# PJSD503	japan	Destroyer	4	3767416528	Disabled: Isokaze
del links['3767416528']
# PJSD504	japan	Destroyer	5	3766367952	Disabled: Minekaze
del links['3766367952']
# PJSD912	japan	Destroyer	10	3338548944	[Shimakaze]
links['3338548944']["url"] = "http://wiki.wargaming.net/ru/Ship:Shimakaze"
# PRSB001	ussr	Battleship	4	4293866960	Николай I
links['4293866960']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9_I"
# PRSB505	ussr	Battleship	5	3765384656	Окт. революция
links['3765384656']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%9E%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D1%80%D0%B5%D0%B2%D0%BE%D0%BB%D1%8E%D1%86%D0%B8%D1%8F"
# PRSC010	ussr	Cruiser	2	4284397008	Диана L
links['4284397008']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%94%D0%B8%D0%B0%D0%BD%D0%B0_Lima"
# PRSC109	ussr	Cruiser	9	4180587984	Дм. Донской
links['4180587984']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B9_%D0%94%D0%BE%D0%BD%D1%81%D0%BA%D0%BE%D0%B9"
# PRSC508	ussr	Cruiser	8	3762206160	Кутузов
links['3762206160']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%9C%D0%B8%D1%85%D0%B0%D0%B8%D0%BB_%D0%9A%D1%83%D1%82%D1%83%D0%B7%D0%BE%D0%B2"
# PRSC606	ussr	Cruiser	6	3659445712	Макаров
links['3659445712']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%90%D0%B4%D0%BC%D0%B8%D1%80%D0%B0%D0%BB_%D0%9C%D0%B0%D0%BA%D0%B0%D1%80%D0%BE%D0%B2"
# PRSC910	ussr	Cruiser	10	3340678608	[Москва]
links['3340678608']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0"
# PRSC999	ussr	Cruiser	10	3247355344	Test Ship
del links['3247355344']
# PRSD105	ussr	Destroyer	5	4184749520	Гневный (OLD)	http://wiki.wargaming.net/ru/Ship:Гневный (OLD)
links['4184749520']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%93%D0%BD%D0%B5%D0%B2%D0%BD%D1%8B%D0%B9"
# PRSD106	ussr	Destroyer	6	4183700944	Огневой (OLD)	http://wiki.wargaming.net/ru/Ship:Огневой (OLD)
links['4183700944']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%9E%D0%B3%D0%BD%D0%B5%D0%B2%D0%BE%D0%B9"
# PRSD108	ussr	Destroyer	8	4181603792	Ташкент (OLD)	http://wiki.wargaming.net/ru/Ship:Ташкент (OLD)
links['4181603792']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%A2%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82"
# PRSD109	ussr	Destroyer	7	4180555216	Киев (OLD)	http://wiki.wargaming.net/ru/Ship:Киев (OLD)
links['4180555216']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%9A%D0%B8%D0%B5%D0%B2"
# PRSD309	ussr	Destroyer	9	3970840016	IDS_PRSD309
del links['3970840016']
# PRSD910	ussr	Destroyer	10	3340645840	[Грозовой]
links['3340645840']["url"] = "http://wiki.wargaming.net/ru/Ship:%D0%93%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D0%BE%D0%B9"


newlist = sorted(links.values(), key=lambda k: k['id_str'])
with open('out\\links.json', 'w') as outfile:
    json.dump(newlist, outfile, encoding='utf8', indent=2, sort_keys=True)
