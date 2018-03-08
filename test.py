import os
from TestRunner import TestRunner
import unittest


class MyTestCase(unittest.TestCase):
    def test_A(self):
        """A simple test that should PASS."""
        self.assertTrue(True)

    def test_B(self):
        """A simple test FAILURE."""
        self.assertFalse(True)

    @staticmethod
    def test_C():
        """A simple ERROR raising test."""
        assert 1 + 'a' == 32


if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    fp = os.path.join(os.path.dirname(__file__), "test.html")
    runner = TestRunner(stream=fp, title="My test report sample", description="This is a sample test case.")
    runner.run(test_suite)