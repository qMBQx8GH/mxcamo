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
        'wowsunpack.exe', '-x',
        '-I', d, os.path.join(path_to_game, 'res_packages'),
        '-o', 'res'],
            shell=True,
    )
    print(d, 'OK')

os.makedirs('tmp', exist_ok=True)
mo_file('gp', 'res\\content\\GameParams.data', 'tmp\\GameParams.json')

info = {}
f = open('tmp\\GameParams.json')
data = json.load(f)
f.close()
for unit_id in data:
    unit = data[unit_id]
    if unit['typeinfo']['type'] == 'Exterior' and unit['typeinfo']['species'] == 'Camouflage':
        info[unit_id] = unit
    elif unit['typeinfo']['type'] == 'Exterior' and unit['typeinfo']['species'] == 'Permoflage':
        info[unit_id] = unit
    else:
        pass

with open('db\\data.json', 'w') as outfile:
    json.dump(info, outfile, sort_keys=True, indent='  ')
