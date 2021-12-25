import os
import numpy as np
import matplotlib.pyplot as plt
import pickle

np.set_printoptions(threshold=np.inf)
imgpath = os.environ.get("EXPASCAL_IMG")
binpath = os.environ.get("EXPASCAL_BIN")

TYPENO_BIN = 0
TYPENO_IMG = 1

class Pascal:
    def __init__(self, devide, size, z_o_flag):
        self.devide: int = devide
        self.size: int = size
        self.z_o_flag: int = z_o_flag
        self.paths_full: tuple = (f"{binpath}{self.devide}-{self.size}-{self.z_o_flag}tri.bin",
                                  f"{imgpath}{self.devide}-{self.size}-{self.z_o_flag}tri.png")

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
            with open(f"{self.paths_full[TYPENO_BIN]}", mode="wb") as fi:
                pickle.dump(triangle, fi)
            return

        if not self.exist_check(TYPENO_BIN):
            new_triangle = body(axis())
            save(new_triangle)

    def exist_check(self, file_type) -> bool:
        return os.path.exists(f"{self.paths_full[file_type]}")

    def contents(self) -> np.matrix:
        print(f"{self.paths_full[TYPENO_BIN]}")
        with open(f"{self.paths_full[TYPENO_BIN]}", mode="rb") as fi:
            triangle = pickle.load(fi)
        return triangle

    def create_image(self):
        plt.imshow(self.contents(), cmap="Blues")
        plt.show()
        return

    def count(self):
        isZero = np.count_nonzero(self.contents==0)
        print(isZero, "/", self.size**2)
        return


if __name__ == "__main__":
    pascal1 = Pascal(7, 34, 1)
    pascal1.create_tri()
    print(pascal1.contents())
    pascal1.create_image()
    print(pascal1.exist_check(TYPENO_BIN))
