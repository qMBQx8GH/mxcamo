#from API_v_1_0 import *
import ini
import menu
import flags
import perks

API_VERSION = 'API_v1.0'
MOD_NAME = 'HelpMe'


class HelpMe:
    def __init__(self):
        self.disabled = False
        self.currentId = ''
        self.menu = menu.MyMenu()
        self.flags = flags.MyFlags()
        self.perks = perks.MyPerks()
        self.setupEvents()

    def setupEvents(self):
        events.onFlashReady(self.onFlashReady)
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)
        events.onKeyEvent(self.onKeyEvent)

    def onFlashReady(self, modName):
        if modName == MOD_NAME:
            iniFile = ini.MyIniFile(utils.getModDir() + '/helpme.ini')
            iniDir = iniFile.get('dir')
            if iniDir:
                with open(utils.getModDir() + '/' + iniDir + '/menu.json', 'r') as menuFile:
                    menuData = menuFile.read()
                self.menu.setMenu(utils.jsonDecode(menuData))
                self.menu.createFlashMenu()

                with open(utils.getModDir() + '/' + iniDir + '/flags.json', 'r') as flagsFile:
                    flagsData = flagsFile.read()
                self.flags.setFlags(utils.jsonDecode(flagsData))
                self.flags.createFlashFlags()

                with open(utils.getModDir() + '/' + iniDir + '/perks.json', 'r') as perksFile:
                    perksData = perksFile.read()
                self.perks.setPerks(utils.jsonDecode(perksData))
                self.perks.createFlashPerks()

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
            if event.isCtrlDown():
                self.Reload()
            elif self.currentId == '':
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

    def Reload(self):
        self.menu.showFlashMenu(self.currentId, False)
        self.onFlashReady(MOD_NAME)
        self.menu.showFlashMenu(self.currentId, True)

g_HelpMe = HelpMe()
