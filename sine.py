"""This program calculates the Taylor series of the function sin(x), around x0 = 0.
It alsos plots a graph of the sine function calculated for different N"""

import math
import numpy as np
import matplotlib.pyplot as plt

def taylor_sine (x,N):
    sine = 0
    n = int((N-1)/2)
    for n in range(0,n+1):
        sine += (((-1)**n)/math.factorial(2*n+1)*(x**(2*n+1)))
        print
    return sine


x = float(input('Enter the value of the angle you want to know the sine of (in radians): '))

N = int(input('Enter the value of N, knowing that N=2n+1 and "n" is the maximum exponent up to which the Taylor series will be calculated: '))

print('Sine calculated by the created function:', taylor_sine(x,N))

print('Math module sine function:', math.sin(x))

print('Difference between calculated and math module result', taylor_sine(x,N) - math.sin(x))


x = np.arange(0,(3*np.pi)/2,0.1)
y = np.sin(x)
y1 = taylor_sine(x,3)
y2 = taylor_sine(x,5)
y3 = taylor_sine(x,7)
y4 = taylor_sine(x,9)
xdegrees = x*180 /np.pi
plt.plot (xdegrees,y)
plt.plot (xdegrees,y1)
plt.plot (xdegrees,y2)
plt.plot (xdegrees,y3)
plt.plot (xdegrees,y4)
plt.legend(['sine',\
            'N=3',\
            'N=5',\
            'N=7',\
            'N=9'],loc=0)
plt.xlabel('Angle in radians (0 to 3pi/2)')
plt.ylabel('Sine(x)')
plt.title('Sine(x) chart')
plt.grid(True)
plt.ylim(-2,2)
plt.yticks()
plt.show()
