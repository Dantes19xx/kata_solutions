from unittest import TestCase
from kyu_6.two_sum import two_sum


class TestTwoSum(TestCase):
    def test1(self):
        self.assertEqual(two_sum([1 ,2, 3], 4), (0,2))

    def test2(self):
        self.assertEqual(two_sum([1234,5678,9012], 14690), (1,2))
    
    def test3(self):
        self.assertEqual(two_sum([2, 2, 3], 4), (0, 1))
