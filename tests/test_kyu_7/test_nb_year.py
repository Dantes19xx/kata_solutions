import unittest
from kyu_7.nb_year import nb_year

class TestNbYear(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)

    def test_aug_zero(self):
        # без дополнительных жителей, только процентный рост
        self.assertEqual(nb_year(1000, 2, 0, 1200), 10)
