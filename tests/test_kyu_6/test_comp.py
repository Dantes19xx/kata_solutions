from unittest import TestCase
from kyu_6.comp import comp


class TestComp(TestCase):
    def test_valid_case(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertTrue(comp(a1, a2))

    def test_invalid_case_wrong_square(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertFalse(comp(a1, a2))

    def test_invalid_case_nonexistent_square(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        self.assertFalse(comp(a1, a2))

