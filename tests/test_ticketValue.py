import unittest
import context

import ticketValue

class TestTicketValue(unittest.TestCase):
    def test_statement(self):
        result = ticketValue.determineValue(19, True)
        self.assertEqual( result , 1000)

    def test_condition1(self):
        result = ticketValue.determineValue(19, False)
        self.assertEqual( result , 1200)

    def test_condition2(self):
        result = ticketValue.determineValue(20, True)
        self.assertEqual( result , 1200)

    def test_branch1(self):
        result = ticketValue.determineValue(19, True)
        self.assertEqual( result , 1000)

    def test_branch2(self):
        result = ticketValue.determineValue(20, False)
        self.assertEqual( result , 1200)



