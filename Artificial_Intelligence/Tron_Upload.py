#!/bin/python
from random import randint
import time

def validMove(px, py, board):
		if px > 0 and px < 15 and py > 0 and py < 15 and board[px][py] == '-':
			return True
		else:
			return False

def puntua_point(x, y, board, n):
	points = 0
	if validMove(x, y, board):
		arr_var = [[0, 1], [0, -1], [-1, 0], [1, 0]]
		points = 1
		if n == 0:
			for pp in range(0, 4):
				xp, yp = x+arr_var[pp][0], y+arr_var[pp][1]
				if validMove(xp, yp, board):
					points += 1
		else:
			for pp in range(0, 4):
				xp, yp = x+arr_var[pp][0], y+arr_var[pp][1]
				points += puntua_point(xp, yp, board, n-1)
	return points

def nextMove(player, x, y, board):
	recursivity_level = 8
	arr_moves = ["RIGHT", "LEFT", "UP", "DOWN"]
	arr_var = [[0, 1], [0, -1], [-1, 0], [1, 0]]
	maxp = None
	maxpp = None
	pmaxp = None
	movido = False
	for z in range(0, 4):
		p = arr_var[z]
		npx, npy = x+p[0], y+p[1]
		if validMove(npx, npy, board):
			puntuation = puntua_point(npx, npy, board, recursivity_level)
			if maxp == None or puntuation > maxp:
				maxp = puntuation
				maxpp = z
				pmaxp = [npx, npy]
	if maxp == None:
		print("Ningun Movimiento Valido")
	else:
		print(arr_moves[maxpp])



player = input()
pos = input().split()
x1, x2, x3, x4 = int(pos[0]), int(pos[1]), int(pos[2]), int(pos[3])

grid = []
for x in range(0, 15):
	row = input()
	grid.append(row)

if player == 'r':
	nextMove(player, x1, x2, grid)
else:
	nextMove(player, x3, x4, grid)

