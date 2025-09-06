from unittest import TestCase
from kyu_7.find_shortest_word import find_short


class TestFindShortestWord(TestCase):
    def test1(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)

    def test2(self):
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
    
    def test3(self):
        self.assertEqual(find_short("lets talk about javascript the best language"), 3)

    def test4(self):
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1)
    
    def test5(self):
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)
    
    def test6(self):
        self.assertEqual(find_short("Let's travel abroad shall we"), 2)
