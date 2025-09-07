from unittest import TestCase
from kyu_6.count_smileys import count_smileys


class TestCountSmileys(TestCase):
    def test1(self):
        self.assertEqual(count_smileys([]), 0)

    def test2(self):
        self.assertEqual(count_smileys([':D',':~)',';~D',':)']), 4)
    
    def test3(self):
        self.assertEqual(count_smileys([':)',':(',':D',':O',':;']), 2)
    
    def test4(self):
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
