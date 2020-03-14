#!/usr/bin/env python
# coding: utf-8

# ## Task-1

# ##### 1.Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[1]:


print('Welcome to Python')


# ##### 2.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both include). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[2]:


s=','
l1=[]
for i in range(2000,3200):
    if ( i % 7 == 0 ) & (i % 5!=0):
        l1.append(str(i))
print(s.join(l1))


# ###### 3.Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
# 

# In[3]:


first_name = input('Enter first Name: ')
last_name  = input('Enter Last Name: ')
res = last_name[::-1]+' '+first_name[::-1]
print(res)


# ##### 4.Write a Python program to find the volume of a sphere with diameter 12 cm.        Formula: V=4/3 * π * r 3

# In[4]:


r =12
pi=3.14
volume=(4//3)*(pi*r**3)
print(volume)


# ## Task 2:

# ##### 1.Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

# In[5]:


numbers =input('Enter sequence of comma separated numbers : ')
list1  = numbers.split(',')
print(list1)


# ##### 2.  Create the below pattern using nested for loop in Python.
# ###### *
# ###### * *
# ###### * * *
# ###### * * * *
# ###### * * * * *
# ###### * * * *
# ###### * * *
# ###### * *
# ###### *

# In[6]:


n=5
for i in range(5):
    for j in range(i):
        print('*',end=' ')
    print()
#second part printing 
for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()


# ##### 3.Write a Python program to reverse a word after accepting the input from the user.
# ##### Sample Output:  Input word: AcadGild   Output: dilGdacA

# In[7]:


word = input('Enter a Word : ')
print(word[::-1])


# ##### 4. Write a Python Program to print the given string in the format specified in the sample output. 
# ###### WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
# 

# In[8]:


print(""" WE, THE PEOPLE OF INDIA, \n \t having solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens""")


# In[ ]:




