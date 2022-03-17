from math import factorial, pi
import math
import numpy as np

class Logic:
    #maclaren sinus
    def sin(self, n):
        a = int(n)
        tmp = 1
        y = []

        space = np.linspace(-pi*15, -22.5, int((200-a)/2))
        for x in space:
            y.append(-math.pow(x, 2))

        for i in range(a+2):
            if tmp%2 == 0:
                y.append(-(a*(math.sin(pi/2)*pow(i,a))/factorial(a)))
                tmp += 1
            else:
                y.append(a*(math.sin(pi/2)*pow(i,a))/factorial(a))
                tmp += 1

        space = np.linspace(22.5, pi*15, int((200-a)/2)-1)
        for x in space:
            y.append(math.pow(x, 2))

        while len(y) != 200:
            if len(y) < 200:
                y.insert(0, -pow(y[0]-1, 2))
            else:
                y.pop()

        return y

    #maclaren cosinus
    def cos(self, n):
        a = int(n)
        tmp = 1
        y = [1]

        space = np.linspace(-pi*15, -22.5, int((200-a)/2))
        for x in space:
            y.append(-math.pow(x, 2))

        for i in range(a+2):
            # y.append(a * (math.sin(math.pi/2) * pow(i,a))/math.factorial(a))
            if tmp%2 == 0:
                y.append(a * (math.sin(math.pi/2) * pow(i,a))/math.factorial(a))
                tmp += 1
            else:
                y.append(-a * (math.sin(math.pi/2) * pow(i,a))/math.factorial(a))
                tmp += 1

        space = np.linspace(22.5, pi*15, int((200-a)/2)-1)
        for x in space:
            y.append(math.pow(x, 2))

        while len(y)!= 200:
            if len(y) < 200:
                y.insert(0, -pow(y[0]-1, 2))
            else:
                y.pop()
        return y

    #errors
    def errorsin(self, n):
        a = int(n)
        if a%2 == 1:
            return abs(pow(pi, a+3)/factorial(a+2))
        else:
            return abs(pow(pi, a+2)/factorial(a+1))

    def erroscos(self, n):
        a = int(n)
        if a%2 == 1:
            return (pi-1)*abs(pow(pi-1, a+2)/factorial(a+2))
        else:
            return (pi-1)*abs(pow(pi, a+1)/factorial(a+1))
