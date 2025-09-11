from unittest import TestCase
from kyu_8.switch_it_up import switch_it_up


class TestSwitch(TestCase):
    def test1(self):
        self.assertEqual(switch_it_up(0), "Zero")
    
    def test2(self):
        self.assertEqual(switch_it_up(9), "Nine")
