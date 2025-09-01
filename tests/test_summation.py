from unittest import TestCase
from kyu_8.summation import summation


class TestSummation(TestCase):
    def test1(self):
        self.assertEqual(summation(1), 1)

    def test2(self):
        self.assertEqual(summation(8), 36)

    def test3(self):
        self.assertEqual(summation(22), 253)

    def test4(self):
        self.assertEqual(summation(100), 5050)

    def test5(self):
        self.assertEqual(summation(213), 22791)
