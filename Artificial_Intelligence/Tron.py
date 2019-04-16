#!/bin/python

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

def nextMove(player, x, y, board):
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

def changeStringPos(grid, row, column, character):
	ts = grid[row]
	grid[row] = ts[:column]+character+ts[column+1:]
	return grid

input="################-rr--------gg##-rr--------gg##-rr--------gg##-rr--------gg##-r---------g-##-r---------gg##rr----------g##-------------##-------------##-------------##-------------##-------------##-------------################"
grid = createGrid(15, 15, input)
print("printGrid method:")
printGrid(grid)
print("")

rr, rc, gr, gc = 4, 3, 5, 13

for round in range(1,100):
	print("")
	print("Round:", round)
	rr, rc = nextMove('r', rr, rc, grid)
	gr, gc = nextMove('g', gr, gc, grid)
	print(rr, rc, gr, gc)
	if (rr == None or gr == None):
		print("Hay un ganador")
		if (rr == None):
			print("Ha ganado g")
		else:
			print("Ha ganado r")
		printGrid(grid)
		break
	elif (rr == gr and rc == gc):
		print("DRAW")
		break
	else:
		changeStringPos(grid, rr, rc, 'r')
		changeStringPos(grid, gr, gc, 'g')
		printGrid(grid)



input="################-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------##-------------################"
grid = createGrid(15, 15, input)
print("printGrid method:")
printGrid(grid)
print("")

rr, rc, gr, gc = 4, 3, 5, 13

for round in range(1,100):
	print("")
	print("Round:", round)
	rr, rc = nextMove('r', rr, rc, grid)
	gr, gc = nextMove('g', gr, gc, grid)
	print(rr, rc, gr, gc)
	if (rr == None or gr == None):
		print("Hay un ganador")
		if (rr == None):
			print("Ha ganado g")
		else:
			print("Ha ganado r")
		printGrid(grid)
		break
	elif (rr == gr and rc == gc):
		print("DRAW")
		break
	else:
		changeStringPos(grid, rr, rc, 'r')
		changeStringPos(grid, gr, gc, 'g')
		printGrid(grid)
