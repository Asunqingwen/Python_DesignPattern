from abc import ABC, abstractmethod
from ObserverPattern import Observer


class Subject(ABC):
    def __init__(self):
        self._changed = False

    @property
    def changed(self):
        return self._changed

    @changed.setter
    def changed(self, flag):
        self._changed = flag

    @abstractmethod
    def registerObserver(self, observer: Observer):
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self._observers = list()
        self._temperature = .0
        self._humidity = .0
        self._pressure = .0

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure

    def registerObserver(self, observer: Observer):
        self._observers.append(observer)

    def removeObserver(self, observer: Observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self, self._temperature, self._humidity, self._pressure)

    def measurementsChanged(self):
        if self.changed:
            self.notifyObservers()
        self.changed = False

    def setMeasurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.changed = True
        self.measurementsChanged()
