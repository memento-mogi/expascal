import objective
import numpy as np

def comp(pascal1, pascal2):
    comp = (pascal1.containts == pascal2.containts)
    print(np.count_nonzero(comp))

if __name__ == "__main__":
    comp(objective.Pascal(2,2), objective.Pascal(4,2))
