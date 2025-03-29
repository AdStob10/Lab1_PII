import math

def pole_szczescianu(a):
    return 6*(a*a)

def objetosc_szescianu(a):
    return a*a*a

def pole_prostopadloscianu(a,b,c):
    return 2*(a*b) + 2*(a*c) + 2*(b*c)

def objetosc_prostopadloscianu(a,b,c):
    return a*b*c

def pole_kuli(r):
    return 4 * math.pi * (r**2)

def objetosc_kuli(r):
    return 4/3 * math.pi * (r**3)