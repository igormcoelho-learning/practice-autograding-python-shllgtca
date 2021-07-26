import unittest
from student import *


class ExampleTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,3), 6)
    def test_mul(self):
        self.assertEqual(mul(3,3), 9)


if __name__ == '__main__':
    unittest.main()