import os
import subprocess
import sys
import matplotlib.pyplot as plt
import numpy as np
import objective
import compare

SIZE = int(sys.argv[1])
PASCAL_SIZE = int(sys.argv[2])
PERCENT =  int(sys.argv[3])
compare_l = np.zeros((SIZE+1, SIZE+1))
pascal_l = [0,1]

for make_i in range(2, SIZE+1):
    pascal = objective.Pascal(make_i, PASCAL_SIZE)
    pascal.set_body(pascal.set_axis())
    pascal_l.append(pascal)

for i in range(2,SIZE+1):
    for j in range(i+1,SIZE+1):
        compare_l[i,j] = compare.comp(pascal_l[i], pascal_l[j])

compare_l = np.where(compare_l>=(SIZE**2)*PERCENT*0.01, 1, 0)

filename = os.environ.get("EXPASCAL_IMG")+str(SIZE)+"-"+str(PASCAL_SIZE)+"-"+str(PERCENT)+"compareimg.png"
fig = plt.figure(dpi=1024)
ax = fig.add_subplot(1,1,1)
ax.imshow(compare_l, cmap="Blues")
fig.savefig(filename)
subprocess.Popen("eog "+filename, shell=True)
 
