# tuples_listing_aliasing_cloning_mutability.py

# FYI: using tuples to return more than 1 values in a func
# def quotient_and_remainder(x, y):
#     """
#     Returns the quotient and remainder 
#     """
#     q = x // y
#     r = x % y

#     return (q, r)

# (quot, rem) = quotient_and_remainder(4,5)
# print(quot, rem)

# # FYI about Lists
# '''
# --> lists are indexed 0 to len(L)-1
# --> range(n) goes from 0 to n-1
# '''

# manupulating tuples
# can iterate over values

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],) # (t[0],) implies a tuple with only 1 element!
        if t[1] not in words:
            words = words + (t[1],)

    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

# testing get_data()
test = ((1,"a"),(2,"b"),(1,"a"),(7,"b"))
(a,b,c) = get_data(test)
print("a:",a,"b:",b,"c:",c)

# apply to any data that u want
tswift = ((2014, "Katy"),
          (2014, "Harry"),
          (2012, "Jake"),
          (2010, "Taylor"),
          (2008, "Joe"))

(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
"Taylor swift wrote songs about", num_people, "people!")