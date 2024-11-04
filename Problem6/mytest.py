# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:10:28 2024

@author: tomke
"""

import MontyHall as mh
fun = dir(mh)
if 'game' in fun:
    print("Contains necessary function")
else:
    print("Missing necessary function")
    
prob = mh.game(1000)
print(prob)