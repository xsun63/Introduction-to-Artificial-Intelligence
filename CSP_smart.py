
# coding: utf-8

# In[66]:

import sys
sys.setrecursionlimit(5000)
from urllib.request import urlopen
from datetime import datetime
import numpy 
import random
class flow_free:       
    def __init__(self,size):
        #first initilize mazeA
        URL= "http://slazebni.cs.illinois.edu/fall17/assignment2/input"+size+".txt"
        response = urlopen(URL)
        lines = response.readlines()
        bitlist= [i.rstrip() for i in lines]
        strlist=[k.decode('ascii') for k in bitlist]
        charlist=[list(j) for j in strlist]
        temp=numpy.asarray(charlist)
        self.value=[]                              #colors availble for each spot
        self.points=[]                            #position of origial points in diagram
        #turn numpy array into a list with edge '_' and size (a+2)*(a+2)
        edge=[]
        for i in range(len(temp)+2):
            edge.append('_')
        self.plane=[]
        self.plane.append(edge)
        for i in range (len(temp)):
            self.plane.append([])
            self.plane[i+1].append('_')
            for j in range(len(temp[0])):
                 self.plane[i+1].append(temp[i][j])
            self.plane[i+1].append('_')
        self.plane.append(edge)                                  
        self.color={}                    #dictionary keep track of colors and corresponding path
        self.complete={}                  #keep track if each number is complete  
        self.recursion=0
        self.unexplored=[]
        self.space={}                    #keep track of legal values for all variables
        for i in range(1,len(self.plane)-1):
            for j in range(1,len(self.plane[0])-1):
                if (self.plane[i][j] != '_'):
                    self.points.append((i,j))
                    if (self.value.count(self.plane[i][j])==0):
                        self.value.append(self.plane[i][j])
                        self.color[self.plane[i][j]]=[(i,j)]
                        self.complete[self.plane[i][j]]=0
                        self.space[self.plane[i][j]]=[]
                    else:
                        self.color[self.plane[i][j]].append((i,j))
                else:
                    self.unexplored.append((i,j))
    def goal(self):
        """decide if we reach goal state"""
        for i in range(1,len(self.plane)-1):
            for j in range(1,len(self.plane[0])-1):       #exclude edge cases
                if (self.plane[i][j]=='_'):
                    return 0
                if (self.points.count((i,j))==0):       #not in value set, need two colors
                    number=0 
                    if (self.plane[i][j]==self.plane[i-1][j]):
                        number+=1
                    if self.plane[i][j]==self.plane[i+1][j]:
                        number+=1
                    if (self.plane[i][j]==self.plane[i][j-1]):
                        number+=1
                    if self.plane[i][j]==self.plane[i][j+1]:
                        number+=1
                    if (number!=2):
                        return 0
                else:
                    if ((self.plane[i+1][j]!=self.plane[i][j]) & (self.plane[i-1][j]!=self.plane[i][j]) & 
                        (self.plane[i][j+1]!=self.plane[i][j]) & (self.plane[i][j-1]!=self.plane[i][j])):
                        #if a color has no neighbor, return failure
                        return 0      
        return 1   
    def neighbor_color(self,position,color):
        """return number of neighbors with given color on given position"""
        number=0
        if (self.plane[position[0]+1][position[1]]==color):
            number+=1
        if (self.plane[position[0]-1][position[1]]==color):
            number+=1
        if (self.plane[position[0]][position[1]+1]==color):
            number+=1
        if (self.plane[position[0]][position[1]-1]==color):
            number+=1
        return number
    def find_current(self):
        """find next variable to assign value to-return a color that we should expand next.return 0 if plane is full(check first)"""
        if (len(self.unexplored)==0):
            return 0
        min_position=10
        color=self.value[0]
        for i in self.value:
            if (self.complete[i]==0):
                self.space[i]=self.effective_position(i)        #update legal values every time
                element=self.color[i][-1]
                if self.neighbor_color(element,i)==2:    #if there are two nodes of same color around last element,list is complete
                    self.complete[i]=1
                    continue
                length=len(self.effective_position(i))
                if (length==0):
                    return 0
                if length<min_position:
                    min_position=length
                    color=i   
        return color
    
    def edge(self,position):
        """decide if given position is on the edge"""
        if ((position[0]==0) | (position[0]==len(self.plane)-1) |(position[1]==0)|(position[1]==len(self.plane[0])-1)):
            return 1
        return 0
    
    def effective_position(self,color):
        """find effective postions for the last element in color list
           input:color to work with
           output:a list containg expandable postions for given color"""
        position=self.color[color][-1]         #postion of last element
        return_list=[]
        #check if '_' and if edge case-did not check for zigzags 
        if (self.plane[position[0]+1][position[1]]=='_')& (self.edge((position[0]+1,position[1]))==0):
            distance=abs(position[0]+1-self.color[color][0][0])+abs(position[1]-self.color[color][0][1])
            return_list.append((distance,(position[0]+1,position[1])))
        if (self.plane[position[0]-1][position[1]]=='_')& (self.edge((position[0]-1,position[1]))==0):
            distance=abs(position[0]-1-self.color[color][0][0])+abs(position[1]-self.color[color][0][1])
            return_list.append((distance,(position[0]-1,position[1])))
        if (self.plane[position[0]][position[1]+1]=='_')& (self.edge((position[0],position[1]+1))==0):
            distance=abs(position[0]-self.color[color][0][0])+abs(position[1]+1-self.color[color][0][1])
            return_list.append((distance,(position[0],position[1]+1)))
        if (self.plane[position[0]][position[1]-1]=='_')& (self.edge((position[0],position[1]-1))==0):
            distance=abs(position[0]-self.color[color][0][0])+abs(position[1]-1-self.color[color][0][1])
            return_list.append((distance,(position[0],position[1]-1)))
        return_list.sort()
        return return_list
    
    def dumb(self):
        """dumb algorithm with random value and variable ordering"""
        if self.goal()==1:
            return 1           #if get to goal,return success
        current=self.find_current();
        if (current==0):                 #now current is a color
            return 0
        self.recursion+=1
        if (self.recursion==100000000):
            return 1
        effective=self.effective_position(current)
        for j in effective:
            i=j[1]
            self.color[current].append(i)        #add postion to list
            self.plane[i[0]][i[1]]=current
            self.unexplored.remove(i)
            if (self.dumb()==1):
                return 1
            del self.color[current][-1]          #remove position from list
            self.plane[i[0]][i[1]]='_'
            self.complete[current]=0
            self.unexplored.append(i)
        return 0        #return failure
    
    
    
start=datetime.now()    
test=flow_free("991")
print(test.dumb())
file = open("testfile_99.txt","w")
for j in range(1,len(test.plane)-1):
    del test.plane[j][0]
    test.plane[j].pop()
    a=''.join(test.plane[j])
    file.write(a)
    file.write("\n")
file.close()
print(datetime.now()-start)
print(test.recursion)
print(test.plane)


# In[ ]:



