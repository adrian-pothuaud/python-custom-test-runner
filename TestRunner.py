# -*- coding:utf-8 -*-
"""CustomTestRunner.TestRunner

This module provides a customized TestRunner class.

Todo:
    * finish writing TestRunner class
    * tests

__author__ = 'adrianpothuaud'

"""

from jinja2 import Environment, PackageLoader, select_autoescape
import TestResult
import time
import sys

DEBUG = True


class TestRunner:
    """A test runner class that displays results in HTML form.

    To be improved...
    """

    def __init__(self, stream, title, description):
        if DEBUG:
            sys.stdout.write("Test runner init...\n")
        self.stream = stream
        self.title = title
        self.description = description

    def _makeHTML(self, time_taken, tests):
        if DEBUG:
            sys.stdout.write("Test runner making HTML output file...\n")
        env = Environment(
            loader=PackageLoader('CustomTestRunner', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('reportTemplate.html')
        output = template.render(tests=tests, time_taken=time_taken, title=self.title, description=self.description)
        with open(self.stream, "w") as f:
            f.write(output)

    def _makeResult(self):
        if DEBUG:
            sys.stdout.write("Test runner making result...\n")
        return TestResult.TestResult(self.stream)

    def run(self, test):
        """Run a test case or test suite.

        :param test:
        :return:
        """
        if DEBUG:
            sys.stdout.write("Test runner running...\n")
        result = self._makeResult()
        start_time = time.time()
        test(result)
        stop_time = time.time()
        time_taken = stop_time - start_time
        run = result.testsRun
        self._makeHTML(time_taken, result.tests)
        return result
