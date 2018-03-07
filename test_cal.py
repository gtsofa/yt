# unittest for cal.py

import unittest

import cal

class TestCal(unittest.TestCase):
    
    def test_add(self):
        result = cal.add(10,5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
    # to avoid using this if statement below; run python -m unittest test_cal.py
