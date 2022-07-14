class Waitress:
    def __init__(self, allMenus):
        self._allMenus = allMenus

    def printMenu(self):
        self._allMenus.print()

    def printVegetarianMenu(self):
        iterator = self._allMenus.createIterator()
        print("\nVEGETARIAN MENU\n----")
        try:
            menuComponent = iterator.next()
            if menuComponent.isVegetarian():
                menuComponent.print()
        except StopIteration:
            pass
