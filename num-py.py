#Numpy Library
#Used for scientific computing
from random import randint
import numpy as np
#creating array using numpy
a=np.array([[randint(2,98), randint(2,98),randint(2,98)],
            [randint(2,98), randint(2,98),randint(2,98)],
            [randint(2,98), randint(2,98),randint(2,98)]])
#Random array generation
print(a)
print(type(a))
# type is numpy type array
#initailising zeroes in the array
print(a.shape)  #prints shape of the array
print(a[0][1])
print(a[0,1])
b=np.zeros((4,4)) #this command is easier using numpy
print(b)
#initialising ones in the array
c=np.ones((4,4))
print(c)
#initialising with a value
d=np.full((4,5),200)
print(d)
#identity matrix using numpy
e=np.eye(4) #One value is enough as it is a square matrix
print(e)
#random generation of a array using numpy
f= np.random.randint(2,98,(3,3))
print(f)


# Matrix operations using numpy
x=np.array([[1,2,3],[4,5,6],[1,2,3]])
y=np.array([[7,8,9],[10,11,12],[2,3,4]])
print(x+y)             #Addition of two matrices
#Subtrction in-built funtion
b=np.subtract(y,x)
print(b)
b=np.multiply(y,x) #Multiplies corresponding row elements NOT MATRIX MULTIPLY
print(b)
b=np.divide(y,x) #Divides corresponding row elements NOT MATRIX DIVISION
print(b)
# b.ndim gives dimension of the array

#For Matrix Multiplication
b=np.dot(x,y)
print(b)
