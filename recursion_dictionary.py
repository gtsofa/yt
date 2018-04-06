# recursion_dictionary.py

# suppose i want to do integer multiplicate and all i have available is addition

# multiplication - iterative soluntion
# check a*b --> 'add a to itself b times'
# capture state by
"""
# start = i
# stop at = 0
# condition: i < i-1 # each time it reduces by 1 iteratively until i get down to 0
# result = current value of computation
# """
# def mult_iter(a, b):
#     # returns a * b using iteration Eg 2*5 --> 2+2+2+2+2
#     result = 0
#     while b > 0:
#         result += a # adds a to results in every iteration
#         b -= 1 # step thro by going backward --> 5 then 4 then 3 then 2 then 1

#     return result

# # testing here:
# print(mult_iter(2,5))

# get the factorial of a number
# Q - What's the base case?
# A - when n == 1 --> this is the simplest bit i know/can deal with
# when will it stop at --> n-1

def fact(n):
    """Return the factorial of a number."""
    if n == 1:
        return 1

    else:
        return n * fact(n-1)