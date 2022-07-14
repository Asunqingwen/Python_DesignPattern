from abc import ABC, abstractmethod


class IteratorOuter:
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def __remove__(self):
        pass


class DinerMenuIterator(IteratorOuter):
    position = 0

    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return self

    def __next__(self):
        if self._items[self.position]:
            menuItem = self._items[self.position]
            self.position = self.position + 1
            return menuItem
        raise StopIteration

    def __remove__(self):
        if self.position <= 0:
            raise IndexError("You can't remove an item until you've done at least one next()")
        self._items[self.position - 1:len(self._items) - 1] = self._items[self.position:len(self._items)]
