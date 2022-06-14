from Duck import MallardDuck, ModelDuck
from StrategyPattern.FlyBehavior import FlyWithWings, FlyNoWay, FlyRocketPowered
from StrategyPattern.QuackBehavior import Quack

if __name__ == '__main__':
    mallard = MallardDuck(Quack(), FlyWithWings())
    mallard.performQuack()
    mallard.performFly()

    model = ModelDuck(Quack(), FlyNoWay())
    model.performFly()
    model.flyBehavior = FlyRocketPowered()
    model.performFly()
