class MyLinks:
    def __init__(self):
        self._links = []
        self._link_menus = {}

    def setLinks(self, links):
        self._links = links
        self._link_menus = {}

    def createFlashLinks(self, ship_id):
        if ship_id in self._link_menus:
            return
        print self._links
        for link in self._links:
            if link['ship_id'] == ship_id:
                if ship_id not in self._link_menus:
                    flash.call('HelpMe.CREATE_MENU', [ship_id, ship_id])
                    self._link_menus[ship_id] = {}
                if link['url'] not in self._link_menus[ship_id]:
                    i = len(self._link_menus[ship_id]) + 1
                    title = link['title']
                    id = ship_id + '[' + str(i) + ']'
                    flash.call('HelpMe.ADD_MENU_ITEM', [ship_id, title, id])
                    flash.call('HelpMe.CREATE_QR_CODE', [id, 10, 350, link['url']])
                    self._link_menus[ship_id][link['url']] = id
        print self._link_menus
