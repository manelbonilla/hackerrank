#!/bin/python
from random import randint
import time

def createGrid(n, m, input):
	if n*m == len(input):
		grid = []
		ini = 0
		fini = m
		while fini <= len(input):
			grid.append(input[ini:fini])
			ini+=m
			fini+=m
		return grid
	else:
		return None

def printGrid(grid):
	for r in range(0, len(grid)):
		for c in range(len(grid[r])):
			print(grid[r][c], end='')
		print("")
		

def validMove(px, py, board):
		if px > 0 and px < 15 and py > 0 and py < 15 and board[px][py] == '-':
			return True
		else:
			return False

def nextMove_oldv1(player, x, y, board):
	arr_moves = ["RIGHT", "LEFT", "UP", "DOWN"]
	arr_var = [[0, 1], [0, -1], [-1, 0], [1, 0]]
	movido = False
	for z in range(0, 4):
		p = arr_var[z]
		npx, npy = x+p[0], y+p[1]
		#print("x", x, "y", y, "npx", npx, "npy", npy)
		if validMove(npx, npy, board):
			print(arr_moves[z])
			return npx, npy
			movido = True
		if movido:
			break
	if not movido:
		#print("Error, no posicion valida")
		return None, None

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
	recursivity_level = 7
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
		return None, None
	else:
		print(arr_moves[maxpp])
		return pmaxp[0], pmaxp[1]


def changeStringPos(grid, row, column, character):
	ts = grid[row]
	grid[row] = ts[:column]+character+ts[column+1:]
	return grid


def partida(rr, rc, gr, gc):
	timer, timeg = [], []
	input="################-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------################"
	grid = createGrid(15, 15, input)
	print("printGrid method:")
	printGrid(grid)
	round=1
	while round<20*20:
		startr = time.time()
		rr, rc = nextMove('r', rr, rc, grid)
		endr = time.time()
		startg = time.time()
		gr, gc = nextMove_oldv1('g', gr, gc, grid)
		endg = time.time()
		sr, sg = endr-startr, endg-startg
		print("Tiempo funcion nextMove:", sr, " tiempo funcion nextMove_oldv1:", sg)
		timer.append(sr)
		timeg.append(sg)
		#print(rr, rc, gr, gc)
		if (rr == None or gr == None):
			print("Hay un ganador")
			if (rr == None):
				print("Ha ganado g, round:", round)
			else:
				print("Ha ganado r, round:", round)
			printGrid(grid)
			break
		elif (rr == gr and rc == gc):
			print("DRAW, round:", round)
			printGrid(grid)
			break
		else:
			changeStringPos(grid, rr, rc, 'r')
			changeStringPos(grid, gr, gc, 'g')
			printGrid(grid)
		time.sleep(0.3)
		round += 1
	sumr, sumg = 0, 0
	for x in range(0, len(timer)):
		if timer[x] > 1:
			sumr += 1
		if timeg[x] > 1:
			sumg += 1
	print("sumr:", sumr, "sumg:", sumg)



x1, x2, x3, x4 = randint(1, 14), randint(1, 14), randint(1, 14), randint(1, 14)
while x1 == x3 or x2 == x4:
	x1, x2, x3, x4 = randint(1, 14), randint(1, 14), randint(1, 14), randint(1, 14)


#partida(4, 3, 5, 13)
partida(x1, x2, x3, x4)
