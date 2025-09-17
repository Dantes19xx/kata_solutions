import unittest
from stack.is_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_true(self):
        ins = Solution()
        self.assertTrue(ins.isPalindrome([1,2,2,1]))

    def test_false(self):
        ins = Solution()
        self.assertFalse(ins.isPalindrome([1,2]))