from unittest import TestCase
from kyu_7.remove_smallest import remove_smallest


class TestRemoveSmallest(TestCase):
    def test1(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])

    def test2(self):
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])

    def test3(self):
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])
    
    def test4(self):
        self.assertEqual(remove_smallest([]), [])
