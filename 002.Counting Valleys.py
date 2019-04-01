#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    init = 0
    valleys = 0
    for i in range(0, n):
        x = s[i]
#        print("[I]", "init:", init, "valleys:", valleys)
        if x == "U":
            if (init + 1) == 0:
                valleys += 1
            init += 1
        else:
            init -= 1
#        print("[F]", "x:", x, "init:", init, "valleys:", valleys)
    return valleys
    
    
t = "UDDDUDUU"
print(countingValleys(len(t),t))
