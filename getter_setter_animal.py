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

    def __str__(self):
        """Return name and age of the animal class"""
        return "animal:"+str(self.name)+":"+str(self.age)



