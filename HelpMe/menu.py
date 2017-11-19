import Keys


class MyMenu:
    def __init__(self):
        self._menu = {}
        self._key_map = {
            'H': Keys.KEY_H,
            '1': Keys.KEY_1,
            '2': Keys.KEY_2,
            '3': Keys.KEY_3,
            '4': Keys.KEY_4,
            '5': Keys.KEY_5,
            '6': Keys.KEY_6,
            '7': Keys.KEY_7,
            '8': Keys.KEY_8,
            '9': Keys.KEY_9,
            '0': Keys.KEY_0,
        }

    def setMenu(self, menu):
        self._menu = menu

    def createFlashMenu(self):
        self._create_menu(self._menu)
        #print self._menu

    def showFlashMenu(self, id='', show=True):
        if not id:
            id = self._menu['id']
        flash.call('HelpMe.SHOW_MENU', [id, show])

    def getMainId(self):
        return self._menu['id']

    def checkMainKey(self, keyCode):
        if 'key' in self._menu:
            if keyCode == self._menu['key']:
                return True
        return False

    def getNewId(self, currentId, keyCode):
        menu = self._find_menu(currentId, self._menu)
        if menu and ('items' in menu):
            for menuItem in menu['items']:
                if ('key' in menuItem) and (keyCode == menuItem['key']):
                    return menuItem['id']
        return ''

    def _find_menu(self, id, menu):
        if menu["id"] == id:
            return menu
        if 'items' in menu:
            for menuItem in menu['items']:
                subMenu = self._find_menu(id, menuItem)
                if subMenu:
                    return subMenu
        return None

    def _create_menu(self, menu):
        # accelerator key
        self._add_accelerator_key(menu)
        # create flash object
        flash.call('HelpMe.CREATE_MENU', [menu['id'], menu['itemsTitle']])
        for menuItem in menu['items']:
            #accelerator key
            self._add_accelerator_key(menuItem)
            #flash item
            flash.call('HelpMe.ADD_MENU_ITEM', [menu['id'], menuItem['title'], menuItem['id']])
            #add submenu
            if 'items' in menuItem:
                self._create_menu(menuItem)

    def _add_accelerator_key(self, menuItem):
        if 'title' in menuItem:
            keyPos = menuItem['title'].find('&')
            if keyPos >= 0:
                keyChar = menuItem['title'][keyPos + 1]
                keyCode = self._key_translate(keyChar)
                if keyCode >= 0:
                    menuItem['key'] = keyCode

    def _key_translate(self, char):
        if char in self._key_map:
            return self._key_map[char]
        else:
            return -1
