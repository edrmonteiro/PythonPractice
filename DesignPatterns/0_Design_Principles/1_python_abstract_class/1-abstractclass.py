import abc

class MyAbsClass(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def myproperty(self):
        pass

    @abc.abstractmethod
    def mymethod(self, value):
        pass

class MyConcreteClass(MyAbsClass):
    @property
    def myproperty(self):
        return 42

    def mymethod(self, value):
        assert 42 == value

c = MyConcreteClass()
print(c.myproperty)
c.mymethod(42)


class MyAbsClass2(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractproperty
    def myproperty(self):
        pass

    @abc.abstractmethod
    def mymethod(self, value):
        pass

class MyConcreteClass2(MyAbsClass2):
    @property
    def myproperty(self):
        return 42

    def mymethod(self, value):
        assert 42 == value

c = MyConcreteClass2()
print(c.myproperty)
c.mymethod(42)