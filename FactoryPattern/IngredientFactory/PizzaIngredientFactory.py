from abc import ABC, abstractmethod

from FactoryPattern.Ingredient.Cheese import ReggianoCheese, MozzarellaCheese, GoatCheese
from FactoryPattern.Ingredient.Clams import FreshClams, FrozenClams
from FactoryPattern.Ingredient.Dough import ThinCrustDough, ThickCrustDough, VeryThinDough
from FactoryPattern.Ingredient.Pepperoni import SlicedPepperoni
from FactoryPattern.Ingredient.Sauce import MarinaraSauce, PlumTomatoSauce, BruschettaSauce
from FactoryPattern.Ingredient.Veggies import Garlic, RedPepper, Mushroom, Onion, EggPlant, Spinach, BlackOlives


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def createDough(self):
        pass

    @abstractmethod
    def createSauce(self):
        pass

    @abstractmethod
    def createCheese(self):
        pass

    @abstractmethod
    def createVeggies(self):
        pass

    @abstractmethod
    def createPepperoni(self):
        pass

    @abstractmethod
    def createClam(self):
        pass


class NYIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return ReggianoCheese()

    def createVeggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FreshClams()


class ChicagoIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThickCrustDough()

    def createSauce(self):
        return PlumTomatoSauce()

    def createCheese(self):
        return MozzarellaCheese()

    def createVeggies(self):
        return [EggPlant(), Spinach(), BlackOlives()]

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FrozenClams()


class CaliforniaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return VeryThinDough()

    def createSauce(self):
        return BruschettaSauce()

    def createCheese(self):
        return GoatCheese()

    def createVeggies(self):
        return [EggPlant(), Mushroom(), Onion()]

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FrozenClams()
