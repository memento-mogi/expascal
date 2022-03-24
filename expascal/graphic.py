import glob
import os
import re
import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.colors as mcolors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import triangles

# get & set path 
bin_dir = os.environ.get("EXPASCAL_BIN", "./tri_bin")
img_dir = os.environ.get("EXPASCAL_IMG", "./tri_img")

comp_sign = ["ー", "＝"]

class MyApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.master = master

        self.master.title("拡張パスカルの三角形")
        self.master.attributes("-fullscreen", True)

        self.index = 0
        self.triangle_list = []
        self.z_o_flag = tk.BooleanVar()
        
        self.set_widgets()
        self.set_viewarea(1)

    def set_widgets(self):
        # styles
        ttk.Style().configure("TLabel", foreground="#111111", background="#dcdcdc", font=("",15))
        ttk.Style().configure("TButton", foreground="#003200", background="#f0fff0", font=("",25))

        # label
        self.label_no1 = ttk.Label(self)
        self.label_no1.configure(text="No1")
        self.label_no1.grid(row=0, column=0)

        self.label_no2 = ttk.Label(self)
        self.label_no2.configure(text="No2")
        self.label_no2.grid(row=1, column=0)
        
        # entry
        self.entry_no1 = ttk.Entry(self)
        self.entry_no1.configure(width=15, font=("", 20))
        self.entry_no1.grid(row=0, column=1)

        self.entry_no2 = ttk.Entry(self)
        self.entry_no2.configure(width=15, font=("", 20))
        self.entry_no2.grid(row=1, column=1)

        # checkbutton
        self.checkbtn_zeroone = ttk.Checkbutton(self)
        self.checkbtn_zeroone.configure(text="01only", onvalue=1, offvalue=0,
                                        variable=self.z_o_flag)
        self.checkbtn_zeroone.grid(row=2, column=0)

        # button
        self.button_create = ttk.Button(self)
        self.button_create.configure(text="create", command=self.create)
        self.button_create.grid(row=2, column=1)

        self.button_compare = ttk.Button(self)
        self.button_compare.configure(text="compare", command=self.compare)
        self.button_compare.grid(row=3, column=1)

        self.button_view = ttk.Button(self)
        self.button_view.configure(text="view", command=self.view)
        self.button_view.grid(row=4, column=1)

        self.button_eog = ttk.Button(self)
        self.button_eog.configure(text="eog", command=self.call_view_eog)
        self.button_eog.grid(row=5, column=1)

        self.button_count = ttk.Button(self)
        self.button_count.configure(text="count", command=self.call_count)
        self.button_count.grid(row=6, column=1)

        self.button_viewset = ttk.Button(self)
        self.button_viewset.configure(text="分割", command=self.call_setviewarea)
        self.button_viewset.grid(row=7, column=1)

        # table
        self.table = ttk.Treeview(self)
        self.table["columns"] = (1,2,3,4,5)
        self.table["show"] = "headings"
        self.table.column(1, width=70)
        self.table.column(2, width=40)
        self.table.column(3, width=40)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.heading(1, text="No.")
        self.table.heading(2, text="devide")
        self.table.heading(3, text="size")
        self.table.heading(4, text="01")
        self.table.heading(5, text="comp")
        self.table.grid(row=8, column=0, columnspan=2)

    def set_viewarea(self, num):
        subplot_devide = ((1,1), (1,2), (2,2), (2,2), (2,3), (2,3))
        self.plt_frame = tk.Frame(self)
        self.plt_frame.grid(row=0, column=2, rowspan=11)
        fig = matplotlib.figure.Figure(figsize=(12.5, 7.7), dpi=100)
        fig.subplots_adjust(left=0, right=1, bottom=0.05, top=0.95, wspace=0, hspace=0.1)
        self.axes = []
        for i in range(1, num+1):
            ax = fig.add_subplot(subplot_devide[num-1][0], subplot_devide[num-1][1], i)
            ax.set_aspect('equal')
            self.axes.append(ax)
        self.canvas = FigureCanvasTkAgg(fig, self.plt_frame)
        self.canvas.get_tk_widget().pack(expand=True)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plt_frame)

    def list_init(self):
        # fill normal triangle table
        for tri_bin_path in glob.glob(f"{bin_dir}tri/*"):
            tri_bin_path = tri_bin_path.split("/")[-1]
            read_num = re.findall(r"(\d+)", tri_bin_path)
            args = [int(i) for i in read_num]
            self.triangle_list.append(triangles.Pascal(*args))
            self.table.insert("", "end", values=(self.index, args[0], args[1], bool(args[2])))
            self.index += 1

        # fill compare triangle table
        for tri_bin_path in glob.glob(f"{bin_dir}cmp/*"):
            tri_bin_path = tri_bin_path.split("/")[-1]
            read_num = re.findall(r"(\d+)", tri_bin_path)
            args = [int(i) for i in read_num]
            self.triangle_list.append(triangles.CompPascal(*args))
            self.table.insert("", "end", values=(self.index, (args[0], args[1]), args[2],\
                    (bool(args[3]), bool(args[4])), comp_sign[args[5]]))
            self.index += 1

    def create(self):
        devide = int(self.entry_no1.get())
        size = int(self.entry_no2.get())
        triangle = triangles.Pascal(devide, size, int(self.z_o_flag.get()))
        self.triangle_list.append(triangle)
        self.table.insert("", "end", values=(self.index, devide, size, self.z_o_flag.get()))
        self.index += 1
        return

    def compare(self):
        index_a = int(self.entry_no1.get())
        index_b = int(self.entry_no2.get())
        pascal_a = self.triangle_list[index_a]
        pascal_b = self.triangle_list[index_b]

        # error handling
        if isinstance(pascal_a, triangles.CompPascal) or \
                isinstance(pascal_b, triangles.CompPascal):
            print("f-パスカルの三角形どうしで比較してください")
            return
        if pascal_a.size != pascal_b.size:
            print("同じサイズで比較して下さい")
            return

        devides = (pascal_a.devide, pascal_b.devide)
        size = pascal_a.size
        z_o_flags = (pascal_a.z_o_flag, pascal_b.z_o_flag)
        comp_type = int(self.z_o_flag.get())

        triangle = triangles.CompPascal(*devides, size, *z_o_flags, comp_type)
        self.triangle_list.append(triangle)
        z_o_flags_show = (bool(z_o_flags[0]), bool(z_o_flags[1]))
        self.table.insert("", "end", values=(self.index, devides, size, z_o_flags_show,\
                comp_sign[comp_type]))
        self.index += 1
        return

    def view(self):
        num = int(self.entry_no1.get())
        ax_no = int(self.entry_no2.get())
        norm = mcolors.TwoSlopeNorm(vcenter=0)
        self.axes[ax_no-1].imshow(self.triangle_list[num].get_contents(),\
                cmap="seismic_r", norm=norm)
        self.canvas.draw()
        return

    def call_view_eog(self):
        num = int(self.entry_no1.get())
        self.triangle_list[num].view_img()
        return

    def call_count(self):
        num = int(self.entry_no1.get())
        print(self.triangle_list[num].count_zeros())
        return

    def call_setviewarea(self):
        num = int(self.entry_no1.get())
        self.set_viewarea(num)

def main():
    root = tk.Tk()
    app = MyApp(master=root)
    app.list_init()
    root.mainloop()

if __name__ == "__main__":
    main()
