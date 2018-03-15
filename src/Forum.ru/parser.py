# -*- coding: UTF-8 -*-
import os
import json
import requests
import HTMLParser
import gettext

os.environ["LANGUAGE"] = 'ru'
tr = gettext.translation('global', 'C:\\Games\\World_of_Warships\\res\\texts')

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
        self.in_list2 = 0
        self.all_links = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            self.ul += 1

        if tag == 'span':
            self.span += 1

        if tag == 'ul':
            for attr in attrs:
                if attr[0] == 'class' and attr[1].startswith('ipsDataItem_subList'):
                    self.in_list = self.ul

        if tag == 'span':
            for attr in attrs:
                if attr[0] == 'class' and attr[1].startswith('ipsType_break'):
                    self.in_list2 = self.span

        if tag == 'a' and self.in_list > 0 and self.in_list == self.ul:
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

        if tag == 'a' and self.in_list2:
            title = ''
            href = ''
            for attr in attrs:
                if attr[0] == 'title':
                    title = attr[1]
                if attr[0] == 'href':
                    href = attr[1]
            if title:
                self.all_links[href] = title

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.ul -= 1
            self.in_list = 0
        if tag == 'span':
            self.span -= 1
            self.in_list2 = 0

links = {}

mainPage = requests.get('https://forum.worldofwarships.ru/forum/155-%D0%BA%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D0%B8-%D0%B2-%D0%B8%D0%B3%D1%80%D0%B5/')
parser = MyHTMLParser()
parser.feed(mainPage.content.decode(mainPage.encoding))
print parser.links

for link in parser.links:
    print '-------------link-------------- ' + link
    page = requests.get(link)
    parser = MyHTMLParser()
    parser.feed(page.content.decode(page.encoding))
    for url in parser.all_links:
        title  = parser.all_links[url]
        for ship_id in ships:
            ship = ships[ship_id]
            ship_name = tr.gettext('IDS_' + ship['id_str']).decode('utf8')
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
                print ['found!', ship_id, ship_name, url]

newlist = sorted(links.values(), key=lambda k: k['id_str'])
with open('out\\links.json', 'w') as outfile:
    json.dump(newlist, outfile, encoding='utf8', indent=2, sort_keys=True)
