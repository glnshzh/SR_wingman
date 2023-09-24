import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="minty")
root.title("fjk,htc的科研工具")
root.geometry('800x1080')
style = ttk.Style()
style.configure("TButton", padding=6)
b1 = ttk.Button(root, text="chatgpt",bootstyle=(SUCCESS, OUTLINE),width=70)
b1.pack(side=TOP, padx=20, pady=40)


root.mainloop()
