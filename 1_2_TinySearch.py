
# coding: utf-8

# In[52]:

#edgeCost.py
import sys
sys.setrecursionlimit(100000)
from urllib.request import urlopen
import numpy as np
import queue

def edgeCost(starting, dest, maze):
	visitmap = [[0 for x in range(len(maze[0]))] for y in range(len(maze))]
	path_cost = 0
	node_number = 0
	frontier = queue.PriorityQueue()
	frontier.put(starting)

	return astar_edge(dest, visitmap, path_cost, node_number, frontier, maze)



def astar_edge(dest, visitmap, path_cost, node_number, frontier, maze):

	if frontier.empty():
		return 0

	cur = frontier.get()
	node_number += 1
	visitmap[cur[1]][cur[2]] = 1

	if (cur[1] == dest[1]) & (cur[2] == dest[2]):
		path = []
		while (cur[3] != None):
			pos = [cur[1], cur[2]]
			cur = cur[3]
			path.append(pos)
		for element in path:
			path_cost += 1
		return path_cost

	#go left
	if (maze[cur[1]][cur[2] - 1]!='%') & (visitmap[cur[1]][cur[2] - 1]==0):
		h = abs(dest[1] - cur[1]) + abs(dest[2] - (cur[2]-1)) + cur[4]
		childleft = (h, cur[1], cur[2]-1, cur, cur[4]+1)
		visitmap[cur[1]][cur[2]-1] = 1
		frontier.put(childleft)

	#go right
	if (maze[cur[1]][cur[2] + 1]!='%') & (visitmap[cur[1]][cur[2] + 1]==0):
		h = abs(dest[1] - cur[1]) + abs(dest[2] - (cur[2]+1)) + cur[4]
		childright = (h, cur[1], cur[2]+1, cur, cur[4]+1)
		visitmap[cur[1]][cur[2]+1] = 1
		frontier.put(childright)

	#go down
	if (maze[cur[1] + 1][cur[2]]!='%') & (visitmap[cur[1] + 1][cur[2]]==0):
		h = abs(dest[1] - (cur[1]+1)) + abs(dest[2] - cur[2]) + cur[4]
		childdown = (h, cur[1]+1, cur[2], cur, cur[4]+1)
		visitmap[cur[1]+1][cur[2]] = 1
		frontier.put(childdown)
		
	#go up
	if (maze[cur[1] - 1][cur[2]]!='%') & (visitmap[cur[1] - 1][cur[2]]==0):
		h = abs(dest[1] - (cur[1]-1)) + abs(dest[2] - cur[2]) + cur[4]
		childup = (h, cur[1]-1, cur[2], cur, cur[4]+1)
		visitmap[cur[1]-1][cur[2]] = 1
		frontier.put(childup)

	return astar_edge(dest, visitmap, path_cost, node_number, frontier, maze)

#astarDistDict.py
def dots(M):
	dots = []
	index = 0
	#Every time we find a '.', add it to the list.
	for i in range(len(M.maze)):
		for j in range(len(M.maze[0])):
			if M.maze[i][j] == '.':
				#(index, row, column)
				d = (index, i, j)
				dots.append(d)
				index += 1

	return dots



def astarDistDict(dots, maze):
	dictionary = {}
	l = len(dots)

	for i in range(l):
		for j in range(i):
			posi = str((dots[i][1], dots[i][2]))
			posj = str((dots[j][1], dots[j][2]))

			starting = (10000, dots[i][1], dots[i][2], None, 0)
			dest = (0, dots[j][1], dots[j][2], None, 0)
			dist = edgeCost(starting, dest, maze)

			addtwodimdict(dictionary, posi, posj, dist)
			addtwodimdict(dictionary, posj, posi, dist)

	for i in range(len(maze)):
		for j in range(len(maze[0])):
			if maze[i][j] == 'P' or maze[i][j] == ' ':
				for k in range(l):
					posCur = str((i,j))
					posDot = str((dots[k][1], dots[k][2]))

					starting = (10000, i,j, None, 0)
					dest = (0, dots[k][1], dots[k][2], None, 0)
					dist = edgeCost(starting, dest, maze)

					addtwodimdict(dictionary, posCur, posDot, dist)
					addtwodimdict(dictionary, posDot, posCur, dist)

	return dictionary



