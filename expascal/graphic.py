import os
import glob
import re
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import objective
import compare as comp

pascal_list = []
index = 0

def list_init():
    global index
    for tri_bin in glob.glob("../tri_bin/*"):
        read_num = re.findall(r"\d+", tri_bin)
        args = [int(i) for i in read_num]
        pascal_list.append(objective.Pascal(args[0], args[1], args[2]))
        table.insert("","end",values=(index, args[0], args[1], bool(args[2])))
        index += 1

def create():
    global index
    global z_o_flag
    devide = int(devide_inbox.get())
    size = int(size_inbox.get())
    pascal = objective.Pascal(devide, size, int(z_o_flag.get()))
    pascal_list.append(pascal)

    pascal.create_tri()

    table.insert("","end",values=(index, devide, size, z_o_flag.get()))
    index += 1
    return

def view():
    num = int(no1_inbox.get())
    fig = pascal_list[num].view_image()
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().place(x=350, y=200)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    return

def count():
    num = int(no1_inbox.get())
    print(pascal_list[num].count())
    return

def compare():
    num_a = int(no1_inbox.get())
    num_b = int(no2_inbox.get())
    if pascal_list[num_a].size == pascal_list[num_b].size:
        print(comp.comp(pascal_list[num_a].contents(), pascal_list[num_b].contents()))
    else:
        print("同じサイズで比較して下さい")
    return

# tk setting
root = tk.Tk()
root.title("拡張パスカルの三角形")
root.geometry("1000x800")

# checkbox var
z_o_flag = tk.BooleanVar()

# styles
label_s = ttk.Style().configure("TLabel", foreground="black", background="white", font=("",30))
button_s = ttk.Style().configure("TButton", foreground="red", background="gray", font=("",30))

# status input boxes
ttk.Label(text="size").grid(row=0, column=0)
size_inbox = ttk.Entry(width=15, font=("", 20))
size_inbox.grid(row=0, column=1)
ttk.Label(text="devide").grid(row=1, column=0)
devide_inbox = ttk.Entry(width=15, font=("", 20))
devide_inbox.grid(row=1, column=1)
zeroone_check = ttk.Checkbutton(onvalue=1, offvalue=0, variable=z_o_flag, text="01only")
zeroone_check.grid(row=2, column=0)

# indexnumber input boxes
ttk.Label(text="no1").grid(row=0, column=2)
no1_inbox = ttk.Entry(width=15, font=("", 20))
no1_inbox.grid(row=0, column=3)
ttk.Label(text="no2").grid(row=1, column=2)
no2_inbox = ttk.Entry(width=15, font=("", 20))
no2_inbox.grid(row=1, column=3)

# buttons
ttk.Button(root, text="create", command=create).grid(row=2, column=1)
ttk.Button(root, text="view", command=view).grid(row=2, column=2)
ttk.Button(root, text="count", command=count).grid(row=2, column=3)
ttk.Button(root, text="compare", command=compare).grid(row=2, column=4)

# table
table = ttk.Treeview(root)
table["columns"] = (1,2,3,4)
table["show"] = "headings"
table.column(1, width=70)
table.column(2, width=70)
table.column(3, width=70)
table.column(4, width=70)
table.heading(1, text="No.")
table.heading(2, text="devide")
table.heading(3, text="size")
table.heading(4, text="01")
table.place(x=50, y=150)

# plt toolbar
toolbarFrame = tk.Frame(master=root)
toolbarFrame.place(x=350+index*100, y=150)

list_init()
root.mainloop()
