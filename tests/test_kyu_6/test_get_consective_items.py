from unittest import TestCase
from kyu_6.get_consective_items import get_consective_items

class TestGetConsecutiveItems(TestCase):
    def test_number_input(self):
        self.assertEqual(get_consective_items(90000, 0), 4)

    def test_string_input(self):
        self.assertEqual(
            get_consective_items(
                'ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii',
                'i'
            ),
            11
        )