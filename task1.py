from math import *


# 2sin(0,53x) – cos^2(x)=0
def function_y(x):
    res = 2 * sin(0.53 * x) - cos(x) ** 2
    return res


def find_root(begin, end):
    eps = 0.00001
    while fabs(end - begin) >= eps:
        fun1 = function_y(begin)
        temp = (begin + end) / 2
        fun2 = function_y(temp)
        if fun1 * fun2 <= 0:
            end = temp
        else:
            begin = temp
    root = (begin + end) / 2
    return root


x_begin = 0
x_end = 15
list_x = []
controll = 0
for x in range(x_begin, x_end):
    result = function_y(x)
    if (result < 0) and (controll == 0):
        list_x.append(x)
        controll += 1
    elif (result > 0) and (controll == 1):
        list_x.append(x)
        controll -= 1
print('Регион нахождения кореней уравнения и сами корни:')
for x in range(len(list_x) - 1):
    print('(', list_x[x], ',', list_x[x + 1], ') корень = ', find_root(list_x[x], list_x[x + 1]))


# end find a range of isolaction
