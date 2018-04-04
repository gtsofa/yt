# tuples_listing_aliasing_cloning_mutability.py

# FYI: using tuples to return more than 1 values in a func
def quotient_and_remainder(x, y):
    """
    Returns the quotient and remainder 
    """
    q = x // y
    r = x % y

    return (q, r)

(quot, rem) = quotient_and_remainder(4,5)
print(quot, rem)

# FYI about Lists
'''
--> lists are indexed 0 to len(L)-1
--> range(n) goes from 0 to n-1
'''