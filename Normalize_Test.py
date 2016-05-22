# -*- coding: utf-8 -*-
__author__ = 'dinal'

import unittest
from Normalize import removeRedundantWhiteSpaces
from Normalize import toLowerCase
from Normalize import removePunctuations

class TestNormalize(unittest.TestCase):
    def test_removeRedundantWhiteSpaces(self):
        self.assertEqual(removeRedundantWhiteSpaces(" \t f\t\t   o o\t"), 'f o o')
        self.assertEqual(removeRedundantWhiteSpaces('\nf\n\n\t\r\r\ro\t o'),'f o o')

    def test_toLowerCase(self):
        self.assertEqual(toLowerCase('ABCDefg'), 'abcdefg')

    def test_toLowerCase_NonASCII(self):
        self.assertEqual(toLowerCase('Километ'), 'километ'.decode('utf-8'))

    def test_removePunctuations(self):
        self.assertEqual(removePunctuations('hello? are you there?'), 'hello are you there')
        self.assertEqual(removePunctuations('!()-[]{};:"\,<>./?@#$%^&*_~'), '')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNormalize)
    unittest.TextTestRunner(verbosity=2).run(suite)