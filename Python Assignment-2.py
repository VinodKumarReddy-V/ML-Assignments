#!/usr/bin/env python
# coding: utf-8

# ## Task-1

# ### 1. 1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
# 

# In[1]:


#define function for myreduce()
def myreduce(functionn,listn):
    '''my own function to work like reduce'''
    result = functionn(listn)
    return result

def summation(n):
    ''' Definition for sum of each values'''
    total=0
    for i in n:
        total= total + i
    return total
    
def multiplication(n):
    ''' Deffinition for multiply all the vlaues'''
    mul =1
    for i in n:
        mul = mul * i
    return mul

input = [2,5,6,7,9]
#calling myreduce function to calculate sum of list 
res = myreduce(summation,input)
print('Sum of input values=',res)
#calling myreduce function to do multiply all the nums
res1 = myreduce(multiplication,input)
print('Product of input values= ',res1)


# ### 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
# 

# In[2]:


#Defining myfilter function
def myfilter(funct,n):
    '''My own function work like myfilter'''
    result = funct(n)
    return result


def divisibleby7(list1):
    ''' Applying filter  logic for list divisible by 7'''
    r =[]
    for i in list1:
        if (i%7 ==0):
            r.append(i)
    return r

def even_nums(list1):
    '''Get the even numbers '''
    s = []
    for i in list1:
        if (i%2==0):
            s.append(i)
    return s
        
inplist = [7,8,12,14,45,78,84,91]
res = myfilter(divisibleby7,inplist)
print('Divisible by 7 are ',res)
even = myfilter(even_nums,inplist)
print('Evenn numbers =',even)


# ### 2.  Implement List comprehensions to produce the following lists.
# #### Write List comprehensions to produce the following Lists
# ##### ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ##### ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ##### ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# ##### [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# ##### [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# ##### [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[3]:


string = "ACADGILD"
[i for i in string ]


# In[4]:


list1 = ['X','Y','Z']
[i*j for i in list1 for j in range(1,5)]


# In[5]:


list2 = ['X','Y','Z']
[j*i for i in range(1,5) for j in list2]


# In[6]:


list3 = [2,3,4]
[[i+j] for i in list3 for j in range(0,3)]


# In[7]:


list4 = [2,3,4,5]
[[i+j for i in list3] for j in range(0,5)]


# In[8]:


list5 = [1,2,3]
[ (j,i) for i in range(1,4) for j in list5]


# #### 3. Implement a function longestWord() that takes a list of words and returns the longest one.

# In[9]:


def longestWord(listw):
    '''To get longest words from list'''
    temp = len(listw[0])
    res = listw[0]
    for i in listw:
        if temp < len(i):
            res = i
    return res

n = ['aaa','bb','CCCCCC','vinod','reddy','SV university']
print('Longest Word==>',longestWord(n))
    


# ## Task-2 

# #### 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# ##### area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# ##### Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.
# 

# In[10]:


class supe():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
#sub class 
class areaSub(supe):
    def calc(self):
        ''' Calculating Area..'''
        s = (self.a + self.b + self.c)/2
        area = (s*(s - self.a)*(s -self.b)* (s -self.c))* 0.5
        #print('Area=',area)
        return area

ar = areaSub(3,4,5)
print('Area of triangle=',ar.calc())


# #### 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
# 

# In[2]:


def filter_long_words(list1,n):
    res =[]
    for i in list1:
        if (len(i)>= int(n)):
            res.append(i)
    return res

listnk = ['aaa','nani','reddy','Banglore','TCS','NishuuuNair']
num=input('Enter a number')
print(filter_long_words(listnk,num))




# #### 2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words .
# ##### Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.
# 

# In[16]:


def find_length(list1):
    '''finding length of each word in a list'''
    res1=[]
    for i in list1:
        res1.append(len(i))
    return res1

inp=['ab','cde','erty','vinod','kumar','inueron']
print('Length of each value is =',find_length(inp))


# #### 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
# 

# In[1]:


def find_vowel_or_not(char1):
    '''Finding given is Vowel or not'''
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    res = ' '
    if char1 in vowel:
        return True
    else:
        return False

char = input('Enter a Character b/w (A-Z)=')
print(find_vowel_or_not(char))
        
    

