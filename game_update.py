# -*- coding: utf-8 -*-

import os
import json
import requests
import subprocess
import xml.etree.ElementTree as ET
import configparser

config = configparser.ConfigParser()
config.read('build.ini')
path_to_game = config['Game']['folder']

xml_root = ET.parse(os.path.join(path_to_game, 'game_info.xml'))
xml_version = xml_root.findall(".//version[@name='client']")
version = xml_version[0].attrib['installed']


def mo_file(t, src, trg):
    files = [
        (t, (os.path.basename(src), open(src, 'rb'), 'application/octet-stream')),
    ]
    response = requests.post('https://mv-smirnov.org/py/', files=files)
    if response.status_code != 200:
        print('response.status_code', response.status_code)
        exit(1)
    print(trg, 'OK')
    with open(trg, 'wb') as out:
        response.raw.decode_content = True
        for chunk in response.iter_content(chunk_size=128):
            out.write(chunk)
    out.close()


content = [
    'gui/camouflages/*.*',
    'gui/permoflages/*.*',
    'content/GameParams.data',
]
for d in content:
    subprocess.run([
        'wowsunpack.exe',
        '-x', os.path.join(path_to_game, "bin", version.split(".")[-1], "idx"),
        '-I', d,
        '-p', '..\\..\\..\\res_packages',
        '-o', 'res',
    ],
        shell=True,
    )
    print(d, 'OK')

os.makedirs('tmp', exist_ok=True)
mo_file('gp', 'res\\content\\GameParams.data', 'tmp\\GameParams.json')

info = []
f = open('tmp\\GameParams.json')
data = json.load(f)
f.close()
for unit_id, unit in data[0].items():
    if unit is not None and 'typeinfo' in unit:
        typeinfo = unit['typeinfo']
        if typeinfo['type'] == 'Exterior':
            if typeinfo['species'] == 'Camouflage' or typeinfo['species'] == 'Permoflage':
                info.append({
                    'name': unit['name'],
                    'typeinfo': unit['typeinfo'],
                    'modifiers': unit['modifiers'],
                })

with open('db\\data.json', 'w') as outfile:
    json.dump(info, outfile, sort_keys=True, indent='  ')
