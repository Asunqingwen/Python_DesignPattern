from abc import abstractmethod


class BaseBeverage:
    description = "Unknown BaseBeverage"

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class DarkRoast(BaseBeverage):

    def __init__(self):
        self.description = "DarkRoast"

    def cost(self):
        return .99


class Decat(BaseBeverage):

    def __init__(self):
        self.description = "Decat"

    def cost(self):
        return 1.05


class Espresso(BaseBeverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(BaseBeverage):

    def __init__(self):
        self.description = "HouseBlend"

    def cost(self):
        return .89
