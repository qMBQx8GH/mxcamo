# -*- coding: UTF-8 -*-
import json
import requests
import urllib

f = open('Wiki.ru\\out\\links.json')
wiki = json.load(f)
f.close()

f = open('Forum.ru\\out\\links.json')
forum = json.load(f)
f.close()

for w in wiki:
    found = False
    for f in forum:
        if w["ship_id"] == f["ship_id"]:
            found = True
    if not found:
        print 'missing forum link for ', w["ship_id"], urllib.unquote(w['url'].encode('utf8'))

with open('..\\HelpMe\\ru\\links.json') as f:
    links = json.load(f)
    for link in links:
        r = requests.get(link["url"])
        if r.status_code != 200:
            print r.status_code, link["ship_id"], urllib.unquote(link['url'].encode('utf8'))
