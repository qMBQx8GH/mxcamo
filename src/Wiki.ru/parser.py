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

newlist = sorted(links.values(), key=lambda k: k['id_str'])
with open('out\\links.json', 'w') as outfile:
    json.dump(newlist, outfile, encoding='utf8', indent=2, sort_keys=True)
