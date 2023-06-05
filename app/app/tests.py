"""
sample test
"""

from django.test import SimpleTestCase
from app import calc


class calcTest(SimpleTestCase):
    """ Test the Calc Module """

    def testAddNumbers(self):
        """test adding no. together"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def testSubstractNumbers(self):
        """test substraction of no. together"""
        res = calc.substract(15, 10)

        self.assertEqual(res, 5)
