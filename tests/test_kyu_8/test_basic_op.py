from unittest import TestCase
from kyu_8.basic_op import basic_op


class TestBasicOp(TestCase):
    def test1(self):
        self.assertEqual(basic_op('+', 4, 7), 11)

    def test2(self):
        self.assertEqual(basic_op('-', 15, 18), -3)
    
    def test3(self):
        self.assertEqual(basic_op('*', 5, 5), 25)

    def test4(self):
        self.assertEqual(basic_op('/', 49, 7), 7)
