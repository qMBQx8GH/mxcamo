import Keys
import menu

API_VERSION = 'API_v1.0'
MOD_NAME = 'HelpMe'


class HelpMe:
    def __init__(self):
        self.disabled = False
        self.currentId = ''
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)
        events.onKeyEvent(self.onKey)
        with open(utils.getModDir() + '/menu.json', 'r') as menuFile:
            menuData = menuFile.read()
        self.menu = menu.MyMenu(utils.jsonDecode(menuData))
        events.onFlashReady(self.onFlashReady)

    def onFlashReady(self, modName):
        if modName == MOD_NAME:
            self.menu.createFlashMenu()

    def onBattleStart(self):
        self.disabled = True
        self.menu.showFlashMenu(self.currentId, False)
        self.currentId = ''

    def onBattleQuit(self, arg):
        self.disabled = False

    def onKey(self, event):
        if self.disabled:
            return
        if not event.isKeyDown():
            return

        if self.menu.checkMainKey(event.key):
            if self.currentId == '':
                self.menu.showFlashMenu()
                self.currentId = self.menu.getMainId()
            else:
                self.menu.showFlashMenu(self.currentId, False)
                self.currentId = ''
        else:
            newId = self.menu.getNewId(self.currentId, event.key)
            if newId:
                self.menu.showFlashMenu(self.currentId, False)
                self.currentId = newId
                self.menu.showFlashMenu(self.currentId, True)


g_HelpMe = HelpMe()
