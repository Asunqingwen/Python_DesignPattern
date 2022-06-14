from ObserverPattern.Observer import CurrentConditionsDisplay,StatisticsDisplay,ForecastDisplay
from Subject import WeatherData

if __name__ == '__main__':
    weatherData = WeatherData()
    currentConditionsDisplay = CurrentConditionsDisplay(weatherData)
    StatisticsDisplay = StatisticsDisplay(weatherData)
    ForecastDisplay = ForecastDisplay(weatherData)
    weatherData.setMeasurements(80, 65, 30.4)
    print("\n")
    weatherData.setMeasurements(82, 70, 29.2)
    print("\n")
    weatherData.setMeasurements(78, 90, 29.2)
