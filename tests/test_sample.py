import unittest
import context

import sample

class TestSample(unittest.TestCase):
    def test_statement(self):
        result = sample.function(True, True)
        self.assertEqual( result , True)

    def test_condition1(self):
        result = sample.function(True, False)
        self.assertEqual( result , False)

    def test_condition2(self):
        result = sample.function(False, True)
        self.assertEqual( result , False)

    def test_branch1(self):
        result = sample.function(False, False)
        self.assertEqual( result , False)

    def test_branch2(self):
        result = sample.function(True, True)
        self.assertEqual( result , True)



