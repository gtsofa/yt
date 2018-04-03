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

# def is_even_with_return(i):
#     """
#     Returns True is i is even, otherwise false.
#     """
#     print("with return")
#     remainder = i % 2
#     return remainder == 0 # to make it boolean

# # calling the function now
# print(is_even_with_return(3))

# # using the function later on the code
# print("all numbers between 0 and 20: even or not")
# for i in range(20):
#     if is_even_with_return(i):
#         print(i, "even")

#     else:
#         print(i, "odd")

# # without return
# def is_even_with_no_return(i):
#     print("without return")
#     remainder = i % 2
#     # return None

# is_even_with_no_return(3)
# print(is_even_with_no_return(3))

# function as arguments

def func_a():
    print 'inside a func_a'

def func_b(y):
    print 'inside func_b'
    return y

def func_c(z):
    print 'inside func_c'
    return z()

# testing them out now
print func_a()
print 5 + func_b(2)
print func_c(func_a)
