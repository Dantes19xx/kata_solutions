from unittest import TestCase
from kyu_7.disemvowel_trolls import disemvowel


class TestDisemvowel(TestCase):
    def test_disemvowel1(self):
        self.assertEqual(disemvowel("LOL"), "LL")

    def test_disemvowel2(self):
        self.assertEqual(disemvowel("Hello"), "Hll")

    def test_desemvowel_with_y(self):
        self.assertEqual(disemvowel("Yelling"), "Yllng")

