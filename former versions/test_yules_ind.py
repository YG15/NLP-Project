# This following code is a test to check yules_ind function work as expected
# Author: Yonathan Guttel
# Date: 12.11.2017
# Version: 1

import unittest
from  yules_ind import yules_ind

class MyTestCase(unittest.TestCase):
    def test_zeros_char(self):
        self.assertEqual(yules_ind(""), (None, None))

    def test_one_char(self):
        self.assertEqual(yules_ind("Good?"), (None, None))

    def test_two_char(self):
        self.assertEqual(yules_ind("Not good?"), (None, None))

    def test_three_dif_char(self):
        self.assertEqual(yules_ind("This is good!"), (None, None))

    def test_three_char(self):
        self.assertEqual(yules_ind("No?!?, I was sure this is good!, I hope this is better!"), (9.0, 1111.11))


if __name__ == '__main__':
    unittest.main()
