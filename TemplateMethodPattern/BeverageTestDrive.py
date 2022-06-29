from CaffeineBeverage import TeaWithHook, CoffeeWithHook

if __name__ == '__main__':
    teaWithHook = TeaWithHook()
    coffeeWithHook = CoffeeWithHook()

    print("\nMaking tea...")
    teaWithHook.prepareRecipe()

    print("\nMaking coffee...")
    coffeeWithHook.prepareRecipe()
