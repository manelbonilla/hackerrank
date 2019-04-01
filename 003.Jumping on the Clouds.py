#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def jumpingOnClouds(c):
    jumps = 0
    pos = 0
    lenc = len(c)
    while pos < lenc:
        if pos+2<lenc and c[pos+2] == 0:
            jumps += 1
            pos += 2
        else:
            jumps += 1
            pos += 1
    return jumps -1
        
        
t = [ 0, 0, 0, 0, 1, 0 ]
print(jumpingOnClouds(t))
t = [ 0, 0, 1, 0 ]
print(jumpingOnClouds(t))
