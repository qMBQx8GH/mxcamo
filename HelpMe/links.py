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
        for link in self._links:
            if link['ship_id'] == ship_id:
                if ship_id not in self._link_menus \
                        and 'ship_name' in link:
                    flash.call('HelpMe.CREATE_MENU', [ship_id, link['ship_name']])
                    self._link_menus[ship_id] = {}
                if ship_id in self._link_menus \
                        and link['url'] not in self._link_menus[ship_id] \
                        and 'title' in link:
                    i = len(self._link_menus[ship_id]) + 1
                    title = link['title']
                    id = ship_id + '[' + str(i) + ']'
                    flash.call('HelpMe.ADD_MENU_ITEM', [ship_id, title, id])
                    flash.call('HelpMe.CREATE_QR_CODE', [id, 510, 100, link['url']])
                    self._link_menus[ship_id][link['url']] = id
