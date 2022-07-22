from StatePattern.StateInterface import SoldOutState, NoQuarterState, HasQuarterState, SoldState


class GumballMachine:
    def __init__(self, numberGumballs):
        self._soldOutState = SoldOutState(self)
        self._noQuarterState = NoQuarterState(self)
        self._hasQuarterState = HasQuarterState(self)
        self._soldState = SoldState(self)
        self._winnerState = SoldState(self)
        self._state = self._soldOutState
        self._count = numberGumballs
        if numberGumballs > 0:
            self._state = self._noQuarterState

    def insertQuarter(self):
        self._state.insertQuarter()

    def ejectQuarter(self):
        self._state.ejectQuarter()

    def turnCrank(self):
        self._state.turnCrank()
        self._state.dispense()

    def setState(self, state):
        self._state = state

    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self._count > 0:
            self._count = self._count - 1

    def getSoldOutState(self):
        return self._soldOutState

    def getNoQuarterState(self):
        return self._noQuarterState

    def getHasQuarterState(self):
        return self._hasQuarterState

    def getSoldState(self):
        return self._soldState

    def getWinnerState(self):
        return self._winnerState

    def getCount(self):
        return self._count

    def __str__(self):
        stringBuffer = str()
        stringBuffer += "\nMighty Gumball Inc.\n"
        stringBuffer += "Java-enabled Standing Gumball Model #2004\n"
        stringBuffer += "Inventory: " + self._count.__str__() + " gumballs\n"
        if self._count == 0:
            stringBuffer += "Machine is sold out\n"
        else:
            stringBuffer += "Machine is waiting for quarter\n"
        return stringBuffer
