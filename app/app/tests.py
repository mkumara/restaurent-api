
"""
Simple Test case
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """
    Simple calc test
    """
    def test_add_numbers(self):
        res = calc.add(10, 12)
        self.assertEqual(res, 22)

    def test_subtract_numbers(self):
        """ test calc subtract function"""
        res = calc.subtract(10, 3)
        self.assertEqual(res, 7)
