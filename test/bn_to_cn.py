"""Generate Cn from Bn"""

import numpy as np
import sympy as sp

def generate(SIZE, B_PERIOD):
    # create axis
    axis = [[0]]
    for i in range(SIZE-1):
        b_index = (i % B_PERIOD) + 1
        axis[0].append(sp.Symbol(f"b{b_index}"))

    temp_body = np.zeros((SIZE-1, SIZE))
    axis_1 = np.concatenate((axis, temp_body))
    axis_1 = np.mat(axis_1)
    axis_2 = axis_1.T * (-1)
    triangle = axis_1 + axis_2
    triangle[0, 0] = 0

    # create body & extract Cn
    Cn = [sp.Symbol("b1")]
    for i in range(1,SIZE):
        for j in range(1,SIZE):
            thenum = triangle[i, j-1]+triangle[i-1, j]
            triangle[i, j] = thenum
            if j - i == 1:
                Cn.append(thenum)

    return Cn


if __name__ == "__main__":
    # input option
    while 1:
        size = input("size: ")
        if size.isnumeric() and int(size) >= 2:
            break
        print("2以上の整数で入力してください")

    while 1:
        b_period = input("period of Bn: ")
        if b_period.isnumeric() and int(b_period) >= 1:
            break
        print("自然数で入力してください")
    
    print(generate(int(size), int(b_period)))
    
