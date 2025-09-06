from unittest import TestCase
from kyu_8.area_or_perimeter import area_or_perimeter


class TestAreaOrPerimeter(TestCase):
    def test_area(self):
        self.assertEqual(area_or_perimeter(4, 4), 16)

    def test_perimeter(self):
        self.assertEqual(area_or_perimeter(6, 10), 32)
