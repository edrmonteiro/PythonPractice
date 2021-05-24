import abc

class AbstractCar(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def description(self):
        pass

    @abc.abstractproperty
    def cost(self):
        pass
