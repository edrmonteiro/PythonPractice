class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        
class CodeBuilder:
    def __init__(self, person):
        self.person = Person()

    def add_field(self, type, value):
        if type == 'name':
            self.person.name = value
        elif type == 'age':
            self.person.age = value
        return self

    def __str__(self):
        return str(self.person)
    

cb = CodeBuilder('Person')\
        .add_field('name', '""')\
        .add_field('age', '0')
print(cb)

stop = True