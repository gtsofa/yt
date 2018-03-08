# primefactors.py unit test cases

import unittest

import primefactors

class PrimeFactorsTestCase(unittest.TestCase):
    
    @property
    def test_factors(self):
        list_of_factors = []
        self.assertEqual(list_of_factors(1), [])
        self.assertEqual(list_of_factors(2), [2])
        self.assertEqual(list_of_factors(3), [3])
        self.assertEqual(list_of_factors(4), [2,2])


if __name__ == '__main__':
    unittest.main()