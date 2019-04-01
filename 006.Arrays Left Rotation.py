#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    for x in range(0, d):
        a.append(a.pop(0))
    return a
    
#Input
#2
# 1, 2, 3, 4   
#Expected Output
#3, 4, 1, 2

list = [1, 2, 3, 4]
print(str(rotLeft(list, 2)))
