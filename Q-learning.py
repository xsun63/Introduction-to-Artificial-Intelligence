
# coding: utf-8

# In[ ]:

import numpy as np
import random
import math

q=np.zeros((10369,3))     #our q value look up table
action_table=np.zeros((10369,3))     #how many times we have done current action at current state
counter=0 
p_height=0.2
grid_size=1/12
bounce_num=0
bounce_max=0
bounce_eight=0
action_max=[0,0,0]
a=0.4 #alpha
c=1000
y=0.9  #gamma
class state:
    def __init__(self):
        #continuous value
        self.x=0.5
        self.y=0.5
        self.vx=0.03
        self.vy=0.01
        self.paddle_y=0.5-p_height/2
        #discrete value
        self.x_grid=0
        self.y_grid=0
        self.grid_position=0
        self.x_velocity=0
        self.y_velocity=0
        self.paddle=0
        self.qx=0
        self.action=0
        self.prev_qx=0
current=state()

for j in range(0,10):
    counter=0 
    bounce_num=0
    bounce_max=0
    bounce_eight=0
    action_max=[0,0,0]
    while (counter<10000):
        current.reward=0
        if (current.x>=1):
            #if hit paddle
            if (current.y<=current.paddle_y+0.2)&(current.y>=current.paddle_y):
                #update state
                current.x=2-current.x
                current.vx=-current.vx+random.uniform(-0.015,0.015)
                current.paddly_y=current.paddle_y+random.uniform(-0.03,0.03)
                #update utility of previous state
                q[current.prev_qx][current.action]+=a
                if (current.vx<0.03)&(current.vx>0):
                    vx=0.03
                if (current.vx>-0.03)&(current.vx<0):
                    vx=-0.03
                bounce_num+=1
                bounce_max+=1
                if (bounce_max==9):
                    bounce_eight+=1
            #if run out of range
            else:
                #update utility and start again   
                q[current.prev_qx][current.action]-=a
                bounce_max=0
                counter+=1
                current.x=0.5
                current.y=0.5
                current.vx=0.03
                current.vy=0.01
                current.paddle_y=0.5-p_height/2
                current.x_grid=0
                current.y_grid=0
                current.grid_position=0
                current.x_velocity=0
                current.y_velocity=0
                current.paddle=0
                current.qx=0
                current.action=0
                current.prev_qx=10368
                continue

        #update q(s,a)
        #update state of current position
        current.x_grid=math.floor(current.x/grid_size)
        current.y_grid=math.floor(current.y/grid_size)
        current.grid_position=current.y_grid*12+current.x_grid

        if (current.vx>0):
            current.x_velocity=1
        else:
            current.x_velocity=0

        if (current.vy>0.015):
            current.y_velocity=2
        if (current.vy<-0.015):
            current.y_velocity=1
        else:
            current.y_velocity=0

        current.paddle=math.floor(12*current.paddle_y/(1-p_height))

        if (current.paddle_y>=1-p_height):
            current.paddle=11
        current.qx=72*current.grid_position+36*current.x_velocity+12*current.y_velocity+current.paddle   
        q[current.prev_qx][current.action]+=a*(y*np.amax(q[current.qx])-q[current.prev_qx][current.action]) 
        #decide next action
        for i in range(0,3):
            if action_table[current.qx][i]>10:
                action_max[i]=q[current.qx][i]/action_table[current.qx][i]
            else:
                action_max[i]=10000
        current.action=action_max.index(max(action_max))
        action_table[current.qx][current.action]+=1
        a=c/(action_table[current.qx][current.action]+c)

        current.prev_qx=current.qx
        #update x,y at the end     action0-move up 1-don't move 2-move down
        current.x+=current.vx                          
        current.y+=current.vy
        current.paddle_y=current.paddle_y-0.04+0.04*current.action
        #check lower bound for x
        if (current.x<=0):
            current.x=-current.x
            current.vx=-current.vx
        #check lower bound for y
        if (current.y<=0):
            current.y=-current.y
            current.vy=-current.vy
        #check upper bound for y
        if (current.y>=1):
            current.y=2-current.y
            current.vy=-current.vy
        #check bound for paddle
        if (current.paddle_y<0):
            current.paddle_y=0
        if (current.paddle_y>1-p_height):
            current.paddle_y=1-p_height

    print(bounce_num/counter)        
    print(bounce_eight)
            


        
        
    




# In[ ]:




# In[ ]:



