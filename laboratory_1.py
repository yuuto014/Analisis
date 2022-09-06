import numpy as np 
import matplotlib.pylab as plt

a = 2
b = 3
a+b,a*b

#generate an array of random numbers (range numbers, size array)
rm = np.random.randint(0,10,(4,5))
rm
#plot numbers 
plt.plot(rm)
#to watch the graphic using 
plt.show()