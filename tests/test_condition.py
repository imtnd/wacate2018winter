import unittest
import context

import condition

class TestCondition(unittest.TestCase):
    def test_AisTrueReturnFalse(self):
        result = condition.checkAnd(True, False)
        self.assertEqual( result , False)

    def test_BisTrueReturnFalse(self):
        result = condition.checkAnd(False, True)
        self.assertEqual( result , False)






