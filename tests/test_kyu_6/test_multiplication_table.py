from unittest import TestCase
from kyu_6.multiplication_table import multiplication_table


class TestMultiplicationTable(TestCase):
    def test_2_dimension(self):
        self.assertEqual(multiplication_table(2), [
            [1, 2],
            [2, 4]
        ])

    def test_3_dimension(self):
        self.assertEqual(multiplication_table(3), [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ])

    def test_4_dimension(self):
        self.assertEqual(multiplication_table(4), [
            [1, 2, 3, 4],
            [2, 4, 6, 8],
            [3, 6, 9, 12],
            [4, 8, 12, 16]
        ])

    def test_5_dimension(self):
        self.assertEqual(multiplication_table(5), [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],
            [4, 8, 12, 16, 20],
            [5, 10, 15, 20, 25]
        ])
