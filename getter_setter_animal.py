# getter_setter_animal.py

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


