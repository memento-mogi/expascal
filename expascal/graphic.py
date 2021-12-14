import tkinter as tk
from tkinter import ttk
import objective
import compare as comp

root = tk.Tk()
root.title("拡張パスカルの三角形")
root.geometry("1000x800")

#table setting
table = ttk.Treeview(root)
table["columns"] = (0,1,2)
table.column(0,width=75)
table.column(1,width=75)
table.column(2,width=100)
table.heading(0, text="No.")
table.heading(1, text="size")
table.heading(2, text="devide")
table.place(x=100, y=200)

pascal_list = []
index = -1

def create():
    global index
    devide = int(devide_inbox.get())
    size = int(size_inbox.get())
    pascal = objective.Pascal(devide, size)
    pascal_list.append(pascal)

    index = index + 1
    pascal.containts = pascal.set_body(pascal.set_axis())
    table.insert("","end",values=(index, size, devide))
    return

def save():
    num = int(no1_inbox.get())
    pascal_list[index].create_image()
    return

def count():
    num = int(no1_inbox.get())
    pascal_list[index].count()
    return

def compare():
    num_a = int(no1_inbox.get())
    num_b = int(no2_inbox.get())
    if pascal_list[num_a].size == pascal_list[num_b].size:
        comp.comp(pascal_list[num_a], pascal_list[num_b])
    else:
        print("同じサイズで比較して下さい")
    return

label_s = ttk.Style().configure("TLabel", foreground="black", background="white", font=("",30))
button_s = ttk.Style().configure("TButton", foreground="red", background="gray", font=("",30))

#status input
ttk.Label(text="size").grid(row=0, column=0)
size_inbox = ttk.Entry(width=15, font=("", 20))
size_inbox.grid(row=0, column=1)
ttk.Label(text="devide").grid(row=1, column=0)
devide_inbox = ttk.Entry(width=15, font=("", 20))
devide_inbox.grid(row=1, column=1)

#number input
ttk.Label(text="no1").grid(row=0, column=2)
no1_inbox = ttk.Entry(width=15, font=("", 20))
no1_inbox.grid(row=0, column=3)
ttk.Label(text="no2").grid(row=1, column=2)
no2_inbox = ttk.Entry(width=15, font=("", 20))
no2_inbox.grid(row=1, column=3)

ttk.Button(root, text="create", command=create).grid(row=2, column=1)
ttk.Button(root, text="save", command=save).grid(row=2, column=2)
ttk.Button(root, text="count", command=count).grid(row=2, column=3)
ttk.Button(root, text="compare", command=compare).grid(row=2, column=4)

root.mainloop()
