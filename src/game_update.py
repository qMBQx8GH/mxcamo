# -*- coding: utf-8 -*-
import subprocess

python = 'C:\\Python27\\python.exe'

res = subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Wiki.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Wiki.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Forum.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Forum.ru'
)
if res.returncode != 0:
    exit(1)

res = subprocess.run(
    [python, 'make_links.py'],
    shell=True,
    cwd='.'
)
if res.returncode != 0:
    exit(1)