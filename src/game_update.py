# -*- coding: utf-8 -*-
import subprocess

python = 'C:\\Python27\\python.exe'

subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Wiki.ru'
)
subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Wiki.ru'
)
subprocess.run(
    [python, 'parser.py'],
    shell=True,
    cwd='Forum.ru'
)
subprocess.run(
    [python, 'makehtml.py'],
    shell=True,
    cwd='Forum.ru'
)
subprocess.run(
    [python, 'make_links.py'],
    shell=True,
    cwd='.'
)
