import unittest
import importlib
import Polynomial_Arithmetic_Calculator
importlib.reload(Polynomial_Arithmetic_Calculator)
from Polynomial_Arithmetic_Calculator import Polynomial

class TestPolynomial(unittest.TestCase):

    def test_init_and_str(self):
        p = Polynomial({2: 3, 0: -4, 1: 0})  # 3x^2 - 4
        self.assertEqual(str(p), '3x^2 - 4')

    def test_addition(self):
        p1 = Polynomial({2: 3, 0: -4})      # 3x^2 - 4
        p2 = Polynomial({1: 2, 0: 4})       # 2x + 4
        result = p1 + p2                    # 3x^2 + 2x
        self.assertEqual(str(result), '3x^2 + 2x')

    def test_subtraction(self):
        p1 = Polynomial({2: 3, 1: 2})       # 3x^2 + 2x
        p2 = Polynomial({2: 1, 1: 2})       # x^2 + 2x
        result = p1 - p2                    # 2x^2
        self.assertEqual(str(result), '2x^2')

    def test_multiplication(self):
        p1 = Polynomial({1: 1, 0: 1})       # x + 1
        p2 = Polynomial({1: 1, 0: -1})      # x - 1
        result = p1 * p2                    # x^2 - 1
        self.assertEqual(str(result), 'x^2 - 1')

    def test_division(self):
        p1 = Polynomial({2: 1, 0: -1})      # x^2 - 1
        p2 = Polynomial({1: 1, 0: -1})      # x - 1
        quotient, remainder = p1 / p2      # (x + 1, 0)
        self.assertEqual(str(quotient), 'x + 1')
        self.assertEqual(str(remainder), '0')

    def test_evaluation(self):
        p = Polynomial({2: 2, 1: -3, 0: 1})  # 2x^2 - 3x + 1
        result = p.evaluate(2)              # 2(4) - 6 + 1 = 3
        self.assertAlmostEqual(result, 3)

    def test_zero_polynomial(self):
        p = Polynomial({0: 0})
        self.assertEqual(str(p), '0')

    def test_divide_by_higher_degree(self):
        p1 = Polynomial({1: 2})             # 2x
        p2 = Polynomial({2: 1})             # x^2
        q, r = p1 / p2                      # 0 quotient, 2x remainder
        self.assertEqual(str(q), '0')
        self.assertEqual(str(r), '2x')

if __name__ == '__main__':
    unittest.main()
