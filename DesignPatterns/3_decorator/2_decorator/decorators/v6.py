from .abstract_decorator import AbstractDecorator

class V6(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', V6'

    @property
    def cost(self):
        return self.car.cost + 1200.00
