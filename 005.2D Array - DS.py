#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = None
    for x in range(1,5):
        for y in range(1,5):
            suma = arr[x][y] + arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1] + arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]
            if max == None or suma > max: max = suma
    return max


#Input
#-9 -9 -9  1 1 1 
# 0 -9  0  4 3 2
#-9 -9 -9  1 2 3
# 0  0  8  6 6 0
# 0  0  0 -2 0 0
# 0  0  1  2 4 0

#Output
#28
    

#Input 2
#-1 -1 0 -9 -2 -2
#-2 -1 -6 -8 -2 -5
#-1 -1 -1 -2 -3 -4
#-1 -9 -2 -4 -4 -5
#-7 -3 -3 -2 -9 -9
#-1 -3 -1 -2 -4 -5

#Expected -6
arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
print(hourglassSum(arr))
