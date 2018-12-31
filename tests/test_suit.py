import unittest

import test_statement
import test_decision
import test_condition
import test_sample
import test_ticketValue

def suite():
  suite = unittest.TestSuite()
  suite.addTest(test_statement.TestStatement('test_statement'))
  suite.addTest(test_decision.TestDecision('test_evenNumber'))
  suite.addTest(test_decision.TestDecision('test_oddNumber'))
  suite.addTest(test_condition.TestCondition('test_AisTrueReturnFalse'))
  suite.addTest(test_condition.TestCondition('test_BisTrueReturnFalse'))
#  suite.addTest(test_sample.TestSample('test_statement'))
#  suite.addTest(test_sample.TestSample('test_condition1'))
#  suite.addTest(test_sample.TestSample('test_condition2'))
  suite.addTest(test_sample.TestSample('test_branch1'))
  suite.addTest(test_sample.TestSample('test_branch2'))
#  suite.addTest(test_ticketValue.TestTicketValue('test_statement'))
  suite.addTest(test_ticketValue.TestTicketValue('test_condition1'))
  suite.addTest(test_ticketValue.TestTicketValue('test_condition2'))
#  suite.addTest(test_ticketValue.TestTicketValue('test_branch1'))
#  suite.addTest(test_ticketValue.TestTicketValue('test_branch2'))


  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  test_suite = suite()
  runner.run(test_suite)
