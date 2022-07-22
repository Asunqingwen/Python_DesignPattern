from StatePattern.GumballMachine import GumballMachine

if __name__ == '__main__':
    gumballMachine = GumballMachine(5)
    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)
