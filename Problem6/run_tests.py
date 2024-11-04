import sys
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
  outfile = sys.argv[1]
  suite = unittest.defaultTestLoader.discover('tests')
  with open(outfile, 'w') as f:
    JSONTestRunner(stream=f, stdout_visibility="visible").run(suite)