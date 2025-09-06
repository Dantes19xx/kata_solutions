from unittest import TestCase
from kyu_6.find_uniq import find_uniq


class TestFindUniq(TestCase):
    def test1(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)

    def test2(self):
         self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        
    def test3(self):
         self.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)
