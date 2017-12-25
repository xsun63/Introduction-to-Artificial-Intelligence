
# coding: utf-8

# In[20]:

import sys
sys.setrecursionlimit(100000)
from urllib.request import urlopen
import numpy as np
import queue 

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
        #initialize position of current point and end point
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j]=='P':
                    self.current=(10000,i,j,None,0)
                if self.maze[i][j]=='.':
                    self.dest=(0,i,j,None,0)    #heuristic+path cost,row,column,parent,path cost
        self.visitmap=[[0 for x in range(len(self.maze[0]))] for y in range(len(self.maze))]
        self.path_cost = 0
        self.node_number = 0
        self.frontier = queue.PriorityQueue()    #queue of node 
        self.frontier.put(self.current)
        self.visitmap[self.current[1]][self.current[2]]=1
    #i= row(r)  j = col(c)   (row,col)
                   
    def Astar(self):
        if self.frontier.empty():
            return 
        self.current=self.frontier.get() #pop items off queue
        self.node_number+=1       
        if(self.current[1]==self.dest[1]) & (self.current[2]==self.dest[2]):
            #if get to end point, find the path from leaf to root
            path=[]
            while(self.current[3] !=None):
                pos=[self.current[1],self.current[2]]
                self.current=self.current[3]
                path.append(pos)       
            return path
            #path stores all  the [r,c]position in the path 
        if (self.maze[self.current[1]][self.current[2]-1]!='%') & (self.visitmap[self.current[1]][self.current[2]-1]==0): #check if able to go left 
            #first calucluate heuristic+path cost, push new position into frontier,mark as visited
            h=abs(self.dest[1]-self.current[1])+abs(self.dest[2]-(self.current[2]-1))+self.current[4]
            childleft=(h,self.current[1],self.current[2]-1,self.current,self.current[4]+1)
            self.frontier.put(childleft)
            self.visitmap[self.current[1]][self.current[2]-1]=1
        if (self.maze[self.current[1]][self.current[2]+1]!='%') & (self.visitmap[self.current[1]][self.current[2]+1]==0):    #go right
            h=abs(self.dest[1]-self.current[1])+abs(self.dest[2]-(self.current[2]+1))+self.current[4]
            childright=(h,self.current[1],self.current[2]+1,self.current,self.current[4]+1)
            self.frontier.put(childright)
            self.visitmap[self.current[1]][self.current[2]+1]=1
        if (self.maze[self.current[1]+1][self.current[2]]!='%') & (self.visitmap[self.current[1]+1][self.current[2]]==0):   #go down
            h=abs(self.dest[1]-(self.current[1]+1))+abs(self.dest[2]-self.current[2])+self.current[4]
            childdown=(h,self.current[1]+1,self.current[2],self.current,self.current[4]+1)
            self.frontier.put(childdown)
            self.visitmap[self.current[1]+1][self.current[2]]=1
        if (self.maze[self.current[1]-1][self.current[2]]!='%') & (self.visitmap[self.current[1]-1][self.current[2]]==0==0):    #go up
            h=abs(self.dest[1]-(self.current[1]-1))+abs(self.dest[2]-self.current[2])+self.current[4]
            childup=(h,self.current[1]-1,self.current[2],self.current,self.current[4]+1)
            self.frontier.put(childup)
            self.visitmap[self.current[1]-1][self.current[2]]=1
        return self.Astar()
         
    def printmaze(self):
        path=self.Astar()
        for element in path:
            self.maze[element[0]][element[1]]='.'
            self.path_cost+=1
        file = open("testfile_astar.txt","w")
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



