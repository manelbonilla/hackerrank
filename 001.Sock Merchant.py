#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    ar.sort()
    last = None
    pair = 0
    for i in ar:
        if last == i:
            pair += 1
            last = None
        else:
            last = i
    return pair

t2 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
t1 = len(t2)

print(sockMerchant(t1, t2))
