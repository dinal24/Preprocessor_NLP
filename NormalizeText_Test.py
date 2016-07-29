__author__ = 'Mursith'

import unittest
from NormalizeText import expandContractions
from NormalizeText import removeIntraPunctuation

class TestNormalizeText(unittest.TestCase):
    def test_expandContractions(self):
        self.assertEqual(expandContractions("isn't"), 'is not')
        self.assertEqual(expandContractions("who's"),'who is')
		
    def test_removeIntraPunctuation(self):
        self.assertEqual(removeIntraPunctuation("Dr. Wallace lives on St. John."), 'Dr Wallace lives on St John.')
        self.assertEqual(removeIntraPunctuation("1.5 million."), '1.5 million.')
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNormalizeText)
    unittest.TextTestRunner(verbosity=2).run(suite)