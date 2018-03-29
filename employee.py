# Employee class

class Employee:
    """A sample employee class"""
    
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        """Initialize employee class"""
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """Return employee email address"""
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """Return employee full name"""
        return '{} {}'.format(self.first, self.last)
        

    def apply_raise(self):
        """Calculates the employee pay raise"""
        self.pay = int(self.pay * self.raise_amt)

    fullname('julius', 'nyule', 20000)