import unittest
from deep.list_to_lists import one_list_to_many_list


class MyTestCase(unittest.TestCase):

    def test_list_1(self):
        list = one_list_to_many_list([1, 2, 8, 3, 2, 4])
        self.assertEqual(list, [[1, 2, 8], [3], [2, 4]])

    def test_list_2(self):
        list = one_list_to_many_list([2,1,3,2])
        self.assertEqual(list, [[2], [1,3], [2]])

    def test_list_3(self):
        list = one_list_to_many_list([1,2,5,11,24,7,12,1,50,51,2,3])
        self.assertEqual(list, [[1,2,5,11,24], [7,12], [1,50,51], [2,3]])

    def test_list_4(self):
        list = one_list_to_many_list([1,2,3,1,2,33,1,2,2,2,2,3,3,3,2,2,3,2,4,6,8,234,432423,4234,2,3424,234,234234,423423,234234,134])
        self.assertEqual(list, [[1, 2, 3], [1, 2, 33], [1, 2], [2], [2], [2, 3], [3], [3], [2], [2, 3], [2, 4, 6, 8, 234, 432423], [4234], [2, 3424], [234, 234234, 423423], [234234], [134]])


if __name__ == '__main__':
    unittest.main()
