# calculator class that will perform test on

def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

# trying out functionality of functions
print(add(5,3))
print(subtract(5,3))
print(multiply(5,3))
print(divide(5,3))