#ref: http://blog.csdn.net/byres/article/details/47287961
def addtwodimdict(thedict, key_a, key_b, val): 
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

#heuristic.py
import sys
sys.setrecursionlimit(100000)
from urllib.request import urlopen
import numpy as np
import queue

def visitDotsDict(dots):
	dictionary = {}
	for i in range(len(dots)):
		dictionary[str((dots[i][1], dots[i][2]))] = 0
	return dictionary

def heuristic(curRow, curCol, dots, visitDots, astarDist, maze):

	posCur = str((curRow, curCol))
	if maze[curRow][curCol] == '.':
		visitDots[posCur] = 2
	
	dotsLeft = []
	for i in range(len(dots)):
		pos = str((dots[i][1], dots[i][2]))
		if visitDots[pos] == 0:
			dotsLeft.append(dots[i])
    
	l = len(dotsLeft) + 1
	A = [[0 for i in range(l)]for j in range(l)]

	for i in range(l):
		for j in range(i):
			#Distance of the point with itself 
			if i == j:
				A[i][j] = 0

			if i>=1 and j == 0:
				posCur = str((curRow, curCol))
				posDot = str((dotsLeft[i-1][1], dotsLeft[i-1][2]))
				edgeCost = abs(curRow-dotsLeft[i-1][1])+abs(curCol-dotsLeft[i-1][2])
				A[i][j] = edgeCost
				A[j][i] = edgeCost
			
			if i>0 and j>0 and i != j:
				posi = str((dotsLeft[i-1][1], dotsLeft[i-1][2]))
				posj = str((dotsLeft[j-1][1], dotsLeft[j-1][2]))
				edgeCost = astarDist[posi][posj]
				A[i][j] = edgeCost
				A[j][i] = edgeCost

	#Prim Algorithm to calculate the minimum total edge cost
	#refer: http://blog.csdn.net/heisediwei/article/details/50326847
	adjvex = np.zeros(l)
	adjvex[0] = 1
	lowCost = A[0]
	lowCost[0] = 0
	count = 0

	while (count < l):
		I = (np.argsort(lowCost))[count]
		adjvex[I] = lowCost[I]
		lowCost[I] = 0
		lowCost = np.array(list(map(lambda x,y:x if x<y else y, lowCost, A[I])))
		count += 1

	return sum(adjvex)


# In[54]:

import sys
sys.setrecursionlimit(100000)
from urllib.request import urlopen
import numpy as np
import queue
import copy

