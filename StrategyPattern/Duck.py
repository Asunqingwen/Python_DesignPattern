class Duck:

    def __init__(self, qb, fb):
        self._quackBehavior = qb
        self._flyBehavior = fb

    # 算法设置
    @property
    def quackBehavior(self):
        return self._quackBehavior

    @quackBehavior.setter
    def quackBehavior(self, qb):
        self._quackBehavior = qb

    @property
    def flyBehavior(self):
        return self._flyBehavior

    @flyBehavior.setter
    def flyBehavior(self, fb):
        self._flyBehavior = fb

    # 执行具体算法
    def performFly(self):
        self._flyBehavior.fly()

    def performQuack(self):
        self._quackBehavior.quack()

    def display(self):
        pass

    def swim(self):
        print("All ducks float,even decoys!")


class MallardDuck(Duck):
    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def display(self):
        print("I'm a model duck")
