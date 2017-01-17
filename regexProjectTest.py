#! /usr/bin/python3
# Test cases for regexProject.py

import regexProject
import unittest


# Test input
class testRegProject(unittest.TestCase):
    def test_values(self):
        self.assertEqual(regexProject.urlFunc('adlfkj http://www.test.com fe'
                                              'dfa $% dfad.'), 'http://www'
                         '.test.com')
        self.assertEqual(regexProject.dateFunc('2112-02-13'), '02.13.2112')
        self.assertEqual(regexProject.dateFunc('03/14/2112'), '03.14.2112')
        self.assertEqual(regexProject.sensFunc('111-11-1111'), '***-**-****')
        self.assertEqual(regexProject.doubleFunc('this this  is a test..??!!'),
                         'this is a test.?!')


if __name__ == '__main__':
    unittest.main()
