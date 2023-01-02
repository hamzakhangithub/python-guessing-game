#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[9]:


def guess(x):
    random_number = random.randint(1,x)
    guess_number=0
    chance=7
    name = input("Enter Your Name: ")
    print(f"Welcome to the Guessing Game {name} ")
    print(f'The number is in between 1 and {x}')
    
    while guess_number!=random_number:
        guess_number = int(input("Guess the Number: "))
        diff = abs(random_number - guess_number)
        if random_number == guess_number:
            print(f"Congrats {name} !! You have guessed it correctly.")
            break
        else:
            if diff<2 and diff>=1:
                print("Way too close!!!")
            elif diff<5:
                print("Very Close!!!")
            elif diff<12 and diff>=5:
                print("Okay You are getting near it.")
        chance-=1
        print(f"You now have {chance} chances.")
        if chance==0:
            print("You are out of chance.")
            print("Game Over!!!")
            break
            
guess(50)


# In[12]:


import os
os.chdir('C:\Git Repositries\Python Guessing Game')


# In[ ]:




