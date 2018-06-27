# -*- coding: UTF-8 -*-
import os
import json
import requests
import HTMLParser
import gettext

os.environ["LANGUAGE"] = 'ru'
tr = gettext.translation('global', '..\\res\\texts')

f = open('..\\db\\ship.json')
ships = json.load(f)
f.close()

class MyHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.ul = 0
        self.in_list = 0
        self.links = []
        self.span = 0
        self.h4 = 0
        self.in_list2 = 0
        self.href = ''
        self.all_links = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            self.ul += 1

        if tag == 'span':
            self.span += 1

        if tag == 'h4':
            self.h4 += 1

        if tag == 'ul':
            for attr in attrs:
                if attr[0] == 'class' and attr[1].startswith('ipsDataItem_subList'):
                    self.in_list = self.ul

        if tag == 'span':
            for attr in attrs:
                if attr[0] == 'class' and attr[1].startswith('ipsType_break'):
                    self.in_list2 = self.span
        elif tag == 'h4':
            for attr in attrs:
                if attr[0] == 'class' and attr[1].endswith('ipsType_break'):
                    self.in_list2 = self.h4

        if tag == 'a' and self.in_list > 0 and self.in_list == self.ul:
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

        if tag == 'a' and self.in_list2:
            title = ''
            self.href = ''
            for attr in attrs:
                if attr[0] == 'title':
                    title = attr[1]
                if attr[0] == 'href':
                    self.href = attr[1]
            if title:
                self.all_links[self.href] = title
                self.href = ''

    def handle_data(self, data):
        if self.in_list2 and self.href:
            self.all_links[self.href] = data
            print(self.href, data)
            self.href = ''

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.ul -= 1
            self.in_list = 0
        if tag == 'span':
            self.span -= 1
            self.in_list2 = 0
        if tag == 'h4':
            self.h4 -= 1
            self.in_list2 = 0

links = {}

mainPage = requests.get('https://forum.worldofwarships.ru/forum/374-%D0%BA%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D0%B8-%D0%B2-%D0%B8%D0%B3%D1%80%D0%B5/')
parser = MyHTMLParser()
parser.feed(mainPage.content.decode(mainPage.encoding))
# print parser.links

for link in parser.links:
    print '--link-- ' + link
    page = requests.get(link)
    parser = MyHTMLParser()
    parser.feed(page.content.decode(page.encoding))
    for url in parser.all_links:
        title  = parser.all_links[url]
        for ship_id in ships:
            ship = ships[ship_id]
            ship_name = tr.gettext('IDS_' + ship['id_str']).decode('utf8')
            ship_name = ship_name\
                .replace('[', '')\
                .replace(']', '')\
                .replace(' (OLD)', '')\
                .replace(' (old)', '')\
                + ''
            if title.lower().find(ship_name.lower()) >= 0:
                links[ship_id] = {
                    "ship_id": ship_id,
                    "id_str": ship['id_str'],
                    "nation": ship['nation'],
                    "tier": ship['tier'],
                    "type": ship['type'],
                    "ship_name": ship_name,
                    "title": u"Форум",
                    "url": url,
                }
                # print ['found!', ship_id, ship_name, url]

ships_add = {}
# PASA015	usa	AirCarrier	10	3335501808	Midway
ships_add['3335501808'] = 'https://forum.worldofwarships.ru/topic/51970-midway-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%B0%D0%B2%D0%B8%D0%B0%D0%BD%D0%BE%D1%81%D0%B5%D1%86-%D1%85-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-064x/'\
# PASC020	usa	Cruiser		10	4273911792	Des Moines
ships_add['4273911792'] = 'https://forum.worldofwarships.ru/topic/91133-des-moines-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-%D1%81%D1%88%D0%B0-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-068/'\
# PASB001	usa	Battleship	3	4293867504	S. Carolina
ships_add['4293867504'] = 'https://forum.worldofwarships.ru/topic/57884-south-carolina-iii-0515x/'
# PASB012	usa	Battleship	8	4282333168	N. Carolina
ships_add['4282333168'] = 'https://forum.worldofwarships.ru/topic/40380-north-carolina-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PASB017	usa	Battleship	10	4277090288	Montana
ships_add['4277090288'] = 'https://forum.worldofwarships.ru/topic/29782-%D0%BE%D1%82-%D0%B0-%D0%B4%D0%BE-%D1%8F-%D0%BC%D0%BE%D0%BD%D1%82%D0%B0%D0%BD%D0%B0-0611%D1%85/'
# ASB705	usa	Battleship	5	3555670000	Texas
ships_add['3555670000'] = 'https://forum.worldofwarships.ru/topic/63710-%D1%82%D0%B5%D1%85%D0%B0%D1%81-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-0615/'
# PASB708	usa	Battleship	8	3552524272	Alabama ST
ships_add['3552524272'] = 'https://forum.worldofwarships.ru/topic/83896-alabama-%E2%80%94-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PASB917	usa	Battleship	10	3333371888	[Montana]
ships_add['3333371888'] = 'https://forum.worldofwarships.ru/topic/29782-%D0%BE%D1%82-%D0%B0-%D0%B4%D0%BE-%D1%8F-%D0%BC%D0%BE%D0%BD%D1%82%D0%B0%D0%BD%D0%B0-0611%D1%85/'
# PASC005	usa	Cruiser	5	4289640432	Omaha
ships_add['4289640432'] = 'https://forum.worldofwarships.ru/topic/32698-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BD%D0%B0-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-omaxa/'
# PASC006	usa	Cruiser	7	4288591856	Atlanta
ships_add['4288591856'] = 'https://forum.worldofwarships.ru/topic/24697-%D0%BE%D0%B1%D0%B7%D0%BE%D1%80-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D0%B0-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-%D0%B0%D1%82%D0%BB%D0%B0%D0%BD%D1%82%D0%B0-upd-271116/'
# PASC045	usa	Cruiser	5	4247697392	Marblehead L
ships_add['4247697392'] = 'https://forum.worldofwarships.ru/topic/76656-uss-marblehead-cl-12-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072x/'
# PASC507	usa	Cruiser	7	3763255280	Indianapolis
ships_add['3763255280'] = 'https://forum.worldofwarships.ru/topic/90244-%C2%AB%D0%B8%D0%BD%D0%B4%D0%B8%D0%B0%D0%BD%D0%B0%D0%BF%D0%BE%D0%BB%D0%B8%D1%81%C2%BB-%D0%BF%D1%80%D0%B5%D0%BC%D1%83%D0%B8%D0%BC-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-068/'
# PASD913	usa	Destroyer	10	3337500656	[Gearing]
ships_add['3337500656'] = 'https://forum.worldofwarships.ru/topic/52407-gearing-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-%D1%85-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-055%D1%85/'
# PBSB910	uk	Battleship	10	3340711888	[Conqueror]
ships_add['3340711888'] = 'https://forum.worldofwarships.ru/topic/93471-conqueror-%E2%80%94-%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PBSC108	uk	Cruiser	8	4181637072	Edinburgh
ships_add['4181637072'] = 'https://forum.worldofwarships.ru/topic/70446-%D1%8D%D0%B4%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3-%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D1%91%D0%B3%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-0513/'
# PGSB109	germany	Battleship	9	4180621104	F. der Große
ships_add['4180621104'] = 'https://forum.worldofwarships.ru/topic/75348-friedrich-der-gro%C3%9Fe-h39-%E2%80%94-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-ix-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-069x/'
# PGSB110	germany	Battleship	10	4179572528	G. Kurfürst
ships_add['4179572528'] = 'https://forum.worldofwarships.ru/topic/63214-gro%C3%9Fer-kurf%C3%BCrst-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-0510x/'
# PGSB503	germany	Battleship	3	3767482160	K. Albert
ships_add['3767482160'] = 'https://forum.worldofwarships.ru/topic/72606-sms-k%C3%B6nig-albert-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-iii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072x/'
# GSB910	germany	Battleship	10	3340711728	[G. Kurfürst]
ships_add['3340711728'] = 'https://forum.worldofwarships.ru/topic/63214-gro%C3%9Fer-kurf%C3%BCrst-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-0510x/'
# PGSC106	germany	Cruiser	6	4183734064	Nürnberg
ships_add['4183734064'] = 'https://forum.worldofwarships.ru/topic/33945-%D0%BD%D1%8E%D1%80%D0%BD%D0%B1%D0%B5%D1%80%D0%B3-%D0%BB%D1%91%D0%B3%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PGSC107	germany	Cruiser	7	4182685488	Yorck
ships_add['4182685488'] = 'https://forum.worldofwarships.ru/topic/34019-%D0%B9%D0%BE%D1%80%D0%BA-%D1%82%D1%8F%D0%B6%D1%91%D0%BB%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PGSC108	germany	Cruiser	8	4181636912	Hipper
ships_add['4181636912'] = 'https://forum.worldofwarships.ru/topic/33808-%D0%B0%D0%B4%D0%BC%D0%B8%D1%80%D0%B0%D0%BB-%D1%85%D0%B8%D0%BF%D0%BF%D0%B5%D1%80-%D1%82%D1%8F%D0%B6%D1%91%D0%BB%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PGSC506	germany	Cruiser	6	3764303664	Graf Spee
ships_add['3764303664'] = 'https://forum.worldofwarships.ru/topic/76443-admiral-graf-spee-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072%D1%85/'
# PGSC706	germany	Cruiser	6	3554588464	HSF Graf Spee
ships_add['3554588464'] = 'https://forum.worldofwarships.ru/topic/76443-admiral-graf-spee-%D0%BD%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072%D1%85/'
# PGSC910	germany	Cruiser	10	3340678960	[Hindenburg]
ships_add['3340678960'] = 'https://forum.worldofwarships.ru/topic/35906-hindenburg-%D1%82%D1%8F%D0%B6%D1%91%D0%BB%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PISC506	italy	Cruiser	6	3764303600	Duca d'Aosta
ships_add['3764303600'] = 'https://forum.worldofwarships.ru/topic/86198-duca-d%E2%80%99-aosta-%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D1%8F%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072x/'
# PJSA917	japan	AirCarrier	10	3333404368	[Hakuryu]
ships_add['3333404368'] = 'https://forum.worldofwarships.ru/topic/39880-%D0%B3%D0%B0%D0%B9%D0%B4-hakuryu-062x/'
# PJSB705	japan	Battleship	5	3555669712	ARP Kongō
ships_add['3555669712'] = 'https://forum.worldofwarships.ru/topic/21980-kongo-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSB706	japan	Battleship	5	3554621136	ARP Kirishima
ships_add['3554621136'] = 'https://forum.worldofwarships.ru/topic/21980-kongo-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSB707	japan	Battleship	5	3553572560	ARP Haruna
ships_add['3553572560'] = 'https://forum.worldofwarships.ru/topic/21980-kongo-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSB708	japan	Battleship	5	3552523984	ARP Hiei
ships_add['3552523984'] = 'https://forum.worldofwarships.ru/topic/21980-kongo-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSB799	japan	Battleship	5	3457103568	ARP Kirishima
ships_add['3457103568'] = 'https://forum.worldofwarships.ru/topic/21980-kongo-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSB918	japan	Battleship	10	3332323024	[Yamato]
ships_add['3332323024'] = 'https://forum.worldofwarships.ru/topic/51992-%D0%B3%D0%B0%D0%B9%D0%B4-yamato-x-069%D1%85/'
# PJSC004	japan	Cruiser	4	4290688720	Yūbari
ships_add['4290688720'] = 'https://forum.worldofwarships.ru/topic/18832-%D1%8E%D0%B1%D0%B0%D1%80%D0%B8-%D1%8F%D0%BF-%E5%A4%95%E5%BC%B5-%E2%80%93-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-iv-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSC705	japan	Cruiser	7	3555636944	ARP Myoko
ships_add['3555636944'] = 'https://forum.worldofwarships.ru/topic/78683-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-ijn-myoko-065/'
# PJSC707	japan	Cruiser	7	3553539792	ARP Ashigara
ships_add['3553539792'] = 'https://forum.worldofwarships.ru/topic/78683-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-ijn-myoko-065/'
# PJSC709	japan	Cruiser	7	3551442640	ARP Haguro
ships_add['3551442640'] = 'https://forum.worldofwarships.ru/topic/78683-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-ijn-myoko-065/'
# PJSC717	japan	Cruiser	7	3543054032	S. Dragon
ships_add['3543054032'] = 'https://forum.worldofwarships.ru/topic/78683-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-ijn-myoko-065/'
# PJSC727	japan	Cruiser	7	3532568272	E. Dragon
ships_add['3532568272'] = 'https://forum.worldofwarships.ru/topic/78683-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-ijn-myoko-065/'
# PJSC737	japan	Cruiser	7	3522082512	ARP Nachi
ships_add['3522082512'] = 'https://forum.worldofwarships.ru/topic/78683-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-ijn-myoko-065/'
# PJSC708	japan	Cruiser	8	3552491216	ARP Takao
ships_add['3552491216'] = 'https://forum.worldofwarships.ru/topic/72679-ijn-atago%E6%84%9B%E5%AE%95-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F0630/'
# PJSC799	japan	Cruiser	8	3457070800	ARP Takao
ships_add['3457070800'] = 'https://forum.worldofwarships.ru/topic/72679-ijn-atago%E6%84%9B%E5%AE%95-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F0630/'
# PJSC934	japan	Cruiser	10	3315513040	[Zao]
ships_add['3315513040'] = 'https://forum.worldofwarships.ru/topic/19646-zao-%E2%80%94-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSD005	japan	Destroyer	6	4289607376	Mutsuki (old)
ships_add['4289607376'] = 'https://forum.worldofwarships.ru/topic/51704-mutsuki-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-0542/'
# PJSD006	japan	Destroyer	7	4288558800	Hatsuharu (old)
ships_add['4288558800'] = 'https://forum.worldofwarships.ru/topic/51916-ijn-hatsuharu-%E5%88%9D%E6%98%A5-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-060%D1%85/'
# PJSD007	japan	Destroyer	8	4287510224	Fubuki (old)
ships_add['4287510224'] = 'https://forum.worldofwarships.ru/topic/21945-fubuki-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F/'
# PJSD010	japan	Destroyer	9	4284364496	Kagero (old)
ships_add['4284364496'] = 'https://forum.worldofwarships.ru/topic/104094-%D0%BA%D0%B0%D0%B3%D0%B5%D1%80%D0%BE-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-%D1%8F%D0%BF%D0%BE%D0%BD%D0%B8%D0%B8-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-%D0%BD%D0%B8%D0%BD%D0%B4%D0%B7%D1%8F-%D0%B1%D0%BE%D1%8F%D1%80%D0%B8%D0%BD-070%D1%85/'
# PJSD014	japan	Destroyer	2	4280170192	Tachibana L
ships_add['4280170192'] = 'https://forum.worldofwarships.ru/topic/49876-tachibana-ii-0516x/'
# PJSD017	japan	Destroyer	5	4277024464	Fūjin
ships_add['4277024464'] = 'https://forum.worldofwarships.ru/topic/83706-kamikazef%C5%ABijin-v-063/'
# PJSD026	japan	Destroyer	5	4267587280	Kamikaze R
ships_add['4267587280'] = 'https://forum.worldofwarships.ru/topic/83706-kamikazef%C5%ABijin-v-063/'
# PJSD208	japan	Destroyer	8	4076746448	Kagero
ships_add['4076746448'] = 'https://forum.worldofwarships.ru/topic/104094-%D0%BA%D0%B0%D0%B3%D0%B5%D1%80%D0%BE-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-%D1%8F%D0%BF%D0%BE%D0%BD%D0%B8%D0%B8-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-%D0%BD%D0%B8%D0%BD%D0%B4%D0%B7%D1%8F-%D0%B1%D0%BE%D1%8F%D1%80%D0%B8%D0%BD-070%D1%85/'
# PJSD209	japan	Destroyer	9	4075697872	Yūgumo
ships_add['4075697872'] = 'https://forum.worldofwarships.ru/topic/104037-yugumo-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-9-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072%D1%85/'
# PJSD518	japan	Destroyer	8	3751687888	Asashio
ships_add['3751687888'] = ''
# PJSD912	japan	Destroyer	10	3338548944	[Shimakaze]
ships_add['3338548944'] = 'https://forum.worldofwarships.ru/topic/54188-shimakaze-%D1%8F%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-%D1%85-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-055x/'
# PRSB505	ussr	Battleship	5	3765384656	Окт. революция
ships_add['3765384656'] = 'https://forum.worldofwarships.ru/topic/91769-%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA%D0%B0%D1%8F-%D1%80%D0%B5%D0%B2%D0%BE%D0%BB%D1%8E%D1%86%D0%B8%D1%8F-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D1%80-v-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PRSC010	ussr	Cruiser	2	4284397008	Диана L
ships_add['4284397008'] = 'https://forum.worldofwarships.ru/topic/78492-%D0%B4%D0%B8%D0%B0%D0%BD%D0%B0-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-%D1%80%D0%B8%D1%84-ii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-072x/'
# PRSC109	ussr	Cruiser	9	4180587984	Дм. Донской
ships_add['4180587984'] = 'https://forum.worldofwarships.ru/topic/66766-%D0%B4%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B9-%D0%B4%D0%BE%D0%BD%D1%81%D0%BA%D0%BE%D0%B9-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-ix-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PRSC910	ussr	Cruiser	10	3340678608	[Москва]
ships_add['3340678608'] = 'https://forum.worldofwarships.ru/topic/62244-%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0-%D1%82%D1%8F%D0%B6%D1%91%D0%BB%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PRSD105	ussr	Destroyer	5	4184749520	Гневный (OLD)
ships_add['4184749520'] = 'https://forum.worldofwarships.ru/topic/84248-%D0%B3%D0%BD%D0%B5%D0%B2%D0%BD%D1%8B%D0%B9-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-070/'
# PRSD106	ussr	Destroyer	6	4183700944	Огневой (OLD)
ships_add['4183700944'] = 'https://forum.worldofwarships.ru/topic/82047-%D0%BE%D0%B3%D0%BD%D0%B5%D0%B2%D0%BE%D0%B9-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-%D1%85%D0%BE%D1%80%D0%BE%D1%88%D0%B0%D1%8F-%D1%88%D0%BB%D1%8E%D0%BF%D0%BA%D0%B0-0614%D1%85/'
# PRSD108	ussr	Destroyer	8	4181603792	Ташкент (OLD)
ships_add['4181603792'] = 'https://forum.worldofwarships.ru/topic/83839-%D1%82%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82-%E2%80%93-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-ix-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-068/'
# PRSD109	ussr	Destroyer	7	4180555216	Киев (OLD)
ships_add['4180555216'] = 'https://forum.worldofwarships.ru/topic/83067-%D0%BA%D0%B8%D0%B5%D0%B2-%E2%80%93-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-066/'
# PRSD910	ussr	Destroyer	10	3340645840	[Грозовой]
ships_add['3340645840'] = 'https://forum.worldofwarships.ru/topic/81697-%D0%B3%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D0%BE%D0%B9-%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-x-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F%D1%81%D1%82%D0%B0%D1%80%D1%82%D0%BE%D0%B2%D0%B0%D1%8F/'
# PWSD501	poland	Destroyer	7	3769513264	Błyskawica
ships_add['3769513264'] = 'https://forum.worldofwarships.ru/topic/73717-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D0%BE%D0%BC%D1%83-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D1%86%D1%83-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-blyskawica-065/'
# PZSD508	pan_asia	Destroyer	8	3762173136	Loyang
ships_add['3762173136'] = 'https://forum.worldofwarships.ru/topic/66511-lo-yang-%D0%BF%D1%80%D0%B5%D0%BC%D0%B8%D1%83%D0%BC%D0%BD%D1%8B%D0%B9-%D1%8D%D1%81%D0%BC%D0%B8%D0%BD%D0%B5%D1%86-%D0%BF%D0%B0%D0%BD-%D0%B0%D0%B7%D0%B8%D0%B8-8-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-%D1%88%D1%85%D1%83%D0%BD%D0%B0-%D0%BD%D1%83%D0%B2%D0%BE%D1%80%D0%B8%D1%88%D0%B0-061/'
# PASA015	usa	AirCarrier	10	4279220208	Midway	http://wiki.wargaming.net/ru/Ship:Midway4279220208
ships_add['4279220208'] = 'https://forum.worldofwarships.ru/forum/425-midway/'
# PASC004	usa	Cruiser	3	4290689008	St. Louis	http://wiki.wargaming.net/ru/Ship:St. Louis
ships_add['4290689008'] = 'https://forum.worldofwarships.ru/topic/57802-st-louis-iii-0515x/'
# PASC007	usa	Cruiser	6	4287543280	Cleveland (old)	http://wiki.wargaming.net/ru/Ship:Cleveland (old)
ships_add['4287543280'] = 'https://forum.worldofwarships.ru/topic/33765-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vi-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-cleveland/'
# PASC012	usa	Cruiser	7	4282300400	Pensacola (old)	http://wiki.wargaming.net/ru/Ship:Pensacola (old)
ships_add['4282300400'] = 'https://forum.worldofwarships.ru/topic/65733-uss-pensacola-%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-vii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-069x/'
# PASC014	usa	Cruiser	8	4280203248	New Orleans (old)	http://wiki.wargaming.net/ru/Ship:New Orleans (old)
ships_add['4280203248'] = 'https://forum.worldofwarships.ru/topic/37925-new-orleans-%D1%82%D1%8F%D0%B6%D1%91%D0%BB%D1%8B%D0%B9-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80-viii-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-06151/'
# PASC017	usa	Cruiser	9	4277057520	Baltimore (old)	http://wiki.wargaming.net/ru/Ship:Baltimore (old)
ships_add['4277057520'] = 'https://forum.worldofwarships.ru/topic/73372-%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BF%D0%BE-%D1%82%D1%8F%D0%B6%D0%B5%D0%BB%D0%BE%D0%BC%D1%83-%D0%BA%D1%80%D0%B5%D0%B9%D1%81%D0%B5%D1%80%D1%83-ix-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-uss-baltimore-065/'
# PASD013	usa	Destroyer	10	4281219056	Gearing	http://wiki.wargaming.net/ru/Ship:Gearing
ships_add['4281219056'] = 'https://forum.worldofwarships.ru/forum/414-gearing/'
# PBSB110	uk	Battleship	10	4179572688	Conqueror	http://wiki.wargaming.net/ru/Ship:Conqueror
ships_add['4179572688'] = 'https://forum.worldofwarships.ru/forum/421-conqueror/'

for ship_id in ships_add:
    ship = ships[ship_id]
    ship_name = tr.gettext('IDS_' + ship['id_str']).decode('utf8')
    if ship_id not in links and ships_add[ship_id]:
        links[ship_id] = {
            "ship_id": ship_id,
            "id_str": ship['id_str'],
            "nation": ship['nation'],
            "tier": ship['tier'],
            "type": ship['type'],
            "ship_name": ship_name,
            "title": u"Форум",
            "url": ships_add[ship_id],
        }


newlist = sorted(links.values(), key=lambda k: k['id_str'])
with open('out\\links.json', 'w') as outfile:
    json.dump(newlist, outfile, encoding='utf8', indent=2, sort_keys=True)
