__author__ = 'dinal'

import unittest
from Normalize import removeRedundantWhiteSpaces

class TestNormalize(unittest.TestCase):
    def test_space(self):
        self.assertEqual(removeRedundantWhiteSpaces(" \t f\t\t   o o\t"), 'f o o')

    def test_newline(self):
        self.assertEqual(removeRedundantWhiteSpaces('\nf\n\n\t\r\r\ro\t o'),'f o o')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNormalize)
    unittest.TextTestRunner(verbosity=2).run(suite)