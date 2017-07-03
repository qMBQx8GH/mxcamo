class MyPerks:
    def __init__(self):
        self._perks = []

    def setPerks(self, perks):
        self._perks = perks

    def createFlashPerks(self):
        for perkSet in self._perks:
            flash.call('HelpMe.CREATE_PERK_SET', [perkSet['id']])
            for perk in perkSet["perks"]:
                flash.call('HelpMe.ADD_PERK', [perkSet['id'], perk[0], perk[1], perk[2]])
