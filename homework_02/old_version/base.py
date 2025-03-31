from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started: bool = False
    weight: int = 40
    fuel: float = float(500)
    fuel_consumption: int = 1

    def __init__(self, weight: int, fuel: float, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Fuel is at 0!")

    def move(self, distance: float):
        if self.fuel >= distance * self.fuel_consumption:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel("Not enough fuel for the move!")
