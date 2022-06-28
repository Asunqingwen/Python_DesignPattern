from DuckClass import Duck


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        for _ in range(5):
            self._turkey.fly()
