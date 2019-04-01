#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
        x1= math.floor(n/len(s))
        x2 = n - (len(s)*x1)
        num_a = (len(s) - len(s.replace("a","")))*x1
        s2 = s[:x2]
        num_a_2 = len(s2) - len(s2.replace("a",""))        
        return num_a + num_a_2
        
print(repeatedString("aba", 10)==7)

print(repeatedString("a", 1000000000000)==1000000000000)

