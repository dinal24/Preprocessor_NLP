__author__ = 'Januka'

import unittest
from Spell_Correction import spellCorrect

class TestSpellCorrection(unittest.TestCase):
    def test_pellCorrect(self):
        self.assertEqual(spellCorrect("helo"), "hole")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpellCorrection)
    unittest.TextTestRunner(verbosity=2).run(suite)