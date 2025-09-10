from unittest import TestCase
from kyu_6.expanded_form import expanded_form


class TestExpanded(TestCase):
    def test1(self):
        self.assertEqual(expanded_form(12), '10 + 2')

    def test2(self):
        self.assertEqual(expanded_form(42), '40 + 2')
    
    def test3(self):
        self.assertEqual(expanded_form(70304), '70000 + 300 + 4')
