import os
import pickle
import subprocess

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

np.set_printoptions(threshold=np.inf)

# get & set path 
bin_dir = os.environ.get("EXPASCAL_BIN", "./tri_bin")
img_dir = os.environ.get("EXPASCAL_IMG", "./tri_img")

COMP_DIFFER = 0
COMP_SAME = 1

class Pascal:
    def __init__(self, devide, size, z_o_flag):
        self.devide: int = devide
        self.size: int = size
        self.z_o_flag: int = z_o_flag
        self.binpath: str = f"{bin_dir}tri/{self.devide}-{self.size}-{self.z_o_flag}tri.bin"
        self.imgpath: str = f"{img_dir}tri/{self.devide}-{self.size}-{self.z_o_flag}tri.png"
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
            triangle[0, 0] = 1
            return triangle

        if not os.path.exists(self.binpath):
            new_triangle = body(axis())
            if self.z_o_flag:
                new_triangle = np.where(new_triangle==0, 0, 1)
            self.save(new_triangle)

    def save(self, triangle):
        with open(self.binpath, mode="wb") as fi:
            pickle.dump(triangle, fi)
        print("new saved")
        return

    def get_contents(self) -> np.matrix:
        with open(self.binpath, mode="rb") as fi:
            triangle = pickle.load(fi)
        return triangle

    def create_fig(self):
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.imshow(self.get_contents(), cmap="Blues")
        plt.show()
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

class CompPascal(Pascal):
    def __init__(self, devide1, devide2, size, z_o_flag1, z_o_flag2, comp_type):
        self.devide: tuple[int, int] = (devide1, devide2)
        self.size: int = size
        self.z_o_flag: tuple[int, int] = (z_o_flag1, z_o_flag2)
        self.comp_type: int = comp_type
        self.binpath: str = f"{bin_dir}cmp/{self.devide}-{self.size}-{self.z_o_flag}-\
                {self.comp_type}tri.bin"
        self.imgpath: str = f"{img_dir}cmp/{self.devide}-{self.size}-{self.z_o_flag}-\
                {self.comp_type}tri.png"
        self.create_tri()
        self.create_fig()
        plt.show()

    def create_tri(self):
        pascal1 = Pascal(self.devide[0], self.size, self.z_o_flag[0])
        pascal2 = Pascal(self.devide[1], self.size, self.z_o_flag[1]) 
        if not os.path.exists(self.binpath):
            new_triangle = pascal1.get_contents() - pascal2.get_contents()
            if self.comp_type:
                new_triangle = np.where(new_triangle==0, 0, 1)
            self.save(new_triangle)


if __name__ == "__main__":
    pascal1 = CompPascal(*(3, 6), 100, *(1, 1), COMP_SAME)
