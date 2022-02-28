import numpy as np

if __name__ == "__main__":
    import objective
    pascal1 = objective.Pascal(4, 1000, 1)
    pascal2 = objective.Pascal(2, 1000, 1)
    print(difference(pascal1, pascal2))
