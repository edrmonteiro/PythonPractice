import abc

class AbstractEmployees(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_employee_info(self, empids):
        pass
