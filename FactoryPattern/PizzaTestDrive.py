from FactoryPattern.PizzaStore.PizzaStore import NYPizzaStore, ChicagoPizzaStore

if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    nyStore.orderPizza("cheese")
    chicagoStore.orderPizza("cheese")
