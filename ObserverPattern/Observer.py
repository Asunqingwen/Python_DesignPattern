from abc import ABC, abstractmethod
from Subject import Subject, WeatherData


class Observer(ABC):
    @abstractmethod
    def update(self, subject, *args):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: Subject):
        self._temperature = .0
        self._humidity = .0
        weatherData.registerObserver(self)

    def update(self, subject, *args):
        if isinstance(subject, WeatherData):
            self._temperature = subject.temperature
            self._humidity = subject.humidity
            self.display()

    def display(self):
        print(
            "Current conditions: " + self._temperature.__str__() + "F degrees and " + self._humidity.__str__() + "% humidity")


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: Subject):
        self._temperature = .0
        self._humidity = .0
        self._pressure = .0
        weatherData.registerObserver(self)

    def update(self, subject, *args):
        if isinstance(subject, WeatherData):
            self._temperature = subject.temperature
            self._humidity = subject.humidity
            self._pressure = subject.pressure
            self.display()

    def display(self):
        print(
            "Statistics Data: " + self._temperature.__str__() + "F degrees and " + self._humidity.__str__() + "% humidity and " + self._pressure.__str__() + "Pa")


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: Subject):
        self._temperature = .0
        self._humidity = .0
        self._pressure = .0
        weatherData.registerObserver(self)

    def update(self, subject, *args):
        if isinstance(subject, WeatherData):
            self._temperature = subject.temperature
            self._humidity = subject.humidity
            self._pressure = subject.pressure
            self.display()

    def display(self):
        print(
            "Forecast Data: : " + self._temperature.__str__() + "F degrees and " + self._humidity.__str__() + "% humidity and " + self._pressure.__str__() + "Pa")
