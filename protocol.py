import abc
from typing import Protocol


class Engine(Protocol):
    def start(self): ...

    def stop(self): ...

    def is_on(self) -> bool: ...

    def get_rpm(self) -> int: ...


class Vehicle(abc.ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abc.abstractmethod
    def drive(self): ...

    @abc.abstractmethod
    def start_stop_engine(self): ...

    def get_rpm(self) -> int:
        return self.engine.get_rpm()


class Car(Vehicle):
    def drive(self):
        print("Car is driving")

    def start_stop_engine(self):
        if self.engine.is_on():
            print("Car is stopping engine")
            self.engine.stop()
        else:
            print("Car is starting engine")
            self.engine.start()


class ElectricEngine:
    def __init__(self, max_power_watts: int):
        self.max_power_watts = max_power_watts
        self._is_on = False
        self._rpm = 0

    def start(self):
        self._is_on = True
        self._rpm = 100

    def stop(self):
        self._is_on = False
        self._rpm = 0

    def get_rpm(self) -> int:
        return self._rpm

    def is_on(self) -> bool:
        return self._is_on


electric_car = Car(ElectricEngine(100))

electric_car.start_stop_engine()
electric_car.start_stop_engine()