
# coding: utf-8

# In[193]:

import os
import math
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')

#set up 3-d array fij with 10 2-d arrays, keeping track of number of counts of fij in any particular classes
fij=[]
prob=[]
prob.append([])                    #prob[0] is probabilty that fij is zero for a particular class
prob.append([])
for i in range(0,10):
    fij.append([])
    prob[0].append([])
    prob[1].append([])
    for j in range(0,28):
        fij[i].append([])
        prob[0][i].append([])
        prob[1][i].append([])
        for k in range(0,28):
            fij[i][j].append(0)
            prob[0][i][j].append(0)
            prob[1][i][j].append(0)
class_num=[0,0,0,0,0,0,0,0,0,0]            
class_prob=[0,0,0,0,0,0,0,0,0,0] 


#trainging process

current_class=1
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
            if current_char!=' ':
                fij[current_class][i][j]+=1

k=10
for i in range(0,10):
    class_prob[i]=class_num[i]/5000
    for j in range(0,28):
        for l in range(0,28):
            prob[1][i][j][l]=(fij[i][j][l]+k)/(class_num[i]+2*k)
            prob[0][i][j][l]=(class_num[i]-fij[i][j][l]+k)/(class_num[i]+2*k)
print(class_num)
file_test = open("fij.txt","w")
for i in range(0,10):
    file_test.write("\n")
    for j in range(0,28):
        a=''.join(str(fij[i][j]))
        file_test.write(a)
        file_test.write("\n")
file_test.close()

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
            if current_char!=' ':
                current_char=1
            else:
                current_char=0
            for l in range(0,10):
                current_prob[l]+=math.log(prob[current_char][l][i][j])
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


# In[186]:

for i in range(0,10):
    for j in range(0,10):
        confusion_matrix[i][j]=float("{0:.5f}".format(confusion_matrix[i][j]))


# In[187]:

print(confusion_matrix)


# In[188]:

file_test = open("confusion_matrix.txt","w")
for i in range(0,10):
    a=''.join(str(confusion_matrix[i]))
    file_test.write(a)
    file_test.write("\n")
file_test.close()


# In[14]:




# In[ ]:



