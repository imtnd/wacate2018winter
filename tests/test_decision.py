import unittest
import context

import decision

class TestDecision(unittest.TestCase):
    def test_evenNumber(self):
        result = decision.checkEvenNumber(10)
        self.assertEqual( result , True)

    def test_oddNumber(self):
        result = decision.checkEvenNumber(1)
        self.assertEqual( result , False)



