import random
import unittest

from merge_sortA import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_random_case(self):
        lst = random.sample(range(1, 100), 10)
        self.assertEqual(merge_sort(lst), sorted(lst))


if __name__ == '__main__':
    unittest.main()
