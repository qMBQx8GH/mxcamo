import Keys
import menu
import flags

API_VERSION = 'API_v1.0'
MOD_NAME = 'HelpMe'


class HelpMe:
    def __init__(self):
        self.disabled = False
        self.currentId = ''
        self.menu = menu.MyMenu()
        self.flags = flags.MyFlags()
        self.setupEvents()

    def setupEvents(self):
        events.onFlashReady(self.onFlashReady)
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)
        events.onKeyEvent(self.onKeyEvent)

    def onFlashReady(self, modName):
        if modName == MOD_NAME:
            with open(utils.getModDir() + '/menu.json', 'r') as menuFile:
                menuData = menuFile.read()
            self.menu.setMenu(utils.jsonDecode(menuData))
            self.menu.createFlashMenu()
            with open(utils.getModDir() + '/flags.json', 'r') as flagsFile:
                flagsData = flagsFile.read()
            self.flags.setFlags(utils.jsonDecode(flagsData))
            self.flags.createFlashFlags()

    def onBattleStart(self):
        self.disabled = True
        self.menu.showFlashMenu(self.currentId, False)
        self.currentId = ''

    def onBattleQuit(self, arg):
        self.disabled = False

    def onKeyEvent(self, event):
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
