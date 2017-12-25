
# coding: utf-8

# In[6]:

import os
import math
import random
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')

#set up 2d array 10*28*28
w=[]                       #data structure for weight w for 10 characters and 784 features
for i in range(0,10):
    w.append([])
    for j in range(0,28):
        w[i].append([])            #try zero weight first
        for k in range(0,28):
            w[i][j].append(0)            #try zero weight first        
class_num=[0,0,0,0,0,0,0,0,0,0]            
class_prob=[0,0,0,0,0,0,0,0,0,0] 
our_classification=[0,0,0,0,0,0,0,0,0,0]              #the weighted c from our current perceptron
classified_character=0                             #max of our_classification
a=1               #a is just alpha
c=0.1
t=1
a=c/(t+c)
b=[0,0,0,0,0,0,0,0,0,0]               #offeset
#set up a 28*28 array to first read the entire character out
character=[]
for i in range (0,28):
    character.append([])
    for j in range(0,28):
        character[i].append(0)

#training process

current_class=1
current_char=''
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train1:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print((1000-wrong)/1000)

f_image.close()
f_label.close()
                
t+=2
a=c/(t+c)      
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train2:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print((1000-wrong)/1000)

f_image.close()
f_label.close()
                
t+=2
a=c/(t+c)      
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train3:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print((1000-wrong)/1000)

f_image.close()
f_label.close()
                
t+=2
a=c/(t+c)      
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train4:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print((1000-wrong)/1000)
f_image.close()
f_label.close()
                
t+=2
a=c/(t+c)      
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train5:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print((1000-wrong)/1000)

f_image.close()
f_label.close()
                
t+=2
a=c/(t+c)      
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train6:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print((1000-wrong)/1000)


f_image.close()
f_label.close()
                
t+=2
a=c/(t+c)      
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train13:")
print((5000-wrong_train)/5000)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')
class_num=[0,0,0,0,0,0,0,0,0,0]  
wrong=0
current_class=1
current_char=''
confusion_matrix=[]                     #confusion matrix is a 10*10 array
for i in range(0,10):
    confusion_matrix.append([])
    for j in range(0,10):
        confusion_matrix[i].append(0)
for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        confusion_matrix[current_class][classified_character]+=1
        
for i in range(0,10):
    for j in range(0,10):
        confusion_matrix[i][j]=confusion_matrix[i][j]/class_num[i]        
print((1000-wrong)/1000)

file_test = open("confusion_matrix.txt","w")
for i in range(0,10):
    a=''.join(str(confusion_matrix[i]))
    file_test.write(a)
    file_test.write("\n")
file_test.close()


# In[ ]:




# In[136]:

import math
import random
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')

#set up 2d array 10*28*28
w=[]                       #data structure for weight w for 10 characters and 784 features
random_element=[]
for i in range(0,5000):
    random_element.append(i)
for i in range(0,10):
    w.append([])
    for j in range(0,28):
        w[i].append([])            #try zero weight first
        for k in range(0,28):
            w[i][j].append(0)            #try zero weight first        
class_num=[0,0,0,0,0,0,0,0,0,0]            
class_prob=[0,0,0,0,0,0,0,0,0,0] 
our_classification=[0,0,0,0,0,0,0,0,0,0]              #the weighted c from our current perceptron
classified_character=0                             #max of our_classification
a=1               #a is just alpha
c=0.1
t=1
a=c/(t+c)
b=[0,0,0,0,0,0,0,0,0,0]               #offeset
#set up a 28*28 array to first read the entire character out
character=[]
for i in range (0,28):
    character.append([])
    for j in range(0,28):
        character[i].append(0)

#training process

current_class=1
current_char=''
wrong_train=0
random_number=0
#print(random_element)
for training_num in range(0,5000):
    random_number=random.choice(random_element)
    f_label.seek(random_number)
    f_image.seek(812*random_number)
    random_element.remove(random_number)
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #print(current_class)
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
#     if (random_number==4960):
#         file_test = open("test_random.txt","w")
#         for i in range(0,28):
#             a=''.join(str(character[i]))
#             file_test.write(a)
#             file_test.write("\n")
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()          
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
        
print(random_element)
print("wrong_train1:")
print(wrong_train)

#testing phase
#open files
test_image="\\testimages"
t_image=open(os.getcwd()+file_image,'r+')
test_label="\\testlabels"
t_label=open(os.getcwd()+file_label,'r+')

wrong=0
current_class=1
current_char=''

for testing_num in range(0,1000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=t_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=t_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=t_image.read(1)
            if current_char=='\n':
                current_char=t_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong+=1
        
        
print(wrong)


# In[117]:

import os
import math
import random
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')

#set up 2d array 10*28*28
w=[]                       #data structure for weight w for 10 characters and 784 features
for i in range(0,10):
    w.append([])
    for j in range(0,28):
        w[i].append([])            #try zero weight first
        for k in range(0,28):
            w[i][j].append(0)            #try zero weight first        
class_num=[0,0,0,0,0,0,0,0,0,0]            
class_prob=[0,0,0,0,0,0,0,0,0,0] 
our_classification=[0,0,0,0,0,0,0,0,0,0]              #the weighted c from our current perceptron
classified_character=0                             #max of our_classification
a=1               #a is just alpha
c=0.1
t=1
a=c/(t+c)
b=[0,0,0,0,0,0,0,0,0,0]               #offeset
#set up a 28*28 array to first read the entire character out
character=[]
for i in range (0,28):
    character.append([])
    for j in range(0,28):
        character[i].append(0)

#training process

current_class=1
current_char=''
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        for i in range(0,28):
            for j in range(0,28):
                w[current_class][i][j]+=a*character[i][j]
                w[classified_character][i][j]-=a*character[i][j]

                
f_image.close()
f_label.close()
              
#open training images and training labels
file_image="\\trainingimages"
f_image=open(os.getcwd()+file_image,'r+')
file_label="\\traininglabels"
f_label=open(os.getcwd()+file_label,'r+')
wrong_train=0
for training_num in range(0,5000):
    our_classification=[0,0,0,0,0,0,0,0,0,0] 
    current_class=f_label.read(1)
    if current_class.isdigit():
        current_class=int(current_class)
    else:
        current_class=f_label.read(1)
        current_class=int(current_class)
    class_num[current_class]+=1
    #first read 784 pixels of a character into character
    for i in range(0,28):
        for j in range(0,28):
            current_char=f_image.read(1)
            if current_char=='\n':
                current_char=f_image.read(1)
            if current_char!=' ':
                character[i][j]=1
            if current_char==' ':
                character[i][j]=0 
    #find which class does we classify this character as and compare
    for i in range(0,10):
        our_classification[i]+=b[i]
        for j in range (0,28):
            for k in range(0,28):
                our_classification[i]+=w[i][j][k]*character[j][k]
    classified_character=our_classification.index(max(our_classification))
    #update w if the result is not correct
    if (classified_character!=current_class):
        wrong_train+=1
print("wrong_train1:")
print(wrong_train)
print(w)


# In[89]:




# In[58]:




# In[ ]:



