import numpy as np
import matplotlib.pyplot as plt

#def axis() -> np.matrix:
#    np.zeros(self.size)
#    axis = [[1, 1]]
#    temp_body = np.zeros((self.size-1, self.size))
#    axis_1 = np.concatenate((axis, temp_body))
#    axis_1 = np.mat(axis_1, dtype="int32")
#    axis_2 = axis_1.T
#    return (axis_1 + axis_2)

def body(SIZE, DIVIDE) -> np.matrix:
    triangle = np.ones((SIZE, SIZE))
    for row in range(1, SIZE):
        for column in range(1, SIZE):
            thenum = (triangle[row-1, column] + triangle[row, column-1]) % DIVIDE
            triangle[row, column] = thenum
    return triangle


def view(tri):
    return

if __name__=="__main__":
    plt.imshow(body(400, 2), cmap="Blues")
    plt.show()
