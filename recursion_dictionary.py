# recursion_dictionary.py

# multiplication - iterative soluntion
# check a*b --> 'add a to itself b times'
# capture state by
"""
start = i
stop at = 0
condition: i < i-1
result = current value of computation
"""
def mult_iter(a, b):
    # returns a * b using iteration Eg 2*5 --> 2+2+2+2+2
    result = 0
    while b > 0:
        result += a # adds a to results in every iteration
        b -= 1 # step thro by going backward --> 5 then 4 then 3 then 2 then 1

    return result

# testing here:
print(mult_iter(2,5))
