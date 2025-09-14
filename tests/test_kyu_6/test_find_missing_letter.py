from unittest import TestCase
from kyu_6.find_missing_letter import find_missing_letter


class TestFindMissingLetter(TestCase):
    def test_case1(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')

    def test_case2(self):
        self.assertEqual(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')

    def test_case3(self):
        self.assertEqual(find_missing_letter(['b', 'd']), 'c')