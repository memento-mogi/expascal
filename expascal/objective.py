import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pickle

np.set_printoptions(threshold=np.inf)
imgpath = os.environ.get("EXPASCAL_IMG")
binpath = os.environ.get("EXPASCAL_BIN")

class Pascal:
    def __init__(self, devide, size, z_o_flag):
        self.devide: int = devide
        self.size: int = size
        self.z_o_flag: int = z_o_flag
        self.path: str = f"{binpath}{self.devide}-{self.size}-{self.z_o_flag}tri.bin"

    def create_tri(self):
        def axis() -> np.matrix:
            np.zeros(self.size)
            axis = [[1, 1]]
            for column_axis in range (2, self.size):
                thenum = (axis[0][column_axis-1]+axis[0][column_axis-2]) % self.devide
                axis[0].append(thenum)
            temp_body = np.zeros((self.size-1, self.size))
            axis_1 = np.concatenate((axis, temp_body))
            axis_1 = np.mat(axis_1, dtype="int32")
            axis_2 = axis_1.T
            return (axis_1 + axis_2)

        def body(triangle) -> np.matrix:
            for row in range(1, self.size):
                for column in range(1, self.size):
                    thenum = (triangle[row-1, column] + triangle[row, column-1]) % self.devide
                    triangle[row, column] = thenum 
            triangle[0,0] = 1
            return triangle

        def save(triangle):
            with open(self.path, mode="wb") as fi:
                pickle.dump(triangle, fi)
            return

        if not os.path.exists(self.path):
            new_triangle = body(axis())
            save(new_triangle)

    def contents(self) -> np.matrix:
        with open(self.path, mode="rb") as fi:
            triangle = pickle.load(fi)
        return triangle

    def view_image(self):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.imshow(self.contents(), cmap="Blues")
        return fig

    def count(self):
        notzero_num = np.count_nonzero(self.contents())
        all_num = self.size**2
        return f"{all_num - notzero_num}/{all_num}"


if __name__ == "__main__":
    pascal1 = Pascal(7, 34, 1)
    pascal1.create_tri()
    print(pascal1.contents())
    pascal1.view_image()
    plt.show()
    print(pascal1.count())
