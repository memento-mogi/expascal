import sympy as sp

a1 = sp.Symbol("a1")
a2 = sp.Symbol("a2")
a3 = sp.Symbol("a3")
a4 = sp.Symbol("a4")
a5 = sp.Symbol("a5")
a6 = sp.Symbol("a6")
a7 = sp.Symbol("a7")
a8 = sp.Symbol("a8")

lis = [a1, a2, a3, a4, a5, a6, a7, a8]
summ = 0
counter = 0

for i in range(6):
    for j in range(i+1):
        for k in range(j+1):
            for l in range(k+1):
                for m in range(l+1):
                    for n in range(m+1):
                        summ = summ + lis[n]
                        counter += 1
                        print(counter)

print(summ)