class M:
	def __init__(self, name):
		URL = "http://slazebni.cs.illinois.edu/fall17/assignment1/"+name+".txt"

		#Change the maze-txt to a 2-d array, call it self.maze
		response = urlopen(URL)
		lines = response.readlines()
		bitlist = [i.rstrip() for i in lines]
		strlist = [k.decode('ascii') for k in bitlist]
		charlist = [list(j) for j in strlist]
		self.maze = np.asarray(charlist)
		for i in range(len(self.maze)):
			for j in range(len(self.maze[0])):
				if self.maze[i][j] == 'P':
					#(heuristic + path_cost, row, column, parent, path_cost)
					self.current = (10000, i, j, None, 0)
					#print(self.current)
		self.visitmap = [[0 for x in range(len(self.maze[0]))] for y in range(len(self.maze))]
		self.dots = dots(self)
		self.visitDots = visitDotsDict(self.dots)
		self.astarDist = astarDistDict(self.dots, self.maze)
		self.path_cost = 0
		self.node_number = 0
		self.frontier = queue.PriorityQueue()
		self.frontier.put(self.current)


	def astar(self,count):
		if self.frontier.empty():
			return
		self.current = self.frontier.get()
		self.node_number += 1
		#print("current:",self.current)
		curRow = self.current[1]
		curCol = self.current[2]
		posCur = str((curRow, curCol))
		self.visitmap[curRow][curCol] = 1

		if (self.maze[curRow][curCol] == '.') and (self.visitDots[posCur] == 0):
			count += 1
			self.visitDots[posCur] = count
			self.maze[curRow][curCol]==' '
			self.frontier=queue.PriorityQueue()       
			self.visitmap = [[0 for x in range(len(self.maze[0]))] for y in range(len(self.maze))]
			#print(self.current)            
			dotsLeft = []
			for i in range(len(self.dots)):
				pos = str((self.dots[i][1], self.dots[i][2]))
				if self.visitDots[pos] == 0:
					dotsLeft.append(self.dots[i])
			#print(len(dotsLeft))
			if len(dotsLeft) == 0:
				path = []
				#self.path_cost=self.current[4]               
				while (self.current[3] != None):
					pos = [self.current[1], self.current[2]]
					self.current = self.current[3]
					path.append(pos)
				return path


		tmp = copy.deepcopy(self.visitDots)
		#go left
		if (self.maze[curRow][curCol - 1]!='%') & (self.visitmap[curRow][curCol - 1]==0):
			h = heuristic(curRow, curCol-1, self.dots, tmp, self.astarDist, self.maze) + self.current[4]
			#h = self.current[4]
			childleft = (h, curRow, curCol-1, self.current, self.current[4]+1)
			self.visitmap[curRow][curCol - 1] = 1
			self.frontier.put(childleft)

		tmp = copy.deepcopy(self.visitDots)
		if (self.maze[curRow][curCol + 1]!='%') & (self.visitmap[curRow][curCol + 1]==0):
			h = heuristic(curRow, curCol+1, self.dots, tmp, self.astarDist, self.maze) + self.current[4]
			#h = self.current[4]
			childright = (h, curRow, curCol+1, self.current, self.current[4]+1)
			self.visitmap[curRow][curCol + 1] = 1
			self.frontier.put(childright)

		tmp = copy.deepcopy(self.visitDots)
		if (self.maze[curRow + 1][curCol]!='%') & (self.visitmap[curRow+1][curCol]==0):
			h = heuristic(curRow+1, curCol, self.dots, tmp, self.astarDist, self.maze) + self.current[4]
			#h = self.current[4]
			childdown = (h, curRow+1, curCol, self.current, self.current[4]+1)
			self.visitmap[curRow + 1][curCol] = 1
			self.frontier.put(childdown)

		tmp = copy.deepcopy(self.visitDots)
		if (self.maze[curRow - 1][curCol]!='%') & (self.visitmap[curRow-1][curCol]==0):
			h = heuristic(curRow-1, curCol, self.dots, tmp, self.astarDist, self.maze) + self.current[4]
			#h = self.current[4]
			childup = (h, curRow-1, curCol, self.current, self.current[4]+1)
			self.visitmap[curRow - 1][curCol] = 1
			self.frontier.put(childup)

		return self.astar(count)





	def printmaze(self,name):

		l = len(self.dots)
		
		#Since the maze-txt can only displace 1 character, the count larger than 9 will be replaced by letters.
		dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		
		path = self.astar(0)
		label = ''
		#print(path)
		for element in path:
			#self.maze[element[0]][element[1]]=i         
			self.path_cost+=1
		if (len(self.dots)<100):
			for i in range(l):
				pos = str((self.dots[i][1], self.dots[i][2]))
				order = self.visitDots[pos]
				if order <= 9:
					label = order
				elif order > 9:
					label = dic[order-10]
				self.maze[self.dots[i][1]][self.dots[i][2]] = label


		#write the result in testfile_pacman_name.txt
		file = open("testfile_part2_"+name+".txt", "w")
		for j in range(len(self.maze)):
			a = ''.join(self.maze[j])
			file.write(a)
			file.write("\n")
		file.close()

		return


# In[ ]:




# In[ ]:



