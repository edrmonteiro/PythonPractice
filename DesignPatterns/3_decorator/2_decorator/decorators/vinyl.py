from .abstract_decorator import AbstractDecorator

class Vinyl(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', vinyl upholstery'

    @property
    def cost(self):
        return self.car.cost + 500.00
