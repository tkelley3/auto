import os
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, partial_credit


class TestFilesExist(unittest.TestCase):

  @weight(1)
  @visibility('visible')
  def test_filesexist(self):
    reqd_files = ['fun.py']
    base = '/autograder/source/'
    for file in reqd_files:
        to_check = os.path.join(base, file)
        self.assertTrue(os.path.isfile(to_check), msg="Required file " + file + " does not exist")


if __name__ == "__main__":
  unittest.main()
