class Singleton:
    _singleton = None

    @staticmethod
    def getInstance(self):
        if not self._singleton:
            self._singleton = Singleton()
        return self._singleton


if __name__ == '__main__':
    singleton1 = Singleton.getInstance
    print(singleton1)
    singleton2 = Singleton.getInstance
    print(singleton2)
