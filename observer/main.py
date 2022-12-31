from typing import Protocol
from enum import Enum


class Weather(Enum):
    SUNNY = 1
    RAINY = 2
    WINDY = 3


class Feeling(Enum):
    WARM = 1
    WET = 2
    COLD = 3


class IWeatherObserver(Protocol):
    name: str
    weather: Weather

    def obtain_feeling(self, feeling: Feeling) -> None:
        raise NotImplementedError

    def update_weather(self, new_weather: Weather) -> None:
        raise NotImplementedError

    def get_weather_message(self) -> str:
        raise NotImplementedError


class IObservedMan():
    observers: list[IWeatherObserver]
    feel: Feeling

    def add_observer(self, observer: IWeatherObserver) -> None:
        raise NotImplementedError

    def notify_observers(self) -> None:
        raise NotImplementedError

    def change_feeling(self, new_feeling: Feeling) -> None:
        raise NotImplementedError


class WeatherObserver:
    def __init__(self, name: str = 'not important', weather: Weather = Weather.SUNNY) -> None:
        self.name = name
        self.weather = weather

    def obtain_feeling(self, feeling: Feeling) -> None:
        if feeling == Feeling.WARM:
            self.update_weather(Weather.SUNNY)
        if feeling == Feeling.COLD:
            self.update_weather(Weather.WINDY)
        if feeling == Feeling.WET:
            self.update_weather(Weather.RAINY)
        print('ALERT! Weather changed!')
        print(self.get_weather_message())


    def update_weather(self, new_weather: Weather) -> None:
        if new_weather:
            self.weather = new_weather

    def get_weather_message(self) -> str:
        return f'Hello! My name is {self.name.capitalize()} and it is {self.weather.name.lower()} outside!'


class ObservedMan:
    def __init__(self, observers: list[IWeatherObserver], feeling: Feeling = Feeling.WARM) -> None:
        self.observers = observers
        self.feeling = feeling

    def add_observer(self, observer: IWeatherObserver) -> None:
        self.observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.obtain_feeling(self.feeling)

    def change_feeling(self, new_feeling: Feeling) -> None:
        self.feeling = new_feeling
        self.notify_observers()

meteo_man = WeatherObserver('Lucas')
guy_outside = ObservedMan([])

guy_outside.add_observer(meteo_man)
print('DEFAULT MESSAGE:')
print(meteo_man.get_weather_message())
print('CHANGED FEELING OF OBSERVED MAN:')
guy_outside.change_feeling(Feeling.COLD)
