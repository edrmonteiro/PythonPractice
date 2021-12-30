import abc

class AbstractFacade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_employees(self):
        pass
