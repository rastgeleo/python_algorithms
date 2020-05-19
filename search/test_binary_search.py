import unittest
import random
from binary_search import do_search


class TestBinarySearch(unittest.TestCase):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
              31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def test_fixed_input(self):
        self.assertEqual(do_search(self.primes, 59), self.primes.index(59))

    def test_outside_value(self):
        self.assertEqual(do_search(self.primes, 81), -1)

    def test_random_input(self):
        choice = random.choice(self.primes)
        self.assertEqual(
                         do_search(self.primes, choice),
                         self.primes.index(choice)
                         )


if __name__ == '__main__':
    unittest.main()
