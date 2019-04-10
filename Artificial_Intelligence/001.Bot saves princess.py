#!/usr/bin/python

def displayPathtoPrincess(n,grid):
	botp = [-1, -1]
	prinp = [-1, -1]
	for x in range(0, n):
		for y in range(0, n):
			z = grid[x][y]
			if z == 'm':
				botp[0] = x
				botp[1] = y
			if z == 'p':
				prinp[0] = x
				prinp[1] = y
	#print("botp:", botp[0], botp[1])
	#print("prinp:", prinp[0], prinp[1])
	disp = [prinp[0]-botp[0], prinp[1]-botp[1]]
	#print("disp:", disp[0], disp[1])

	if disp[0] > 0:
		for x in range(0, disp[0]):
			print("DOWN")
	elif disp[0] < 0:
		for x in range(disp[0], 0):
			print("UP")
	if disp[1] > 0:
		for x in range(0, disp[1]):
			print("RIGHT")
	elif disp[1] < 0:
		for x in range(disp[1], 0):
			print("LEFT")



#m = int(input())
#grid = [] 
#for i in range(0, m): 
#    grid.append(input().strip())

grid = []
m=3
grid.append("---")
grid.append("-m-")
grid.append("p--")

displayPathtoPrincess(m,grid)
