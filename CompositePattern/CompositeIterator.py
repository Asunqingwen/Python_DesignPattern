from MenuComponent import Menu


class CompositeIterator:
    stack = list()

    def __init__(self, iterator):
        self.stack.append(iterator)

    def next(self):
        try:
            iterator = self.stack[-1]
            component = iterator.next()
            if isinstance(component, Menu):
                self.stack.append(component.createIterator())
            return component
        except StopIteration:
            return None
