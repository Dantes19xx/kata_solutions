import unittest
from kyu_4.permutations import permutations

class TestPermutations(unittest.TestCase):
    def test_single_char(self):
        self.assertEqual(sorted(permutations('a')), ['a'])

    def test_two_chars(self):
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])

    def test_duplicate_chars(self):
        self.assertEqual(
            sorted(permutations('aabb')),
            ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
        )

