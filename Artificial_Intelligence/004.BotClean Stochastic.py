#!/bin/python3

def distance(p1, p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def nextMove(posr, posc, board):
	min_point = None
	maxr=len(board)
	result = None
	if board[posr][posc] == 'd':
		result = "CLEAN"
	else:
		for x in range(0, maxr):
			maxc=len(board[x])
			for y in range(0, maxc):
				if board[x][y] == 'd':
					min_point = (x, y)
					break
			if min_point != None:
				break
		if min_point[0] > posr:
			result = "DOWN"
		elif min_point[0] < posr:
			result = "UP"
		elif min_point[1] > posc:
			result = "RIGHT"
		else:
			result = "LEFT"
	print(result)

# Tail starts here

grid = []
grid.append("b---d")
grid.append("-----")
grid.append("-----")
grid.append("-----")
grid.append("-----")
nextMove(0, 1, grid)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
