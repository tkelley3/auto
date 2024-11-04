import os
import unittest
from unittest import mock
from gradescope_utils.autograder_utils.decorators import weight, visibility, partial_credit

import numpy as np

class TestEncryption(unittest.TestCase):

  @weight(1)
  @visibility("visible")
  @unittest.mock.patch("encryption.input", create=True)
  def test_encryption(self, mocked_input):
      #opens input file for input value to test
      input_file = open("input.txt", "r")
      input_val = input_file.readline()

      print(input_val)

      """
      Can iterate over input_val if you want to test multiple values!
      """

      # mocks the built-in input() function so that it does not take in a command-line arg
      mocked_input.side_effect = [input_val, "done"]

      # run the student's code
      import encryption

      print(os.path.getsize("encrypted.txt"))

      f = open("encrypted.txt", "r")
      f.seek(0) #Unecessary but important if file was manipulated before reading
      if f.read() == "":
          print("No data found in output 'encrypted.txt' file")
      else:
          print("Data present in output 'encrypted.txt' file")
      
      # runs check to see if the student's output file is not empty
      self.assertNotEqual(os.path.getsize("encrypted.txt"), 0,
                          msg="No Data found in output 'encrypted.txt' file")
    
if __name__ == "__main__":
  unittest.main()

