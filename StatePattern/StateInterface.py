import time
from abc import ABC
import random


class State(ABC):
    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass


class NoQuarterState(State):

    def __init__(self, gumballMachine):
        self._gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You inserted a quarter")
        self._gumballMachine.setState(self._gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")


class HasQuarterState(State):
    random.seed(time.time())

    def __init__(self, gumballMachine):
        self._gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert another quarter")

    def ejectQuarter(self):
        print("Quarter returned")
        self._gumballMachine.setState(self._gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("You turned...")
        winner = random.randint(0, 9)
        if winner == 0 and self._gumballMachine.getCount() > 1:
            self._gumballMachine.setState(self._gumballMachine.getWinnerState())
        else:
            self._gumballMachine.setState(self._gumballMachine.getSoldState())

    def dispense(self):
        print("No gumball dispensed")


class SoldState(State):
    def __init__(self, gumballMachine):
        self._gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self._gumballMachine.releaseBall()
        if self._gumballMachine.getCount() > 0:
            self._gumballMachine.setState(self._gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self._gumballMachine.setState(self._gumballMachine.getSoldOutState())


class SoldOutState(State):
    def __init__(self, gumballMachine):
        self._gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")


class WinnerState(State):
    def __init__(self, gumballMachine):
        self._gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter")
        self._gumballMachine.releaseBall()
        if self._gumballMachine.getCount() == 0:
            self._gumballMachine.setState(self._gumballMachine.getSoldOutState())
        else:
            self._gumballMachine.releaseBall()
            if self._gumballMachine.getCount() > 0:
                self._gumballMachine.setState(self._gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs!")
                self._gumballMachine.setState(self._gumballMachine.getSoldOutState())
