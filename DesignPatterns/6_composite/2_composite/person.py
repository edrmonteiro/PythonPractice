from abstract_composite import AbstractComposite

class Person(AbstractComposite):

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def get_oldest(self):
        return self
