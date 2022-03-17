#!/usr/bin/python3
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import Logic as l

# print(pow(2, 2))

""" 
x=[1,3,5,7]
y=[2,4,6,1]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("A simple line graph")
plt.show() 
"""
logic = l.Logic()
workN = 1
n = input("Podaj n ")
fun = input("Podaj sin lub cos ")
space = np.linspace(-np.pi*5, np.pi*5, 400)
# print('Blad wynosi: ', l.Logic.errorsin(n))

#drawing axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlim(-np.pi*5, np.pi*5)
ax.set_ylim(-10, 10)

#drawing sin or cos
if fun == "sin":
    y = np.sin(space)
    plt.plot(space, y, 'b-', label='sin(x)')
elif fun == "cos":
    y = np.cos(space)
    plt.plot(space, y, 'b-', label='cos(x)')
else:
    print("Niedozwolona wartosc")
    exit(0)

print("n: " + n + " funkcja: " + fun)

#drawing maclaurin's
if fun == "sin":
    print('Blad wynosi: ', logic.errorsin(n))
    y = logic.sin(n*workN, space)
    print(y)
    plt.plot(space, y, 'g-', label=f"approximation to {n}")
elif fun == "cos":
    print('Blad wynosi: ',  logic.erroscos(n))
    # space = np.linspace(-np.pi*15,np.pi*15,1000)
    y = logic.cos(n*workN, space)
    print(y)
    plt.plot(space, y, 'g-', label=f"approximation to {n}")

plt.legend(loc='upper left')
plt.show()

