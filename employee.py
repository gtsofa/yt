# Employee class

class Employee:
    """A sample employee class"""
    
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        """Initialize employee class"""
        self.first = first
        self.last = last
        self.pay = pay

    #@property
    def email(self):
        """Return employee email address"""
        return '{}.{}@company.com'.format(self.first.lower(), self.last.lower())

    #@property
    def fullname(self):
        """Return employee full name"""
        return '{} {}'.format(self.first, self.last)
        

    def apply_raise(self):
        """Calculates the employee pay raise"""
        self.pay = int(self.pay * self.raise_amt)

    #fullname('julius', 'nyule', 20000)

    # testing the class
emp_1 = Employee('Julius', 'Nyule', 5000)
emp_2 = Employee('Tsofa', 'Maestro', 2000)

print(emp_1) # <__main__.Employee instance at 0x7f9c1d9bda70>
print(emp_1.fullname())
print(emp_1.email())