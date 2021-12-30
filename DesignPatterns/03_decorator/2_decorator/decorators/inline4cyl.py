from .abstract_decorator import AbstractDecorator

class Inline4Cyl(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', inline 4 cylinder'

    @property
    def cost(self):
        return self.car.cost + 500.00
