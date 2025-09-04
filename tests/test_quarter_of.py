from unittest import TestCase
from kyu_8.quarter_of import quarter_of


class TestQuarterOf(TestCase):
    def test1(self):
        self.assertEqual(quarter_of(3), 1)
    
    def test2(self):
        self.assertEqual(quarter_of(8), 3)
    
    def test3(self):
        self.assertEqual(quarter_of(11), 4)
