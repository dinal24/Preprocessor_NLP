__author__ = 'Januka Samaranayake'

import unittest
from Spell_Correction import spellCorrect

class TestSpellCorrection(unittest.TestCase):
    def test_pellCorrect(self):
        self.assertEqual(spellCorrect("tha"), "that")
        self.assertEqual(spellCorrect("foq"), "for")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpellCorrection)
    unittest.TextTestRunner(verbosity=2).run(suite)