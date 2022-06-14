from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")
