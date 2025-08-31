from unittest import TestCase
from kyu_6.find_odd import find_it


class TestFindIt(TestCase):
    def test_find_it_1(self):
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
    
    def test_find_it_2(self):
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)

    def test_finde_it_3(self):
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)

    def test_find_it_4(self):
        self.assertEqual(find_it([10, 10, 10]), 10)
    
    def test_find_it_5(self):
        self.assertEqual(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)

    def test_find_it_6(self):
        self.assertEqual(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)
        