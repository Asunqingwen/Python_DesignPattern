from IteratorPattern.Menu import DinerMenu, CafeMenu
from IteratorPattern.Waitress import Waitress

if __name__ == '__main__':
    dinerMenu = DinerMenu()
    cafeMenu = CafeMenu()

    waitress = Waitress(dinerMenu, cafeMenu)
    waitress.printMenu()
