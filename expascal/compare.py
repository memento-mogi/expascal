import objective
import numpy as np

def comp(pascal1, pascal2):
    comp_l = (pascal1.contents == pascal2.contents)
    comp = np.count_nonzero(comp_l)
    return comp

if __name__ == "__main__":
    comp(objective.Pascal(2,2), objective.Pascal(4,2))
