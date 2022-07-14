from abc import ABC, abstractmethod

import CompositeIterator, NullIterator


class MenuComponent(ABC):
    def add(self, menuComponent):
        raise Exception

    def remove(self, menuComponent):
        raise Exception

    def getChild(self, i):
        raise Exception

    def getName(self):
        raise Exception

    def getDescription(self):
        raise Exception

    def getPrice(self):
        raise Exception

    def isVegetarian(self):
        raise Exception

    def print(self):
        raise Exception

    def createIterator(self):
        return None


class Menu(MenuComponent):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._menuComponents = list()

    def add(self, menuComponent):
        self._menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self._menuComponents.remove(menuComponent)

    def getChild(self, i):
        return self._menuComponents[i]

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def print(self):
        print("\n" + self.getName() + ", " + self.getDescription())
        print("---------------------")

        for component in self._menuComponents:
            component.print()

    def createIterator(self):
        return CompositeIterator(iter(self._menuComponents))


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
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

    def print(self):
        if self.isVegetarian():
            print(" " + self.getName() + "(v), " + self.getPrice().__str__())
        else:
            print(" " + self.getName() + ", " + self.getPrice().__str__())
        print("     --" + self.getDescription())

    def createIterator(self):
        return NullIterator()
