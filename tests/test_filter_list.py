from unittest import TestCase
from kyu_7.filter_list import filter_list


class TestFilterList(TestCase):
    def test1(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])

    def test2(self):
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])

    def test3(self):
        self.assertEqual(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])
