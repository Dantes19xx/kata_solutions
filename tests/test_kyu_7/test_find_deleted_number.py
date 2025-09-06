from unittest import TestCase
from kyu_7.find_deleted_number import find_deleted_number


class TestFindDeletedNumber(TestCase):
    def test1(self):
        self.assertEqual(find_deleted_number([1,2,3,4,5], [3,4,1,5]), (2, 'Deletion'))
    
    def test2(self):
        self.assertEqual(find_deleted_number(
            [1,2,3,4,5,6,7,8,9], [1,9,7,4,6,2,3,8]),
            (5, 'Deletion')
        )
    
    def test3(self):
        self.assertEqual(find_deleted_number(
            [1,2,3,4,5,6,7,8,9], [5,7,6,9,4,8,1,2,3]),
            (0, 'No deletion')
        )
