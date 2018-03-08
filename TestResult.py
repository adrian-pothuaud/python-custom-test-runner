# -*- coding:utf-8 -*-
"""CustomTestRunner.TestResult

This module provides a customized TestResult class.

Todo:
    * finish writing TestResult class
    * tests

__author__ = 'adrianpothuaud'

"""

import sys
import unittest

DEBUG = True


# ----- Attributes for Easy Modifications
test_states = {
    "pass": "PASSED",
    "fail": "FAILED",
    "err": "ERROR"
}
"""test_states

An attribute to store test states for easier modification.
Used by TestResult.add_success, TestResult.add_error and TestResult.add_failure.
"""
# Attributes for Easy Modifications -----


class TestResult(unittest.TestResult):
    """A Custom Test Result object.

    Used by CustomTestRunner
    """
    def __init__(self, stream):
        if DEBUG:
            sys.stdout.write("Test result init...\n")
        unittest.TestResult.__init__(self)
        self.stream = stream
        self.tests = []
        self.current_test = None

    @staticmethod
    def get_description(test):
        """Returns a test description.

        :param test:
        :return:
        """
        if DEBUG:
            sys.stdout.write("Test result getting test description...\n")
        return test.shortDescription() or str(test)

    def startTest(self, test, **kwargs):
        """Test start process.

        :param test:
        :return:
        """
        if DEBUG:
            sys.stdout.write("Test result starting test...\n")
        self.current_test = dict()
        unittest.TestResult.startTest(self, test)
        self.current_test["abstract"] = str(test)
        self.current_test["description"] = self.get_description(test)

    def addSuccess(self, test):
        """Processing a test success.

        :param test:
        :return:
        """
        if DEBUG:
            sys.stdout.write("Test result add test success...\n")
        unittest.TestResult.addSuccess(self, test)
        self.current_test["state"] = test_states["pass"]
        self.tests.append(self.current_test)
        self.current_test = None

    def addError(self, test, err):
        """Processing a test error.

        :param err:
        :param test:
        :return:
        """
        if DEBUG:
            sys.stdout.write("Test result add test error...\n")
        unittest.TestResult.addError(self, test, err)
        self.current_test["state"] = test_states["err"]
        self.current_test["error"] = err
        self.tests.append(self.current_test)
        self.current_test = None

    def addFailure(self, test, err):
        """Processing a test failure.

        :param err:
        :param test:
        :return:
        """
        if DEBUG:
            sys.stdout.write("Test result add test failure...\n")
        unittest.TestResult.addFailure(self, test, err)
        self.current_test["state"] = test_states["fail"]
        self.current_test["failure"] = err
        self.tests.append(self.current_test)
        self.current_test = None
