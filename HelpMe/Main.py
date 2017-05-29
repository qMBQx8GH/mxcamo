import Keys
import time

API_VERSION = 'API_v1.0'
MOD_NAME = 'HelpMe'


# print 'HelpMe.py loaded'


class HelpMe:
    CHANGE_STATE = "HelpMe.changeState"
    SHOW_MAIN_MENU = "HelpMe.showMainMenu"
    SHOW_FLAG_MENU = "HelpMe.showFlagMenu"
    SHOW_FLAG_HINT_CV = "HelpMe.showFlagHintCV"
    SHOW_FLAG_HINT_BB = "HelpMe.showFlagHintBB"
    SHOW_FLAG_HINT_CA = "HelpMe.showFlagHintCA"
    SHOW_FLAG_HINT_DD = "HelpMe.showFlagHintDD"
    SHOW_PERK_MENU = "HelpMe.showPerkMenu"
    SHOW_PERK_MENU_CV = "HelpMe.showPerkMenuCV"
    SHOW_PERK_MENU_BB = "HelpMe.showPerkMenuBB"
    SHOW_PERK_MENU_CA = "HelpMe.showPerkMenuCA"
    SHOW_PERK_MENU_DD = "HelpMe.showPerkMenuDD"
    SHOW_PERK_HINT_TEST = "HelpMe.showPerkHintTest"
    HIDE = ""
    NOT_CHANGED = "none"

    def __init__(self):
        self.state = HelpMe.HIDE
        events.onKeyEvent(self.onKey)

    def onKey(self, event):
        newState = HelpMe.NOT_CHANGED
        if event.key == Keys.KEY_H and event.isKeyDown():
            if self.state != HelpMe.HIDE:
                newState = HelpMe.HIDE
            else:
                newState = HelpMe.SHOW_MAIN_MENU
        elif event.key == Keys.KEY_1 and event.isKeyDown():
            if self.state == HelpMe.SHOW_MAIN_MENU:
                newState = HelpMe.SHOW_FLAG_MENU
            elif self.state == HelpMe.SHOW_FLAG_MENU:
                newState = HelpMe.SHOW_FLAG_HINT_CV
            elif self.state == HelpMe.SHOW_PERK_MENU:
                newState = HelpMe.SHOW_PERK_MENU_CV
            elif self.state == HelpMe.SHOW_PERK_MENU_CV\
                    or self.state == HelpMe.SHOW_PERK_MENU_BB\
                    or self.state == HelpMe.SHOW_PERK_MENU_CA\
                    or self.state == HelpMe.SHOW_PERK_MENU_DD:
                newState = self.state + 'JP'
        elif event.key == Keys.KEY_2 and event.isKeyDown():
            if self.state == HelpMe.SHOW_MAIN_MENU:
                newState = HelpMe.SHOW_PERK_MENU
            elif self.state == HelpMe.SHOW_FLAG_MENU:
                newState = HelpMe.SHOW_FLAG_HINT_BB
            elif self.state == HelpMe.SHOW_PERK_MENU:
                newState = HelpMe.SHOW_PERK_MENU_BB
            elif self.state == HelpMe.SHOW_PERK_MENU_CV \
                     or self.state == HelpMe.SHOW_PERK_MENU_BB \
                     or self.state == HelpMe.SHOW_PERK_MENU_CA \
                     or self.state == HelpMe.SHOW_PERK_MENU_DD:
                newState = self.state + 'US'
        elif event.key == Keys.KEY_3 and event.isKeyDown():
            if self.state == HelpMe.SHOW_FLAG_MENU:
                newState = HelpMe.SHOW_FLAG_HINT_CA
            elif self.state == HelpMe.SHOW_PERK_MENU:
                newState = HelpMe.SHOW_PERK_MENU_CA
            elif self.state == HelpMe.SHOW_PERK_MENU_CV \
                     or self.state == HelpMe.SHOW_PERK_MENU_BB \
                     or self.state == HelpMe.SHOW_PERK_MENU_CA \
                     or self.state == HelpMe.SHOW_PERK_MENU_DD:
                newState = self.state + 'RU'
        elif event.key == Keys.KEY_4 and event.isKeyDown():
            if self.state == HelpMe.SHOW_FLAG_MENU:
                newState = HelpMe.SHOW_FLAG_HINT_DD
            elif self.state == HelpMe.SHOW_PERK_MENU:
                newState = HelpMe.SHOW_PERK_MENU_DD
            elif self.state == HelpMe.SHOW_PERK_MENU_CV \
                    or self.state == HelpMe.SHOW_PERK_MENU_BB \
                    or self.state == HelpMe.SHOW_PERK_MENU_CA \
                    or self.state == HelpMe.SHOW_PERK_MENU_DD:
                newState = self.state + 'DE'
        elif event.key == Keys.KEY_5 and event.isKeyDown():
            if self.state == HelpMe.SHOW_PERK_MENU_CV \
                    or self.state == HelpMe.SHOW_PERK_MENU_BB \
                    or self.state == HelpMe.SHOW_PERK_MENU_CA \
                    or self.state == HelpMe.SHOW_PERK_MENU_DD:
                newState = self.state + 'GB'

        if newState != HelpMe.NOT_CHANGED and newState != self.state:
            flash.call(HelpMe.CHANGE_STATE, [self.state, False])
            self.state = newState
            flash.call(HelpMe.CHANGE_STATE, [self.state, True])


g_HelpMe = HelpMe()
