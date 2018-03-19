# -*- coding: UTF-8 -*-
import json
import re

links = []

with open('Wiki.ru\\out\\links.json') as f:
    ships = json.load(f)
    for ship in ships:
        links.append({
            "ship_id": ship["ship_id"],
            "url": ship["url"],
            "title": ship["title"],
            "ship_name":  ship["ship_name"],
        })

r = re.compile('(https://forum\\.worldofwarships\\.ru/topic/[0-9]+-)', )
with open('Forum.ru\\out\\links.json') as f:
    ships = json.load(f)
    for ship in ships:
        rg = r.match(ship["url"])
        if rg:
            url = rg.group(1)
        else:
            url = ship["url"]
        links.append({
            "ship_id": ship["ship_id"],
            "url": url,
            "title": ship["title"],
        })

with open('..\\HelpMe\\ru\\links.json', 'w') as outfile:
    json.dump(links, outfile, encoding='utf8', indent=2, sort_keys=True)