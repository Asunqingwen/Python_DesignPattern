from abc import ABC, abstractmethod

from IteratorPattern.Iterator import DinerMenuIterator


class Menu(ABC):
    @abstractmethod
    def createIterator(self):
        pass


class MenuItem:
    def __init__(self, name=None, description=None, vegetarian=None, price=None):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def getPrice(self):
        return self._price

    def isVegetarian(self):
        return self._vegetarian


class DinerMenu(Menu):
    MAX_ITEMS = 6
    numberOfItems = 0

    def __init__(self):
        self._menuItems = [None] * self.MAX_ITEMS
        self.__addItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.__addItem("BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.__addItem("Soup of the day", "Soup of the day,with a side of potato salad", False, 3.29)
        self.__addItem("Hot dog", "A hot dog,with saurkraut,relish,onions,topped with cheese", False, 3.05)

    def __addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        if (self.numberOfItems >= self.MAX_ITEMS):
            print("Sorry,menu is full! Can't add item to menu")
        else:
            self._menuItems[self.numberOfItems] = menuItem
            self.numberOfItems = self.numberOfItems + 1

    def createIterator(self):
        return DinerMenuIterator(self._menuItems)


class CafeMenu(Menu):
    def __init__(self):
        self._menuItems = dict()
        self.__addItem("Veggie Burger and Air Fires", "Veggie burger on a whole wheat bun, lettuce,tomato,and fries",
                       True, 3.99)
        self.__addItem("Soup of the day", "A cup of the soup of the day,with a side salad", False, 3.69)
        self.__addItem("Burrito", "A large burrito, with whole pinto beans,salsa,guacamole", True, 4.29)

    def __addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self._menuItems[menuItem.getName()] = menuItem

    def createIterator(self):
        return iter(self._menuItems.values())
