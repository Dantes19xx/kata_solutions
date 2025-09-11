from unittest import TestCase
from kyu_8.is_palindrome import is_palindrome


class TestIsPalindrome(TestCase):
    def test1(self):
        self.assertTrue(is_palindrome('a'))
    
    def test2(self):
        self.assertTrue(is_palindrome('aba'))
    
    def test3(self):
        self.assertTrue(is_palindrome('Abba'))
    
    def test4(self):
        self.assertFalse(is_palindrome('walter'))
    
    def test4(self):
        self.assertFalse(is_palindrome('Kasue'))
