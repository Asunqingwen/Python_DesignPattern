from DecoraterPattern.BaseBeverage import Espresso, DarkRoast, HouseBlend
from DecoraterPattern.CondimentDecorator import Mocha, Whip, Soy

if __name__ == '__main__':
    baseBeverage = Espresso()
    print(baseBeverage.getDescription() + " $" + baseBeverage.cost().__str__())

    baseBeverage1 = DarkRoast()
    baseBeverage1 = Mocha(baseBeverage1)
    baseBeverage1 = Mocha(baseBeverage1)
    baseBeverage1 = Whip(baseBeverage1)
    print(baseBeverage1.getDescription() + " $" + baseBeverage1.cost().__str__())

    baseBeverage2 = HouseBlend()
    baseBeverage2 = Soy(baseBeverage2)
    baseBeverage2 = Mocha(baseBeverage2)
    baseBeverage2 = Whip(baseBeverage2)
    print(baseBeverage2.getDescription() + " $" + baseBeverage2.cost().__str__())
