from unittest import TestCase
from kyu_7.zipvalidate import zipvalidate


class TestZipValidate(TestCase):
    def test_true(self):
        self.assertTrue(zipvalidate('198328'))
        self.assertTrue(zipvalidate('310003'))
        self.assertTrue(zipvalidate('424000'))

    def test_false(self):
        self.assertFalse(zipvalidate('12A483'))
        self.assertFalse(zipvalidate('1@63'))
        self.assertFalse(zipvalidate('111'))
        self.assertFalse(zipvalidate('056879'))
        self.assertFalse(zipvalidate('1111111'))
