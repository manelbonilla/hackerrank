#!/usr/bin/python


def nextMove(n,r,c,grid):
	botp = [r, c]
	prinp = [-1, -1]
	for x in range(0, n):
		for y in range(0, n):
			if grid[x][y] == 'p':
				prinp[0] = x
				prinp[1] = y
	#print("botp:", botp[0], botp[1])
	#print("prinp:", prinp[0], prinp[1])
	hp, vp = prinp[0]-r, prinp[1]-c
	#print("disp:", hp, vp)
	res = None
	if hp > 0:
		res = "DOWN"
	elif hp < 0:
		res = "UP"
	if vp > 0:
		res = "RIGHT"
	elif vp < 0:
		res = "LEFT"
	return res

#n = int(input())
#r,c = [int(i) for i in input().strip().split()]
#grid = []
#for i in range(0, n):
#    grid.append(input())

####5
####2 3
####-----
####-----
####p--m-
####-----
####-----

#CASO 1
n=5
r=2
c=3
grid = []
grid.append("-----".strip())
grid.append("-----".strip())
grid.append("p--m-".strip())
grid.append("-----".strip())
grid.append("-----".strip())

#CASO 2
####n=5
####r=4
####c=1
####grid = []
####grid.append("-----".strip())
####grid.append("-----".strip())
####grid.append("-----".strip())
####grid.append("-p---".strip())
####grid.append("-m---".strip())

print(nextMove(n,r,c,grid))
