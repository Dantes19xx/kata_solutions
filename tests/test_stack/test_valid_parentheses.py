import unittest
from stack.valid_parentheses import Solution

class TestIsValid(unittest.TestCase):

    def test_true1(self):
        self.assertTrue(Solution("()"))
        
    def test_true2(self):
        self.assertTrue(Solution("()[]{}"))

    def test_true3(self):
        self.assertTrue(Solution("([])"))

    def test_false(self):
        ins = Solution("(]")
        self.assertFalse(ins.isValid())

    def test_false2(self):
        ins = Solution("([)]")
        self.assertFalse(ins.isValid())
        