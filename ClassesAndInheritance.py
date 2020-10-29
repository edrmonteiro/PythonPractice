"""
coding: utf-8
Created on 29/10/2020

@author: github.com/eduardormonteiro

From: MIT 6.00.1x Introduction to Computer Science and Programming Using Python
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
        
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def speak(self):
        print("meep")
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                       and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)
        
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)


import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
       self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name, age):
        Person.__init__(self, name, age) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,Student) or isinstance(obj,Grad)

def isMITPerson(obj):
    return isinstance(obj,MITPerson) or isinstance(obj,Grad)


# jelly = Cat(1)
# jelly.set_name('Jelly')
# tiger = Cat(1)
# tiger.set_name('Tiger')
# bean = Cat(0)
# bean.set_name('Bean')
# print(jelly)
# jelly.speak()
# blob = Animal(1)
# peter = Rabbit(3)
# peter.speak()
# eduardo = Person('Eduardo', 46)
# eduardo.speak()
# enzo = Person('Enzo', 5)
# eduardo.age_diff(enzo)
# fred = Student('Fred', 18, 'Course VI')

# peter = Rabbit(2)
# peter.set_name('Peter')
# hopsy = Rabbit(3)
# hopsy.set_name('Hopsy')
# cotton = Rabbit(1, peter, hopsy)
# cotton.set_name('Cottontail')
# mopsy = peter + hopsy
# print(mopsy == cotton)


p1 = MITPerson('Eduardo', 46)
p2 = MITPerson('Enzo', 5)

print(p1 > p2)

print(isStudent(p1))
print(isMITPerson(p1))

debugStop = True
