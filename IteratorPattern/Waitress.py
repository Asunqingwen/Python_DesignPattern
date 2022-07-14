class Waitress:

    def __init__(self, dinerMenu, cafeMenu):
        self._dinerMenu = dinerMenu
        self._cafeMenu = cafeMenu

    def printMenu(self):
        dinerIterator = self._dinerMenu.createIterator()
        cafeIterator = self._cafeMenu.createIterator()
        print("\nLUNCH")
        self.__printMenu(dinerIterator)
        print("\nDINNER")
        self.__printMenu(cafeIterator)

    def __printMenu(self, iterator):
        for iter in iterator:
            print(iter.getName().__str__() + ", ")
            print(iter.getPrice().__str__() + " -- ")
            print(iter.getDescription())
