from abc import ABC, abstractmethod

from FactoryPattern.Ingredient.Cheese import Cheese
from FactoryPattern.Ingredient.Clams import Clams
from FactoryPattern.Ingredient.Pepperoni import Pepperoni
from FactoryPattern.Ingredient.Dough import Dough
from FactoryPattern.Ingredient.Sauce import Sauce


class Pizza:
    name = ''
    dough = Dough()
    sauce = Sauce()
    veggies = list()
    cheese = Cheese()
    pepperoni = Pepperoni()
    clams = Clams()

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class CheesePizza(Pizza):
    def __init__(self, pizzaIngredientFactory):
        self._pizzaIngredientFactory = pizzaIngredientFactory

    def prepare(self):
        print("Preparing " + self.name)

        self.dough = self._pizzaIngredientFactory.createDough()
        self.sauce = self._pizzaIngredientFactory.createSauce()
        self.cheese = self._pizzaIngredientFactory.createCheese()


class ClamPizza(Pizza):
    def __init__(self, pizzaIngredientFactory):
        self._pizzaIngredientFactory = pizzaIngredientFactory

    def prepare(self):
        print("Preparing " + self.name)

        self.dough = self._pizzaIngredientFactory.createDough()
        self.sauce = self._pizzaIngredientFactory.createSauce()
        self.cheese = self._pizzaIngredientFactory.createCheese()
        self.clams = self._pizzaIngredientFactory.createClam()


class PepperoniPizza(Pizza):
    def __init__(self, pizzaIngredientFactory):
        self._pizzaIngredientFactory = pizzaIngredientFactory

    def prepare(self):
        print("Preparing " + self.name)

        self.dough = self._pizzaIngredientFactory.createDough()
        self.sauce = self._pizzaIngredientFactory.createSauce()
        self.cheese = self._pizzaIngredientFactory.createCheese()
        self.pepperoni = self._pizzaIngredientFactory.createPepperoni()


class VeggiePizza(Pizza):
    def __init__(self, pizzaIngredientFactory):
        self._pizzaIngredientFactory = pizzaIngredientFactory

    def prepare(self):
        print("Preparing " + self.name)

        self.dough = self._pizzaIngredientFactory.createDough()
        self.sauce = self._pizzaIngredientFactory.createSauce()
        self.cheese = self._pizzaIngredientFactory.createCheese()
        self.veggies = self._pizzaIngredientFactory.createVeggies()
