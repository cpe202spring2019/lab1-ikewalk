import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """ Tests max_list_iter with empty list, none type, list length of one, longer list, shorter list,
         list with two max values in different locations, and a list with all of the same max values, and one value """
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        elist = []
        self.assertEqual(max_list_iter(elist), None)
        self.assertEqual(max_list_iter([1]), 1)
        m_list = [5, 8, 3, 18, 36, 10, 7]
        self.assertEqual(max_list_iter(m_list), 36)
        m_list = [5, 8, 3]
        self.assertEqual(max_list_iter(m_list), 8)
        m_list = [5, 3, 8]
        self.assertEqual(max_list_iter(m_list), 8)
        m_list = [8, 5, 3]
        self.assertEqual(max_list_iter(m_list), 8)
        m_list = [8, 8, 3]
        self.assertEqual(max_list_iter(m_list), 8)
        m_list = [3, 8, 8]
        self.assertEqual(max_list_iter(m_list), 8)
        m_list = [8, 8, 8]
        self.assertEqual(max_list_iter(m_list), 8)
        self.assertEqual(max_list_iter([8]), 8)

    def test_reverse_rec(self):
        """ Tests reverse_rec with different values, checks against something that it is not equal to, empty list,
         none type, and with a string """
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([7, 3, 8, 9]), [9, 8, 3, 7])
        self.assertNotEqual(reverse_rec([7, 3, 8, 9]), [3, 8, 9, 7])
        self.assertEqual(reverse_rec([]), None)
        self.assertEqual(reverse_rec([1]), [1])
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        str_list = ['s', 't', 'r', 'i', 'n', 'g']
        self.assertEqual(reverse_rec(str_list), ['g', 'n', 'i', 'r', 't', 's'])

    def test_bin_search(self):
        """ Tests bin_search with a none type, empty list, values not in the list, values in the list, but not in range,
          tests one of the worst case searches, tests with a string, and with one value in the list """
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(12, 0, 3, list_val), None)
        self.assertEqual(bin_search(-1, 0, 8, list_val), None)
        self.assertEqual(bin_search(5, 0, 3, list_val), None)
        self.assertEqual(bin_search(9, 0, 10, list_val), 7)
        self.assertEqual(bin_search(9, 0, 10, []), None)
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(9, 0, 10, None)
        str_list = ['s', 't', 'r', 'i', 'n', 'g']
        self.assertEqual(bin_search('n', 0, len(list_val) - 1, str_list), 4)
        self.assertEqual(bin_search(4, 0, 1, [4]), 0)
        self.assertEqual(bin_search(4, 0, 10, [4]), 0)
        self.assertEqual(bin_search(6, 0, 1, [4]), None)


if __name__ == "__main__":
    unittest.main()
