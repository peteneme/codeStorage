#!/usr/bin/python

import matplotlib.pyplot as plt

### https://matplotlib.org/stable/tutorials/introductory/pyplot.html


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')




### line , x axis default
plt.plot([1, 2, 3, 4])

### red dot
plt.plot([1, 2, 3, 4], [0, 3, 7, 4], 'ro')


plt.bar([1,2,3,5],[1,2,1,1])


plt.xlabel('x axis could be default data', fontsize=14, color='red')
plt.ylabel('some numbers')

plt.axis([0, 6, 0, 20])

plt.title('title')
plt.grid(True)

plt.show()