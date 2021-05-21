from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abstract_facade import AbstractFacade

class FacadeFactory(object):
    @staticmethod
    def create_facade(module_name):
        module = import_module('.' + module_name, __package__)

        classes = getmembers(module,
                             lambda m: (
                                 isclass(m) 
                                 and not isabstract(m)
                                 and issubclass(m, AbstractFacade))
        )

        return classes[0][1]()
