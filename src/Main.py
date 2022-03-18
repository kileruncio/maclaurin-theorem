#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import Logic as l

logic = l.Logic()
workN = 1
n = input("Provide n: ")
fun = input("Choose sin or cos: ")
space = np.linspace(-np.pi*5, np.pi*5, 400)

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
    print("You can provide only sin or cos, nothing else")
    exit(0)

print(f"n: {n} function: {fun}")

#drawing maclaurin's
if fun == "sin":
    print('Value of error: ', logic.errorsin(n))
    y = logic.sin(n*workN, space)
    print(y)
    plt.plot(space, y, 'g-', label=f"approximation to {n}")
elif fun == "cos":
    print('Value of error: ',  logic.erroscos(n))
    y = logic.cos(n*workN, space)
    print(y)
    plt.plot(space, y, 'g-', label=f"approximation to {n}")

plt.legend(loc='upper left')
plt.show()

