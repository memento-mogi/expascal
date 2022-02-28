import sympy as sp
import numpy as np
import pprint

SIZE = 60

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

#a = []
koho = [0, 0, 0, a1, a2, a1, 0, 0, 0, -a1, -a2, -a1]
shuki = len(koho)

#print(a)
tri = np.ones((SIZE, SIZE)).tolist()

for i in range(SIZE):
    for j in range(SIZE-1-i):
        tri[i][j] = 0
    tri[i][SIZE-1-i] = koho[i%shuki]

for i in range(1, SIZE):
    for j in range(SIZE-i,SIZE):
        tri[i][j] = tri[i-1][j] + tri[i][j-1]

print("do")

for i in range(0, SIZE):
    for j in range(SIZE-1-i,SIZE):
        num = tri[i][j]
        tri[i][j] = 0 if num == 0 else 1

pprint.pprint(tri, width=1000)
