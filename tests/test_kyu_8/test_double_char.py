from unittest import TestCase
from kyu_8.double_char import double_char


class TestClassDoubleChar(TestCase):
    def test1(self):
        self.assertEqual(double_char("String"),"SSttrriinngg")

    def test2(self):
        self.assertEqual(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
    
    def test3(self):
        self.assertEqual(double_char("1234!_ "),"11223344!!__  ")
