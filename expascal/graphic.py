import tkinter as tk
import tkinter.font
import objective

root = tk.Tk()
root.title("拡張パスカルの三角形")
root.geometry("1000x800")

def create():
    devide = int(devide_inbox.get())
    size = int(size_inbox.get())
    global pascal1
    pascal1 = objective.Pascal(devide, size)
    pascal1.containts = pascal1.set_body(pascal1.set_axis())

def save():
    pascal1.create_image()

def count():
    pascal1.count()

FONT = tk.font.Font(
        root,
        family="Helvetica",
        size=20)

devide_label = tk.Label(text="devide", fg="black", font=FONT).grid(row=1, column=0)
devide_inbox = tk.Entry(width=15, font=FONT)
devide_inbox.grid(row=1, column=1)

size_label = tk.Label(text="size", fg="black", font=FONT).grid(row=0, column=0)
size_inbox = tk.Entry(width=15, font=FONT)
size_inbox.grid(row=0, column=1)

create_button = tk.Button(root, text="create", fg="red", font=FONT, command=create)
create_button.grid(row=2, column=1)

save_button = tk.Button(root, text="save", fg="red", font=FONT, command=save)
save_button.grid(row=2, column=2)

count_button = tk.Button(root, text="count", fg="red", font=FONT, command=count)
count_button.grid(row=2, column=3)

root.mainloop()
