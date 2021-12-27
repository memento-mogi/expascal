import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pickle
import subprocess

np.set_printoptions(threshold=np.inf)
bin_dir = os.environ.get("EXPASCAL_BIN")
img_dir = os.environ.get("EXPASCAL_IMG")

class Pascal:
    def __init__(self, devide, size, z_o_flag):
        self.devide: int = devide
        self.size: int = size
        self.z_o_flag: int = z_o_flag
        self.binpath: str = f"{bin_dir}{self.devide}-{self.size}-{self.z_o_flag}tri.bin"
        self.imgpath: str = f"{img_dir}{self.devide}-{self.size}-{self.z_o_flag}tri.png"
        self.create_tri()

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
            with open(self.binpath, mode="wb") as fi:
                pickle.dump(triangle, fi)
            print("new saved")
            return

        if not os.path.exists(self.binpath):
            new_triangle = body(axis())
            if self.z_o_flag:
                new_triangle = np.where(new_triangle==0, 0, 1)
            save(new_triangle)

    def get_contents(self) -> np.matrix:
        with open(self.binpath, mode="rb") as fi:
            triangle = pickle.load(fi)
        return triangle

    def create_fig(self):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.imshow(self.get_contents(), cmap="Blues")
        return fig

    def view_img(self):
        fig = plt.figure(dpi=1024)
        ax = fig.add_subplot(111)
        ax.imshow(self.get_contents(), cmap="Blues")
        fig.savefig(self.imgpath)
        subprocess.Popen(f"eog {self.imgpath}", shell=True)


    def count_zeros(self):
        notzero_num = np.count_nonzero(self.get_contents())
        all_num = self.size**2
        return f"{all_num - notzero_num}/{all_num}"


if __name__ == "__main__":
    pascal1 = Pascal(3, 10, 1)
#    print(pascal1.contents())
#    pascal1.create_fig()
#    plt.show()
    pascal1.view_img()
