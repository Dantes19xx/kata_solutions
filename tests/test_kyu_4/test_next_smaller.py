from unittest import TestCase
from kyu_4.next_smaller import next_smaller


class TestNextSmaller(TestCase):
    def test1(self):
        self.assertEqual(next_smaller(907), 790)

    def test2(self):
        self.assertEqual(next_smaller(531), 513)

    def test3(self):
        self.assertEqual(next_smaller(135), -1)

    def test4(self):
        self.assertEqual(next_smaller(2071), 2017)

    def test5(self):
        self.assertEqual(next_smaller(414), 144)

    def test6(self):
        self.assertEqual(next_smaller(123456798), 123456789)

    def test7(self):
        self.assertEqual(next_smaller(123456789), -1)

    def test8(self):
        self.assertEqual(next_smaller(1234567908), 1234567890)