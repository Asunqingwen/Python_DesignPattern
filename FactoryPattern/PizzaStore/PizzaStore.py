from abc import ABC, abstractmethod

from FactoryPattern.IngredientFactory.PizzaIngredientFactory import NYIngredientFactory, ChicagoIngredientFactory, \
    CaliforniaIngredientFactory
from FactoryPattern.Pizza.Pizza import CheesePizza, PepperoniPizza, ClamPizza, VeggiePizza, Pizza


class PizzaStore(ABC):
    @abstractmethod
    def createPizza(self, type):
        pass

    def orderPizza(self, type):
        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def createPizza(self, type):
        pizza = Pizza()
        pizzaIngredientFactory = NYIngredientFactory()
        if "cheese" == type:
            pizza = CheesePizza(pizzaIngredientFactory)
            pizza.setName("New York Style Cheese Pizza")
        elif "pepperoni" == type:
            pizza = PepperoniPizza(pizzaIngredientFactory)
            pizza.setName("New York Style Pepperoni Pizza")
        elif "clam" == type:
            pizza = ClamPizza(pizzaIngredientFactory)
            pizza.setName("New York Style Clam Pizza")
        elif "veggie" == type:
            pizza = VeggiePizza(pizzaIngredientFactory)
            pizza.setName("New York Style Veggie Pizza")
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, type):
        pizza = Pizza()
        pizzaIngredientFactory = ChicagoIngredientFactory()
        if "cheese" == type:
            pizza = CheesePizza(pizzaIngredientFactory)
            pizza.setName("Chicago Style Cheese Pizza")
        elif "pepperoni" == type:
            pizza = PepperoniPizza(pizzaIngredientFactory)
            pizza.setName("Chicago Style Pepperoni Pizza")
        elif "clam" == type:
            pizza = ClamPizza(pizzaIngredientFactory)
            pizza.setName("Chicago Style Clam Pizza")
        elif "veggie" == type:
            pizza = VeggiePizza(pizzaIngredientFactory)
            pizza.setName("Chicago Style Veggie Pizza")
        return pizza


class CaliforniaPizzaStore(PizzaStore):
    def createPizza(self, type):
        pizza = Pizza()
        pizzaIngredientFactory = CaliforniaIngredientFactory()
        if "cheese" == type:
            pizza = CheesePizza(pizzaIngredientFactory)
            pizza.setName("California Style Cheese Pizza")
        elif "pepperoni" == type:
            pizza = PepperoniPizza(pizzaIngredientFactory)
            pizza.setName("California Style Pepperoni Pizza")
        elif "clam" == type:
            pizza = ClamPizza(pizzaIngredientFactory)
            pizza.setName("California Style Clam Pizza")
        elif "veggie" == type:
            pizza = VeggiePizza(pizzaIngredientFactory)
            pizza.setName("California Style Veggie Pizza")
        return pizza
