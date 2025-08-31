from unittest import TestCase
from kyu_7.maskify import maskify


class TestMaskify(TestCase):
    def test1(self):
        self.assertEqual(maskify(""), "")
    
    def test2(self):
        self.assertEqual(maskify("123"), "123")
    
    def test3(self):
        self.assertEqual(maskify("SF$SDfgsd2eA"), "########d2eA")
