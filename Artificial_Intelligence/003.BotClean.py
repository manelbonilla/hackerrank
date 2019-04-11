#!/usr/bin/python

# Head ends here

def distance(p1, p2):
	return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def next_move(posr, posc, board):
	#dirty_cell = []
	#dir_dis = []
	min_dis = None
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
					dt = distance((posr, posc),(x, y))
					#dirty_cell.append((x, y))
					#dir_dis.append(dt)
					#print(dt, min_dis)
					if min_dis == None or min_dis > dt:
						min_dis = dt
						min_point = (x, y)
		#print(str(min_dis), str(min_point))
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
grid.append("----d")
grid.append("-d--d")
grid.append("--dd-")
grid.append("--d--")
grid.append("----d")
next_move(0, 1, grid)

grid = []
grid.append("d")
next_move(0, 0, grid)

####if __name__ == "__main__":
####    pos = [int(i) for i in input().strip().split()]
####    board = [[j for j in input().strip()] for i in range(5)]
####    next_move(pos[0], pos[1], board)
