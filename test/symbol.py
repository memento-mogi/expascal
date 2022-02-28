import sympy as sp
import pprint
import numpy as np
SIZE = 16

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
a11 = sp.Symbol("a11")
a12 = sp.Symbol("a12")
a13 = sp.Symbol("a13")
m = sp.Symbol("m")

tri = np.ones((SIZE, SIZE)).tolist()
koho = [a8, a1, a2, a3, a4, a5, a6, a7]
shuki = len(koho)
for i in range(1, SIZE):
    tri[0][i] = koho[i%shuki]
    tri[i][0] = koho[i%shuki] * (-1)

for i in range(1,SIZE):
    for j in range(1,SIZE):
        tri[i][j] = (tri[i][j-1]+tri[i-1][j])
    print(i)


pprint.pprint(tri, width=1000)
