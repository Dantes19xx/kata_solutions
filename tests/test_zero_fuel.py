from unittest import TestCase
from kyu_8.zero_fuel import zero_fuel


class TestZeroFuel(TestCase):
    def test1(self):
        self.assertTrue(zero_fuel(50, 25, 2))

    def test2(self):
        self.assertFalse(zero_fuel(100, 50, 1),False)
