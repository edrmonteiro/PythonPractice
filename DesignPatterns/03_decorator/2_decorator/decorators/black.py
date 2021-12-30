from .abstract_decorator import AbstractDecorator

class Black(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', midnight black'

    @property
    def cost(self):
        return self.car.cost + 1800.00
