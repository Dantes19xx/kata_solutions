from unittest import TestCase
from kyu_6.find_even_index import find_even_index


class TestFindEvenIndex(TestCase):
    def test1(self):
        self.assertEqual(find_even_index([1,2,3,4,3,2,1]), 3)

    def test2(self):
        self.assertEqual(find_even_index([1,100,50,-51,1,1]), 1)
    
    def test3(self):
        self.assertEqual(find_even_index([1,2,3,4,5,6]), -1)

    def test4(self):
        self.assertEqual(find_even_index([20,10,30,10,10,15,35]), 3)
