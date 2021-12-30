from .abstract_decorator import AbstractDecorator

class White(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', white'

    @property
    def cost(self):
        return self.car.cost + 800.00
