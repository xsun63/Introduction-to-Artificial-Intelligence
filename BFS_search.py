
# coding: utf-8

# In[96]:

import sys
sys.setrecursionlimit(100000)
from urllib.request import urlopen
import numpy as np
import queue 
class Node:     #states
    def _init_(self):
        self.r= 0     #row
        self.c= 0     #column
        self.parent=None      #parent in tree
class search_maze:       
    def __init__(self,name):
        #first initilize maze
        URL= "http://slazebni.cs.illinois.edu/fall17/assignment1/"+name+".txt"
        response = urlopen(URL)
        lines = response.readlines()
        bitlist= [i.rstrip() for i in lines]
        strlist=[k.decode('ascii') for k in bitlist]
        charlist=[list(j) for j in strlist]
        self.maze=np.asarray(charlist)
        #initialize position of start point and end point
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j]=='P':
                    p=Node()
                    p.r=i
                    p.c=j
                    p.label =0
                    p.parent=None;
                if self.maze[i][j]=='.':
                    g=Node()
                    g.r=i
                    g.c=j
                    g.label=0
                    g.parent=None;
        #build visitmap same size of maze to mark a position as visited
        self.visitmap=[[0 for x in range(len(self.maze[0]))] for y in range(len(self.maze))]        
        self.path_cost = 0
        self.node_number = 0
        self.current=p
        self.dest=g
        self.visitmap[self.current.r][self.current.c]=1
        self.frontier = queue.Queue()    #queue of node 
        self.frontier.put(self.current)
    #i= row(r)  j = col(c)   (row,col)
                   
    def BFS(self):
        if self.frontier.empty():
            return 
        self.current=self.frontier.get() #pop items off queue
        self.node_number+=1
        if(self.current.r==self.dest.r) & (self.current.c==self.dest.c):
            #if reaches destination,find the path from leaf node to root and return it
            path=[]
            while(self.current.parent !=None):
                pos=[self.current.r,self.current.c]
                self.current=self.current.parent
                path.append(pos)       
            return path
            #path stores all  the [r,c]position in the path 
        if (self.maze[self.current.r][self.current.c-1]!='%') & (self.visitmap[self.current.r][self.current.c-1]==0): #check if able to go left
            #if able to go left, set up child, push it into frontier,mark this postion as visited
            childleft=Node()
            childleft.r=self.current.r
            childleft.c=self.current.c-1
            childleft.parent=self.current
            self.visitmap[self.current.r][self.current.c-1]=1
            self.frontier.put(childleft)
        if (self.maze[self.current.r][self.current.c+1]!='%') & (self.visitmap[self.current.r][self.current.c+1]==0):    #go right
            childright=Node()
            childright.r=self.current.r
            childright.c=self.current.c+1
            childright.parent=self.current
            self.visitmap[self.current.r][self.current.c+1]=1
            self.frontier.put(childright)
        if (self.maze[self.current.r+1][self.current.c]!='%') & (self.visitmap[self.current.r+1][self.current.c]==0):   #go down
            childdown=Node()
            childdown.r=self.current.r+1
            childdown.c=self.current.c
            childdown.parent=self.current
            self.frontier.put(childdown)
            self.visitmap[self.current.r+1][self.current.c]=1
        if (self.maze[self.current.r-1][self.current.c]!='%') & (self.visitmap[self.current.r-1][self.current.c]==0==0):    #go up
            childup=Node()
            childup.r=self.current.r-1
            childup.c=self.current.c
            childup.parent=self.current
            self.frontier.put(childup)
            self.visitmap[self.current.r-1][self.current.c]=1
        return self.BFS()
         
    def printmaze(self):
        path=self.BFS()
        #draw path
        for element in path:
            self.maze[element[0]][element[1]]='.'
            self.path_cost+=1
        #write to file
        file = open("testfile_BFS.txt","w")
        for j in range(len(self.maze)):
            a=''.join(self.maze[j])
            file.write(a)
            file.write("\n")
        file.close()
        
        
maze1 = search_maze("mediumMaze")
maze1.printmaze()
print(maze1.node_number)
print(maze1.path_cost)


# In[ ]:




# In[ ]:




# In[ ]:



