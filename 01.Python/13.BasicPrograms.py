# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 12:58:09 2017

@author: rmatam
"""
#While Loop
a,b=0,1
while b<10:
    print b
    a,b=b,a+b
a
b

#while loop2   
c,d=0,1
while c<1000:
    print c
    c,d=d,c+d
    
    
#If Conditonal program
x=int(raw_input("Please Enter Input:"))
if x<0:
    x=0
    print 'Negative Chnaged to Zero'
elif x==0:
    print 'Zero'
elif x==1:
    print'Single'
else:
    print 'More'

#Measure of some words
Words=['cat','dog','elephant','rat','mouse']
for w in Words:
    print w,len(w)
    for w in Words[:]:
        if len(w)>6:
            Words.insert(0,w)
            Words
    
    
#Range funtion
range(10)
range(100)
range(5,1)
range(5,10)
range(5,20)
range(0,10,3)
range(0,100,4)
range(-10,-100,-3)

a=['Mary','had','a','little','lamb']
for i in range(len(a)):
    print i, a[i]


#Define Functions
def fib(n): # write Fibonaci series up to n
    a,b=0,1
    while a<n:
        print a
        a,b=b,a+b

#now call the function
fib(2000)

#Define Functions
def square(n): # write square of number up to n
    a=0
    while a<n:
        print a**2
        a=a+1
#now call the function
square(10)

#Define Functions
def cube(n): # write Cube of number up to n
    a=0
    while a<n:
        print a**3
        a=a+1
#now call the function
cube(10)


#Define Functions
def SquareRoot(n): # write squareroot of number up to n
    a=0
    while a<n:
        print a** 0.5
        a=a+1
#now call the function
SquareRoot(10)

#Documentation String
def MyFunction():
    """ Do Nothing .But document it.
    
    No Really it does not do it.
    """
    pass
#call the function now
MyFunction.__doc__

#list operations
#list.append(x)
a=[66.25,333,333,1,1234.5]
print a.count(x)
print a.count(66)
print a.count(66.25)
a.insert(2,0)
print a
a.append(2000)
a
#a.append(200,300,400)
#a.insert(1,200,2,300,3,400)
a.remove(333)
a

#Using list as stack
stack=[2,3,4,5,6,7]
stack.pop(5)
stack
stack.append(7)
stack

#Usinfg List as Queues
from collections import deque
queue=deque(["Eric","john","Micheal"])
queue.append("Terry")
queue.append("john")
queue
queue.popleft()
queue.popleft()
queue

#Functional programming tools
# filter(function,sequence)
def f(x):return x%3==0 or x%5==0
filter(f,range(2,20))

#map(function,sequence)
def cube1(x):return x**3
map(cube1,range(1,11))


seq=range(8)
def f(x,y): return x+y
map(f,seq,seq)
reduce(f,range(2,11))
reduce(f,range(11))

#list comprehensions
squares=[]
for x in range(10):
    squares.append(x**2)

squares


#Sets
basket=["apple","orange","grapes","orange"]
fruit=set(basket)
fruit
'orange' in fruit
