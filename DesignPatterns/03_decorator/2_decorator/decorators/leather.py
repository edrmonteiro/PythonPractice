from .abstract_decorator import AbstractDecorator

class V6(AbstractDecorator):
    @property
    def description(self):
        return self.car.description + ', top-grain leather'

    @property
    def cost(self):
        return self.car.cost + 2700.00
