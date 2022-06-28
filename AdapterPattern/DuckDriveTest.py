from DuckClass import MallardDuck
from TurkeyClass import WildTurkey
from TurkeyAdapterClass import TurkeyAdapter


def testDuck(duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    duck = MallardDuck()

    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)

    print("The Turkey says......")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    testDuck(duck)

    testDuck(turkeyAdapter)
