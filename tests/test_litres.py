from unittest import TestCase
from kyu_8.litres import litres


class TestLitres(TestCase):
    def test1(self):
        self.assertEqual(litres(1.4), 0)
    
    def test2(self):
        self.assertEqual(litres(12.3), 6)

    def test3(self):
        self.assertEqual(litres(0.82), 0)
    
    def test4(self):
        self.assertEqual(litres(11.8), 5)
    
    def test5(self):
        self.assertEqual(litres(1787), 893)
