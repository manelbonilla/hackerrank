#!/usr/bin/env python

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

input="######---##---##---######"
print("input:", input)
print("")

grid = createGrid(5, 5, input)
print("grid:", str(grid))
print("")

print("printGrid method:")
printGrid(grid)
print("")
