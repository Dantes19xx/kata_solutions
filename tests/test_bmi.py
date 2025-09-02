from unittest import TestCase
from kyu_8.bmi import bmi


class TestBMI(TestCase):
    def test_underweight(self):
        self.assertEqual(bmi(50, 1.80), "Underweight")

    def test_normal(self):
        self.assertEqual(bmi(80, 1.80), "Normal")

    def test_overweight(self):
        self.assertEqual(bmi(90, 1.80), "Overweight")
    
    def test_obese(self):
        self.assertEqual(bmi(100, 1.80), "Obese")
        