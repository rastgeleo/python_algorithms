import unittest
import random

from karatsuba import karatsuba


class TestKaratsuba(unittest.TestCase):

    def test_base(self):
        self.assertEqual(karatsuba(8, 9), 72)

    def test_big_random(self):

        for _ in range(100):
            x = random.randint(10, 10000000)
            y = random.randint(10, 10000000)
            self.assertEqual(karatsuba(x, y), x*y)


if __name__ == '__main__':
    unittest.main()
