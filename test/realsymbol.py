
import sympy as sp
import numpy as np
import pprint
import matplotlib.pyplot as plt

SIZE = 30

a1 = sp.Symbol("a1")
a2 = sp.Symbol("a2")
a3 = sp.Symbol("a3")
a4 = sp.Symbol("a4")
a5 = sp.Symbol("a5")
a6 = sp.Symbol("a6")
a7 = sp.Symbol("a7")
a8 = sp.Symbol("a8")
a9 = sp.Symbol("a9")
a10 = sp.Symbol("a10")
m = sp.Symbol("m")
#m = 3

tri = np.ones((SIZE, SIZE)).tolist()
koho = [0, a1, a2, 0, -a1, -a2]
tri = np.ones((SIZE, SIZE)).tolist()
shuki = len(koho)
for i in range(1, SIZE):
    tri[0][i] = koho[i%shuki]
    tri[i][0] = koho[i%shuki]

for i in range(1,SIZE):
    for j in range(1,SIZE):
        tri[i][j] = (tri[i][j-1]+tri[i-1][j])
    print(i)

#for i in range(0, SIZE):
#    for j in range(0,SIZE):
#        num = tri[i][j]
#        tri[i][j] = 0 if num == 0 else 1

#np.savetxt('/home/maetaka-2020248/tri.txt', tri)
#plt.imshow(tri)
#plt.show()
print(tri)
