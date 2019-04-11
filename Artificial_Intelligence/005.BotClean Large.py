#!/usr/bin/python

# Head ends here

def distance(p1, p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


def next_move(posx, posy, dimx, dimy, board):
	min_dis = None
	min_point = None
	result = None
	if board[posx][posy] == 'd':
		result = "CLEAN"
	else:
		for x in range(0, dimx):
			for y in range(0, dimy):
				if board[x][y] == 'd':
					dt = distance((posx, posy),(x, y))
					if min_dis == None or min_dis > dt:
						min_dis = dt
						min_point = (x, y)
		if min_point[0] > posx:
			result = "DOWN"
		elif min_point[0] < posx:
			result = "UP"
		elif min_point[1] > posy:
			result = "RIGHT"
		else:
			result = "LEFT" 
	print(result)

# Tail starts here

grid = []
grid.append("-b--d")
grid.append("-d--d")
grid.append("--dd-")
grid.append("--d--")
grid.append("----d")
next_move(0, 1, 5, 5, grid)


####if __name__ == "__main__":
####    pos = [int(i) for i in input().strip().split()]
####    board = [[j for j in input().strip()] for i in range(5)]
####    next_move(pos[0], pos[1], board)
