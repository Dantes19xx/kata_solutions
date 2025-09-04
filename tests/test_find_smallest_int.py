from unittest import TestCase
from kyu_8.find_smallest_int import find_smallest_int


class TestSmallestInt(TestCase):
    def test1(self):
        self.assertEqual(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)

    def test2(self):
        self.assertEqual(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)

    def test3(self):
        self.assertEqual(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)
