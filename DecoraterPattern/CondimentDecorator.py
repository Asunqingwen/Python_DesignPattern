from DecoraterPattern.BaseBeverage import BaseBeverage


class CondimentDecorator(BaseBeverage):
    def getDescription(self):
        pass


class Milk(CondimentDecorator):
    def __init__(self, baseBeverage):
        self._baseBeverage = baseBeverage

    def getDescription(self):
        return self._baseBeverage.getDescription() + ", Milk"

    def cost(self):
        return .10 + self._baseBeverage.cost()


class Mocha(CondimentDecorator):
    def __init__(self, baseBeverage):
        self._baseBeverage = baseBeverage

    def getDescription(self):
        return self._baseBeverage.getDescription() + ", Mocha"

    def cost(self):
        return .20 + self._baseBeverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, baseBeverage):
        self._baseBeverage = baseBeverage

    def getDescription(self):
        return self._baseBeverage.getDescription() + ", Soy"

    def cost(self):
        return .15 + self._baseBeverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, baseBeverage):
        self._baseBeverage = baseBeverage

    def getDescription(self):
        return self._baseBeverage.getDescription() + ", Whip"

    def cost(self):
        return .10 + self._baseBeverage.cost()
