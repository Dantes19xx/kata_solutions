from unittest import TestCase
from kyu_6.spin_words import spin_words

class TestSpinWords(TestCase):
    def test_single_word(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("to"), "to")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")

    def test_multiple_words(self):
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
