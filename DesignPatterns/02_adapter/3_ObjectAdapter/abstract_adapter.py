import abc

class AbstractAdapter(metaclass=abc.ABCMeta):
    def __init__(self, adapt):
        self._adapt = adapt

    @property
    def adapt(self):
        return self._adapt

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def address(self):
        pass
