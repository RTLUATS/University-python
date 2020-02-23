from math import *


# x^3+4x^2-6x+2=0 a= -6   b=-3,5

def function(x):
    res = x ** 3 + 4 * x ** 2 - 6 * x + 2
    return res


def dfunction(x):
    res = 3 * x ** 2 + 8 * x - 6
    return res


def tangent(end):
    x = end
    eps = 0.000001
    f = function(x)
    while fabs(f) > eps:
        f = function(x)
        df = dfunction(x)
        x = x - f / df
    return x


def chords(begin, end):
    eps = 0.000001
    while fabs((end - begin)) > eps:
        begin = end - (end - begin) * function(end) / (function(end) - function(begin))
        end = begin - (begin - end) * function(begin) / (function(begin) - function(end))
    return end


x_begin = -6
x_end = -3.5
print('Корень при помощи метода касательных =', tangent(x_end))
print('Корень при помощи метода хорд =', chords(x_begin, x_end))
