class MyFlags:
    def __init__(self):
        self._flags = []

    def setFlags(self, flags):
        self._flags = flags

    def createFlashFlags(self):
        for flagSet in self._flags:
            flash.call('HelpMe.CREATE_FLAG_SET', [flagSet['id']])
            for hint in flagSet["hints"]:
                flash.call('HelpMe.ADD_FLAG_HINT', [flagSet['id'], hint["type"], hint["col"], hint["row"]])
