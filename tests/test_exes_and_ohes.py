from unittest import TestCase
from kyu_7.exes_and_ohes import xo


class TestXO(TestCase):
    def test_xo_true_1(self):
        self.assertTrue(xo("ooxx"))

    def test_xo_true_2(self):
        self.assertTrue(xo("ooxXm"))
    
    def test_xo_true_3(self):
        self.assertTrue(xo("zpzpzpp"))

    def test_xo_false_1(self):
        self.assertFalse(xo("xooxx"))
    
    def test_xo_false_2(self):
        self.assertFalse(xo("zzoo"))
