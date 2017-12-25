
# coding: utf-8

# In[50]:

import os
import math
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')

#set up 4-d array fij with 10 2-d arrays, keeping track of number of counts of fij in any particular classes
fij=[]
prob=[]
for i in range(0,10):
    fij.append([])
    prob.append([])
    for j in range(0,256):
        fij[i].append([])
        prob[i].append([])
        for k in range(0,7):
            fij[i][j].append([])
            prob[i][j].append([])
            for m in range(0,14):
                fij[i][j][k].append(0)
                prob[i][j][k].append(0)
class_num=[0,0,0,0,0,0,0,0,0,0]            
class_prob=[0,0,0,0,0,0,0,0,0,0] 

#set up a 28*28 array to first read the entire character out
character=[]
for i in range (0,28):
    character.append([])
    for j in range(0,28):
        character[i].append(0)

#trainging process
current_class=1
current_block=(0,0,0,0,0,0,0,0)
index=0
current_char=''
for training_num in range(0,5000):
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char==' ':
                character[i][j]=0
            else:
                character[i][j]=1
    for i in range(0,7):
        for j in range(0,14):
            #current_block=(character[2*i][4*j],character[2*i][4*j+1],character[2*i][4*j+2],character[2*i][4*j+3],character[2*i+1][4*j],character[2*i+1][4*j+1],character[2*i+1][4*j+2],character[2*i+1][4*j+3])
            current_block=(character[4*i][2*j],character[4*i+1][2*j],character[4*i+2][2*j],character[4*i+3][2*j],character[4*i][2*j+1],character[4*i+1][2*j+1],character[4*i+2][2*j+1],character[4*i+3][2*j+1])
            #current_block=(character[4*i][4*j],character[4*i+1][4*j],character[4*i+2][4*j],character[4*i+3][4*j],character[4*i][4*j+1],character[4*i+1][4*j+1],character[4*i+2][4*j+1],character[4*i+3][4*j+1],character[4*i][4*j+2],character[4*i+1][4*j+2],character[4*i+2][4*j+2],character[4*i+3][4*j+2],character[4*i][4*j+3],character[4*i+1][4*j+3],character[4*i+2][4*j+3],character[4*i+3][4*j+3])
            #index=(current_block[0]<<15)|(current_block[1]<<14)|(current_block[2]<<13)|(current_block[3]<<12)|(current_block[4]<<11)|(current_block[5]<<10)|(current_block[6]<<9)|(current_block[7]>>8)|(current_block[8]<<7)|(current_block[9]<<6)|(current_block[10]<<5)|(current_block[11]<<4)|(current_block[12]<<3)|(current_block[13]<<2)|(current_block[14]<<1)|(current_block[15])
            index=(current_block[0]<<7)|(current_block[1]<<6)|(current_block[2]<<5)|(current_block[3]<<4)|(current_block[4]<<3)|(current_block[5]<<2)|(current_block[6]<<1)|(current_block[7])
            fij[current_class][index][i][j]+=1

#print(fij)




# In[51]:

k=0.1
for i in range(0,10):
    class_prob[i]=class_num[i]/5000
    for j in range(0,256):
        for l in range(0,7):
            for m in range(0,14):
                prob[i][j][l][m]=(fij[i][j][l][m]+k)/(class_num[i]+2*k)


# In[52]:

#testing process

#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

#set up data structure to hold correct rates
current_max=0                             #the class that has highest prob
wrong=0
current_prob=[0,0,0,0,0,0,0,0,0,0]      #probalility of current character for each class
test_case=[0,0,0,0,0,0,0,0,0,0]         #number of test cases for each class
test_wrong=[0,0,0,0,0,0,0,0,0,0]        #number of wrong test cases for each class
correct_rate=[0,0,0,0,0,0,0,0,0,0]      #percentage of all give classes correctly classified
confusion_matrix=[]                     #confusion matrix is a 10*10 array
for i in range(0,10):
    confusion_matrix.append([])
    for j in range(0,10):
        confusion_matrix[i].append(0)
print(class_prob)
file = open("wrong_cases.txt","w")

#go through every test image and record data by the way
for test_num in range(0,1000):
    for i in range(0,10):
        current_prob[i]=math.log(class_prob[i])
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    test_case[current_class]+=1
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char==' ':
                character[i][j]=0
            else:
                character[i][j]=1
    for i in range(0,7):
        for j in range(0,14):
            current_block=(character[4*i][2*j],character[4*i+1][2*j],character[4*i+2][2*j],character[4*i+3][2*j],character[4*i][2*j+1],character[4*i+1][2*j+1],character[4*i+2][2*j+1],character[4*i+3][2*j+1])
            #current_block=(character[2*i][4*j],character[2*i][4*j+1],character[2*i][4*j+2],character[2*i][4*j+3],character[2*i+1][4*j],character[2*i+1][4*j+1],character[2*i+1][4*j+2],character[2*i+1][4*j+3])
            #current_block=(character[4*i][4*j],character[4*i+1][4*j],character[4*i+2][4*j],character[4*i+3][4*j],character[4*i][4*j+1],character[4*i+1][4*j+1],character[4*i+2][4*j+1],character[4*i+3][4*j+1],character[4*i][4*j+2],character[4*i+1][4*j+2],character[4*i+2][4*j+2],character[4*i+3][4*j+2],character[4*i][4*j+3],character[4*i+1][4*j+3],character[4*i+2][4*j+3],character[4*i+3][4*j+3])
            #index=(current_block[0]<<15)|(current_block[1]<<14)|(current_block[2]<<13)|(current_block[3]<<12)|(current_block[4]<<11)|(current_block[5]<<10)|(current_block[6]<<9)|(current_block[7]>>8)|(current_block[8]<<7)|(current_block[9]<<6)|(current_block[10]<<5)|(current_block[11]<<4)|(current_block[12]<<3)|(current_block[13]<<2)|(current_block[14]<<1)|(current_block[15])
            index=(current_block[0]<<7)|(current_block[1]<<6)|(current_block[2]<<5)|(current_block[3]<<4)|(current_block[4]<<3)|(current_block[5]<<2)|(current_block[6]<<1)|(current_block[7])          
            for l in range(0,10):
                current_prob[l]+=math.log(prob[l][int(index)][i][j])
#             fij[current_class][index][i][j]+=1                
#             for l in range(0,10):
#                 current_prob[l]+=math.log(prob[current_char][l][i][j])
    current_max=current_prob.index(max(current_prob))
    if current_max!=current_class:
        file.write("true class:")
        file.write(str(current_class))
        file.write("      identified as:")
        file.write(str(current_max))
        file.write("\n")
        test_wrong[current_class]+=1
        confusion_matrix[current_class][current_max]+=1
        wrong+=1
       

    
#print our results  
for i in range(0,10):
    correct_rate[i]=(test_case[i]-test_wrong[i])/test_case[i]
    for j in range(0,10):
        confusion_matrix[i][j]=confusion_matrix[i][j]/test_case[i]
"{0:.2f}".format(13.949999999999999)
print(wrong)
print(test_case)
print(correct_rate)
print(confusion_matrix)


# In[53]:

for i in range(0,10):
    for j in range(0,10):
        confusion_matrix[i][j]=float("{0:.3f}".format(confusion_matrix[i][j]))
file_test = open("confusion_matrix.txt","w")
for i in range(0,10):
    a=''.join(str(confusion_matrix[i]))
    file_test.write(a)
    file_test.write("\n")
file_test.close()


# In[ ]:



