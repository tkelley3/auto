"""
Expected output:
t = 6.21 s, maxh = 61.5 m , range = 349 m, final velocity = 66.1 m/s

Student output in form of:
v_f, range, time, height
"""

import math as math
import matplotlib.pyplot as plt
import os
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, partial_credit
import fun
import numpy as np

class TestProjectile(unittest.TestCase):

  @weight(1)
  @visibility('visible')
  def test_projectile(self):

    # input to test
    # For a projectile launched with a velocity of 62 m/s
    # at an angle of 25 degrees from a height of 26.5 m:
    input_velocity = 62
    input_angle = 25
    input_height = 26.5
      
    # obtains student's results from program (should be returned as a value)
    student_result = fun.projectile(input_velocity, input_angle, input_height)
    
    # target values
    target_values = np.array([66.06, 349, 6.21, 61.5])

    #tolerance that is 10 integers, but can be adjusted as needed!
    tolerance = 3

    # runs check to see if the student's result and expected orbits within tolerance
    for i,student_val in enumerate(student_result):
        self.assertLessEqual(abs(student_val - target_values[i]), tolerance,
                                msg=f"Student Result {student_val} and Target {target_values[i]} value are not \
                                equal to within {tolerance} integers.")      

if __name__ == "__main__":
  unittest.main()
