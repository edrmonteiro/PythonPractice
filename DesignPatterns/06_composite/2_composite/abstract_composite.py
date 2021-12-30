import abc

class AbstractComposite(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_oldest(self):
        pass
