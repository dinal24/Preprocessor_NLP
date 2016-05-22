__author__ = 'Januka'

import unittest
from Spell_Correction import spellCorrect

class TestSpellCorrection(unittest.TestCase):
    def test_pellCorrect(self):
        self.assertEqual(spellCorrect("hellp"), "help")
        self.assertEqual(spellCorrect("hell"), "hell")
        self.assertEqual(spellCorrect("helli"), "hell i")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpellCorrection)
    unittest.TextTestRunner(verbosity=2).run(suite)