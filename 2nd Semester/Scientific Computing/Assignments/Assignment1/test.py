import unittest
import error_calc
import numpy as np


class TestErrorCalc(unittest.TestCase):

    def setUp(self):
        self.val = 0.2
        self.n = 5

    def test_factorial(self):
        self.assertEqual(error_calc.factorial(2), 2)
        self.assertEqual(error_calc.factorial(0), 1)
        self.assertEqual(error_calc.factorial(3), 6)


    def test_ex(self):
        self.assertEqual(round(error_calc.ex(self.val), self.n - 1), round(np.exp(self.val), self.n - 1))
        self.assertEqual(round(error_calc.ex(self.val, self.n), self.n - 1), round(np.exp(self.val), self.n - 1))
        

    def test_truncation(self):
        self.assertEqual(error_calc.truncation_error(0.2, 4), 6.942482683625073e-05)
        self.assertEqual(error_calc.truncation_error(0.2, 3), 0.0014027581601696593)
        # give the value 3
        self.assertEqual(error_calc.truncation_error(0.2), 0.0014027581601696593)
        


if __name__ == "__main__":
    unittest.main()
