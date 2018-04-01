# getter_setter_animal.py

import random

print("# parentclass Animal")
class Animal(object):
    """Animal model"""

    def __init__(self, age):
        """Initializes animal class"""
        self.age = age
        self.name = None

    def get_age(self):
        """Return animal age"""
        return self.age

    def get_name(self):
        """Return animal name"""
        return self.name

    def set_age(self, newage):
        """set age of animal"""
        self.age = newage

    def set_name(self, newname=""):
        """set animal name to newname"""
        self.name = newname

    #w/o this mtd, this will be printed <__main__.Animal object at 0x7fb504f0c5d0>
    def __str__(self):
        """Print object of type animal: Return name and age of the animal class"""
        return "animal name is "+str(self.name)+" and age:"+str(self.age)

# test class
animale = Animal(24)
animale.set_name('Boris')
print(animale)

# Inherintance: subclass Cat
print("--subclass Cat--")
class Cat(Animal):
    """Cat class inherits from animal."""
    def speak(self):
        """Return sound of Cat"""
        print("meow!")

    def __str__(self):
        """Return the object of Cat """
        return "cat:"+str(self.name)+":"+str(self.age)

# test cat class
gatto = Cat(5)
print(gatto)
gatto.set_name("helium")
print(gatto)

# Inherintance: subclass Person
print("--subclass Person--")
class Person(Animal):
    """Person class"""
    def __init__(self, name, age):
        """Initialize Person class"""
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        """Return friends """
        return self.friends

    def add_friends(self, fname):
        """Adds friends """
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        """Return sound of the person"""
        print("hello")

    def age_diff(self, other):
        """Return age difference of a person"""
        diff = self.age - other.age
        print(abs(diff), "year difference")

    def __str__(self):
        """Return Cat data objects """
        return "person:"+str(self.name)+":"+str(self.age)

# test subclass Person
persone = Person("gtsofa", 23)
print(persone)

# Inheritance: subclass Student : inherit Person & Animal attributes.
class Student(Person):
    """Student class """
    def __init__(self, name, age, major=None):
        """Initialize student subclass"""
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        """set student major"""
        self.major = major

    def speak(self):
        """sound of student"""
        # random() will gives us random numbers on range of 0 & 1 excluding 1
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
        """Display Student data attributes."""
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

# subclass student test
print("# student testing----")
studente1 = Student("Tsofa", 34, "CS")
studente2 = Student("Sarah", 33)
print(studente1)
print(studente2)
print(studente1.get_name(),"says:", random.random())
studente1.speak()
print(studente2.get_name(),"says:", random.random())
studente2.speak()
#print(studente2.get_name(),"says:",r)

# Inherintance: subclass Rabbit: inherit Animal
class Rabbit(Animal):
    """Rabbit class"""
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        """Initialize Rabbit class """
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        """Return Rabbit ID rid"""
        return str(self.rid).zfill(3) #pad the beggining with zeros

    def get_parent1(self):
        """Return parent 1"""
        return self.parent1

    def get_parent2(self):
        """Return parent 2"""
        return self.parent2

    def __add__(self, other):
        """Returning object of same type as this class"""
        return Rabbit(0,self, other) # o-id, self-parent, other-otherparent

    def __eq__(self, other):
        """Compare two rabbits if they have the same two parents"""
        parent_same = self.parent1.rid == other.parent1.rid \
                    and self.parent2.rid == other.parent2.rid

        parents_opposite = self.parent2.rid == other.parent1.rid \
                        and self.parent1.rid == other.parent2.rid

        return parent_same or parents_opposite

    def __str__(self):
        """Return rabbit object"""
        #return "rabbit:"+ str(self.get_name()+":"+ self.get_rid())
        return "rabbit:"+ self.get_rid()

    

# rabbit tests
print("\n ----rabbits tests---")
print("--testing creating rabbits---")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent 1:", r1.get_parent1())
print("r2 parent 2:", r2.get_parent2())

print("---testing rabbit equality---")
r5 = r2+r3
r6 = r3+r2
print("r2:", r2)
print("r3:", r3)
print("r5", r5)
print("r6", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())







