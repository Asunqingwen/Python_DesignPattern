from CompositePattern.MenuComponent import Menu, MenuItem
from CompositePattern.Waitress import Waitress

if __name__ == '__main__':
    pancakeHouseMenu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    dinerMenu = Menu("DINER MENU", "lunch")
    cafeMenu = Menu("CAFE MENU", "Dinner")
    dessertMenu = Menu("DESSERT MENU", "Dessert of course!")

    allMenus = Menu("ALL MENUS", "All menus combined")

    allMenus.add(pancakeHouseMenu)
    allMenus.add(dinerMenu)
    allMenus.add(cafeMenu)

    pancakeHouseMenu.add(MenuItem(
        "K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99
    ))

    pancakeHouseMenu.add(MenuItem(
        "Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99
    ))
    pancakeHouseMenu.add(MenuItem(
        "Blueberry Pancakes", "Pancakes made with fresh blueberries, and blueberry syrup", True, 3.49
    ))
    pancakeHouseMenu.add(MenuItem(
        "Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59
    ))

    dinerMenu.add(MenuItem(
        "Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99
    ))
    dinerMenu.add(MenuItem(
        "BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", False, 2.99
    ))
    dinerMenu.add(MenuItem(
        "Soup of the day", "Soup of the day,with a side of potato salad", False, 3.29
    ))
    dinerMenu.add(MenuItem(
        "Hot dog", "A hot dog,with saurkraut,relish,onions,topped with cheese", False, 3.05
    ))
    dinerMenu.add(MenuItem(
        "Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99
    ))
    dinerMenu.add(MenuItem(
        "Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89
    ))

    dinerMenu.add(dessertMenu)
    dessertMenu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla ice cream", True, 1.59
                             ))
    dessertMenu.add(MenuItem("Cheesecake", "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99
                             ))
    dessertMenu.add(MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89
                             ))
    cafeMenu.add(
        MenuItem("Veggie Burger and Air Fires", "Veggie burger on a whole wheat bun, lettuce,tomato,and fries", True,
                 3.99))
    cafeMenu.add(MenuItem("Soup of the day", "A cup of the soup of the day,with a side salad", False, 3.69))
    cafeMenu.add(MenuItem("Burrito", "A large burrito, with whole pinto beans,salsa,guacamole", True, 4.29))

    waitress = Waitress(allMenus)
    waitress.printMenu()
