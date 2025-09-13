import unittest
from kyu_4.top_3_words import top_3_words

class TestTop3Words(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])

    def test_case2(self):
        self.assertEqual(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])

    def test_case3(self):
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])

    def test_case4(self):
        self.assertEqual(top_3_words("  , e   .. "), ["e"])

    def test_case5(self):
        self.assertEqual(top_3_words("  ...  "), [])

    def test_case6(self):
        self.assertEqual(top_3_words("  '  "), [])

    def test_case7(self):
        self.assertEqual(top_3_words("  '''  "), [])

    def test_case8(self):
        text = """In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""
        self.assertEqual(top_3_words(text), ["a", "of", "on"])
