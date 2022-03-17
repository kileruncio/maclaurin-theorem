from math import factorial, pi
import math
import numpy as np

class Logic:
    #maclaren sinus
    def sin(self, n, space):
        a = int(n)
        y = []

        for x in space:
            q = math.sin(0)
            w = -1

            for i in range(1, a):
                if i%2 == 1:
                    q += ((w*pow(x,i))/factorial(i))
                    if w < 0:
                        w = 1
                    else:
                        w = -1
            y.append(-q)
        return y

    #maclaren cosinus
    def cos(self, n, space):
        a = int(n)
        y = []
        w = -1

        for x in space:
            q = math.cos(0)

            for i in range(1, a):
                if i%2 == 0:
                    q += ((w*pow(x,i))/math.factorial(i))
                    if w < 0:
                        w = 1
                    else:
                        w = -1
            y.append(q)
        return y

    #errors
    def errorsin(self, n):
        a = int(n)
        try:
            if a%2 == 1:
                return abs(pow(pi, a+3)/factorial(a+2))
            else:
                return abs(pow(pi, a+2)/factorial(a+1))
        except OverflowError:
            print(f"Jezyk nie radzi sobie z tak duza liczba jak {a}")
            exit(0)

    def erroscos(self, n):
        a = int(n)
        if a%2 == 1:
            return (pi-1)*abs(pow(pi-1, a+2)/factorial(a+2))
        else:
            return (pi-1)*abs(pow(pi, a+1)/factorial(a+1))
