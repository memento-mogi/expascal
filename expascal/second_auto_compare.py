import os
import subprocess
import sys
import matplotlib.pyplot as plt
import numpy as np
import objective
import compare

SIZE = int(sys.argv[1])
PASCAL_SIZE = int(sys.argv[2])
#PERCENT =  int(sys.argv[3])
compare_l = np.zeros(int(SIZE/2))
compare_l[0] = (PASCAL_SIZE**2)/2
compare_l[1] = (PASCAL_SIZE**2)/2
pascal_l = [0,1]

for make_i in range(2, SIZE+1):
    pascal = objective.Pascal(make_i, PASCAL_SIZE)
    pascal.set_body(pascal.set_axis())
    pascal_l.append(pascal)

for i in range(2, int(SIZE/2)):
    compare_l[i] = compare.comp(pascal_l[i], pascal_l[i*2])

#compare_l = np.where(compare_l>=(SIZE**2)*PERCENT*0.01, 1, 0)


print(compare_l)
print(np.mean(compare_l))
print(np.min(compare_l))
print(np.max(compare_l))

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(range(int(SIZE/2)), compare_l, label="lab")

ax.grid(axis="x", alpha=0.8, linewidth=1)
ax.grid(axis="y", alpha=0.8, linewidth=1)

#filename = os.environ.get("EXPASCAL_IMG")+str(SIZE)+"-"+str(PASCAL_SIZE)+"-"+str(PERCENT)+"compareimg.png"
#ax = fig.add_subplot(1,1,1)
#ax.imshow(compare_l, cmap="Blues")
#fig.savefig(filename)
#subprocess.Popen("eog "+filename, shell=True)
plt.show()
