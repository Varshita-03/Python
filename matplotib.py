#Matplotib is installed
"""Matplotib is used for plotting graphs and visualisation of data"""

import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0,3*np.pi,0.1) #0.1 to ensure pointing at eveery point
y_cos=np.cos(x) #x has range from 0 to 3*pi
y_sin=np.sin(x)
plt.xlabel('Angle(in theta)') #prints x and y-axis labels
plt.ylabel('Value')
plt.plot(x,y_cos)
plt.plot(x,y_sin)
plt.legend(['cos','sine'])
plt.title('Graphs on sine and cosine')

"""x=[0,2,4,6,8,10]
y=[0,1,2,3,4,5]
plt.plot(x,y)"""

