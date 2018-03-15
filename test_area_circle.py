# test_area_cirlce.py

# structure of unit testing
# import statements

import unittest

# import program / file you're testing
import area_cirle

# create a class that's going to do the testing
class TestareaCircle(unittest.TestCase):
    # run some tests that's going to give us the area of a cirlce
    def test_areaCirlce_for_10radius(self):
        # capture the results of the function 
        # u need to know the formulae of what u are trying to achieve area = pi*r.squared
        results = area_cirle.areaCirlce(10)

        # check for  expected output
        expected = 314.1592653589793
        self.assertEqual(expected, results)


# run the tests
if __name__ == '__main__':
    unittest.main()
