#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pprint
import time

size = 501
divide = 32

tri_l = []
tri_axis = np.empty(size, dtype=np.int64)

# 軸の数列生成
np.put(tri_axis, [0, 1], 1) 

for column_axis in range (2, size):
    thenum = (tri_axis[column_axis-1]+tri_axis[column_axis-2]) % divide
    np.put(tri_axis, column_axis, thenum)

print(tri_axis)

tri_axis_l = tri_axis.tolist()
tri_l.append(tri_axis_l)

prevrow = tri_axis

# 中身生成
for row in range(1, size):
    tri_row = np.empty(size, dtype=np.int64)
    np.put(tri_row, 0, tri_axis[row])

    for column in range(1, size):
        thenum = (prevrow[column] + tri_row[column-1]) % divide
        np.put(tri_row, column, thenum)

    prevrow = tri_row

    tri_row_l = tri_row.tolist()
    tri_l.append(tri_row_l)
    

tri_show = np.array(np.where(np.array(tri_l)==0,0,1))

filename = str(divide)+"img.png"

fig = plt.figure(dpi=1024)
ax = fig.add_subplot(1,1,1)
ax.imshow(tri_show, cmap="Blues")

fig.savefig(filename)
