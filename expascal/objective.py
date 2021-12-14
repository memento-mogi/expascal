import numpy as np
import matplotlib.pyplot as plt
import subprocess

np.set_printoptions(threshold=np.inf)

class Pascal:    
    def __init__(self, devide, size):
        self.devide: int = devide
        self.size: int = size


    def set_axis(self) -> np.matrix:
        np.zeros(self.size)
        axis = [[1, 1]]
        for column_axis in range (2, self.size):
            thenum = (axis[0][column_axis-1]+axis[0][column_axis-2]) % self.devide
            axis[0].append(thenum)
        
        temp_body = np.zeros((self.size-1,self.size))
        axis_1 = np.concatenate((axis, temp_body))
        axis_1 = np.mat(axis_1, dtype="int16")
        axis_2 = axis_1.T
        return(axis_1 + axis_2)


    def set_body(self, triangle) -> np.matrix:
        for row in range(1, self.size):
            for column in range(1, self.size):
                thenum = (triangle[row-1, column] + triangle[row, column-1]) % self.devide
                triangle[row, column] = thenum
        triangle[0,0] = 1
        return triangle

    def create_image(self):
        filename = "/home/maetaka-2020248/projects_python/projects_expascal/img/" + str(self.devide)+"-"+str(self.size)+"img.png"
        fig = plt.figure(dpi=1024)
        ax = fig.add_subplot(1,1,1)
        ax.imshow(self.containts, cmap="Blues")
        fig.savefig(filename)
        subprocess.Popen("eog "+filename, shell=True)
        return

    def count(self):
        isZero = np.count_nonzero(self.containts==0)
        print(isZero,"/",self.size**2)
        return

    def toZeroone(self):
        self.containts = np.where(self.containts==0, 0, 1)

if __name__ == "__main__":
    pascal1 = Pascal(4, 34)
    pascal1.containts = pascal1.set_body(pascal1.set_axis())
    print(pascal1.containts)
    pascal1.count()
