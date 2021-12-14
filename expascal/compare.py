import objective
import numpy as np

def comp(pascal1, pascal2):
    pascal1.containts = pascal1.set_body(pascal1.set_axis())
    pascal2.containts = pascal2.set_body(pascal2.set_axis())
    comp = (pascal1.containts == pascal2.containts)
    print(np.sum(comp))


if __name__ == "__main__":
    compare(objective.Pascal(2,2), objective.Pascal(4,2))
