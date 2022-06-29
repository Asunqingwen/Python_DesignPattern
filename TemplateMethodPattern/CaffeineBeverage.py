from abc import ABC, abstractmethod

from typing_extensions import final


class CaffeineBeverage(ABC):
    @final
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass

    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")

    def customerWantsCondiments(self):
        return True


class CoffeeWithHook(CaffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter")

    def addCondiments(self):
        print("Adding Sugar and Milk")

    def customerWantsCondiments(self):
        answer = self._getUserInput()
        return answer.lower().startswith("y")

    def _getUserInput(self):
        print("Would you like milk and sugar with your coffee (y/n)? ")
        answer = input()
        return answer


class TeaWithHook(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding Lemon")

    def customerWantsCondiments(self):
        answer = self._getUserInput()
        return answer.lower().startswith("y")

    def _getUserInput(self):
        print("Would you like lemon with your tea (y/n)? ")
        answer = input()
        return answer
