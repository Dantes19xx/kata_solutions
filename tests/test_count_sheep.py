from unittest import TestCase
from kyu_8.count_sheep import count_sheep


class TestCountSheep(TestCase):
    def test1(self):
        self.assertEqual(count_sheep(0), "")

    def test2(self):
        self.assertEqual(count_sheep(1), "1 sheep...")
    
    def test3(self):
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
    
    def test4(self):
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
