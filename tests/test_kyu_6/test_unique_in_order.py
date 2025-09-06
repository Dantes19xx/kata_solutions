from unittest import TestCase
from kyu_6.unique_in_order import unique_in_order


class TestUniqInOrder(TestCase):
    def test1(self):
        self.assertEqual(unique_in_order(""), [])

    def test2(self):
        self.assertEqual(unique_in_order([]), [])
    
    def test3(self):
        self.assertEqual(unique_in_order(()), [])
    
    def test4(self):
        self.assertEqual(unique_in_order("A"), ["A"])
    
    def test5(self):
        self.assertEqual(unique_in_order(["A"]), ["A"])
    
    def test6(self):
        self.assertEqual(unique_in_order(("A")), ["A"])
    
    def test7(self):
        self.assertEqual(unique_in_order(("AA")), ["A"])
    
    def test8(self):
        self.assertEqual(unique_in_order(
            ("AAAABBBCCDAABBB")),
            ["A", "B", "C", "D", "A", "B"]
        )
    
    def test9(self):
        self.assertEqual(
            unique_in_order(("ABBCcA")),
            ["A", "B", "C", "c", "A"]
        )
    
    def test10(self):
        self.assertEqual(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
    
    def test11(self):
        self.assertEqual(unique_in_order(
            ["a", "b", "b", "a"]),
            ["a", "b", "a"]
        )
