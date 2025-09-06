from unittest import TestCase
from kyu_7.isograms import is_isogram


class TestIsograms(TestCase):
    def test1(self):
        self.assertTrue(is_isogram("Dermatoglyphics"))

    def test2(self):
        self.assertTrue(is_isogram("isogram"))

    def test3(self):
        self.assertFalse(is_isogram("aba"))
    
    def test4(self):
        self.assertFalse(is_isogram("moOse"))
    
    def test5(self):
        self.assertFalse(is_isogram("isIsogram"))
    
    def test6(self):
        self.assertTrue(is_isogram(""))
