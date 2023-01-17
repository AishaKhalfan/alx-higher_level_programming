#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def testAssertMax(self):
        self.assertEqual(max_integer([5, 3, 2]), 5)
        self.assertEqual(max_integer([4, 6, 7]), 7)
        self.assertEqual(max_integer([7, 8, 5]), 8)
        self.assertEqual(max_integer([6, 3, 4]), 6)
        self.assertEqual(max_integer([-4, -5, -8]), -4)
        self.assertEqual(max_integer([-4]), -4)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 2, 9]), 9)
        self.assertEqual(max_integer([10, 2, 7]), 10)

    def test_empty(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
