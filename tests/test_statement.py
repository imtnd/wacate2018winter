import unittest
import context

import statement

class TestStatement(unittest.TestCase):
    def test_statement(self):
        result = statement.add(2, 3)
        self.assertEqual( result , 5)


