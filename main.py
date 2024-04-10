# How to close the Window in Tkinter

from tkinter import Tk, ttk

root = Tk()

frm = ttk.Frame(root, padding=10)

frm.grid()

ttk.Label(frm, text="bobbyhadz.com").grid(column=0, row=0)

# 👇️ Close tkinter window when the button is clicked
ttk.Button(frm, text="Close Window",
           command=root.destroy).grid(column=1, row=0)

root.mainloop()