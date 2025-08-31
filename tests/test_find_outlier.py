from unittest import TestCase
from kyu_6.find_outlier import find_outlier


class TestFindOutlier(TestCase):
    def test1(self):
        self.assertEqual(find_outlier([2, 4, 6, 8, 10, 3]), 3)
    
    def test2(self):
         self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        
    def test3(self):
         self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
