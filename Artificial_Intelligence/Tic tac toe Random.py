#!/bin/python3

import math
import os
import random
from random import shuffle
import re
import sys

def print_board(board):
	for r in board:
		for c in r:
			print(c, end='')
		print("")


def nextMove(player, board):
	available = []
	for i1 in range(3):
		for i2 in range(3):
			cell = board[i1][i2]
			if cell != 'X' and cell != 'O': available.append((i1, i2))
	shuffle(available)
	move = available[0]
	print(move[0], move[1])



if __name__ == '__main__':
    player = input().split()
    r1 = list(input())
    r2 = list(input())
    r3 = list(input())
    r = [ r1, r2, r3]
    nextMove(player, r)
    
#nextMove("X", [list("___"), list("___"), list("_XO")])
