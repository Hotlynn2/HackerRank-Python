# Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

import math
import os
import random
import re
import sys

N = int(input())


if N % 2 == 1:
    print('Weird')
    
x = range(2,6)
if (N % 2 == 0) and (N in x):
    print('Not Weird')
        
Y = range(6,21)
if (N  % 2 == 0) and (N in Y):
    print('Weird')
              
if (N % 2 == 0) and N > 20:
    print('Not Weird')
        
    

