#!/usr/bin/python3

import collatz
import unittest


class testCollatz(unittest.TestCase):
    def test_values(self):
        self.assertEqual(collatz.collatz(3), 10)

if __name__ == '__main__':
    unittest.main()
