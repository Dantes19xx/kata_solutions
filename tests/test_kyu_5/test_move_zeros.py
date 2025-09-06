from unittest import TestCase
from kyu_5.move_zeros import move_zeros


class TestMoveZeroes(TestCase):
    def test_1(self):
        self.assertEqual(
            move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), 
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
        )

    def test_2(self):
        self.assertEqual(
            move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
    
    def test_3(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])
    
    def test_4(self):
        self.assertEqual(move_zeros([0]), [0])

    def test_5(self):
        self.assertEqual(move_zeros([]), [])
