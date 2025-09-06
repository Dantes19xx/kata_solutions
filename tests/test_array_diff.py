from unittest import TestCase
from kyu_6.array_diff import array_diff


class TestArrayDiff(TestCase):
    def test1(self):
        self.assertEqual(array_diff([1,2], [1]), [2])
    
    def test2(self):
        self.assertEqual(array_diff([1,2,2], [1]), [2,2])
    
    def test3(self):
        self.assertEqual(array_diff([1,2,2], [2]), [1])
    
    def test4(self):
        self.assertEqual(array_diff([1,2,2], []), [1,2,2])
    
    def test5(self):
        self.assertEqual(array_diff([], [1,2]), [])
    
    def test6(self):
        self.assertEqual(array_diff([1,2,3], [1, 2]), [3])
