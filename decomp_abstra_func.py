# decomp_abstract_func.py
# Abstraction
'''
--> You don't need to know how project works to use it.
--> Achieve it by -- function specifications or docstrings.
'''
# Decomposition
'''
--> Different devices will work together to achieve and end goal
--> Achieve it by --modules --functions --classes
'''

def is_even_with_return(i):
    """
    Returns True is i is even, otherwise false.
    """
    print("print with return")
    remainder = i % 2
    return remainder == 0

# calling the function now
print(is_even_with_return(3))

# without return
def is_even_with_no_return(i):
    print("without return")
    remainder = i % 2
    # return None

is_even_with_no_return(3)
print(is_even_with_no_return(3))
