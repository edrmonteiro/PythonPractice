from .abstract_decorator import AbstractDecorator

class Red(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', Ferarri red'

    @property
    def cost(self):
        return self.car.cost + 1200.00
