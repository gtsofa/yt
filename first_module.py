# corey series
"""
Whenever a python prog runs directly it equates __name__ variable to __main__ first.
ie sort of like asking is the program running directly or imported?
"""
#print "This is first module's name: {}".format(__name__) 

if __name__ == '__main__':
    print "Run directly"
else:
    print "Run from import."