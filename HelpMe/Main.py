#from API_v_1_0 import *
import ini
import menu
import flags
import perks
import links

API_VERSION = 'API_v1.0'
MOD_NAME = 'HelpMe'


class HelpMe:
    def __init__(self):
        self.disabled = False
        self.currentId = ''
        self.menu = menu.MyMenu()
        self.flags = flags.MyFlags()
        self.perks = perks.MyPerks()
        self.links = links.MyLinks()
        self.setupEvents()

    def setupEvents(self):
        events.onFlashReady(self.onFlashReady)
        events.onBattleStart(self.onBattleStart)
        events.onBattleQuit(self.onBattleQuit)
        events.onKeyEvent(self.onKeyEvent)
        flash.addExternalCallback('HelpMe.MENU_ITEM_CLICKED', self.onMenuItemClick)

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

                with open(utils.getModDir() + '/' + iniDir + '/links.json', 'r') as linksFile:
                    linksData = linksFile.read()
                    self.links.setLinks(utils.jsonDecode(linksData))

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
            elif event.isAltDown():
                flash.reloadMod(MOD_NAME)
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
                newMenu = self.menu.getById(newId)
                if newMenu and 'links' in newMenu and newMenu['links']:
                    newId = self.getCurrentShipId()
                    self.links.createFlashLinks(newId)
                self.currentId = newId
                self.menu.showFlashMenu(self.currentId, True)

    def onMenuItemClick(self, _unknown_zero_, newId):
        self.menu.showFlashMenu(self.currentId, False)
        newMenu = self.menu.getById(newId)
        if newMenu and 'links' in newMenu and newMenu['links']:
            newId = self.getCurrentShipId()
            self.links.createFlashLinks(newId)
        self.currentId = newId
        self.menu.showFlashMenu(self.currentId, True)

    def Reload(self):
        self.menu.showFlashMenu(self.currentId, False)
        self.onFlashReady(MOD_NAME)
        self.menu.showFlashMenu(self.currentId, True)

    def xmlCut(self, str, tag):
        result = ''
        open_tag_start = str.find('<' + tag)
        if open_tag_start >= 0:
            open_tag_end = str.find('>', open_tag_start)
            if open_tag_end >= 0:
                end_tag_start = str.find('</' + tag, open_tag_end)
                if end_tag_start >= 0:
                    result = str[open_tag_end + 1:end_tag_start]
        return result

    def getCurrentShipId(self):
        with open(utils.getModDir() + '\\..\\..\\..\\..\\preferences.xml', 'r') as prefsFile:
            prefsData = prefsFile.read()
            lobby_values = self.xmlCut(prefsData, 'lobby_values')
            ship = self.xmlCut(lobby_values, 'ship')
            return ship.strip()
        return ''

g_HelpMe = HelpMe()
