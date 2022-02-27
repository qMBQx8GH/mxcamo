# mxcamo

1. Требуется python 3.X, git и 7zip
2. Склонировать репозиторий
```git clone https://github.com/qMBQx8GH/mxcamo```
3. Перейти в папку mxcamo
```cd mxcamo```
4. Установить зависимости
```python -m pip install -r requirements.txt```
5. Скопировать и настроить build.ini
```cp build.ini.dist build.ini```
6. Скопировать файлы из ресурсов игры
```python game_update.py```
7. Создать модифицированные файлы
```python make_icons.py```
8. Создать архив с модом для распаковки в папке с игрой
```build.cmd```
