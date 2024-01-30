
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(5,6)

        self.assertEqual(res,11)

    def test_subtract(self):
        res = calc.subtract(5,7)

        self.assertEqual(res,2)