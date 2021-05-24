from .abstract_car import AbstractCar

class Economy(AbstractCar):
    @property
    def description(self):
        return 'Economy'

    @property
    def cost(self):
        return 12000.00
