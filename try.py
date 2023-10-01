import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Framework:
    def __init__(self):
        self.root = ttk.Window(themename="minty")
        self.root.title("科研工具")
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        ww = 800
        wh = 800
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        sw =self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        ww = 800
        wh = 800
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack()
        self.frame2_create()
        b1 = ttk.Button(self.frame1, text="chatgpt", bootstyle=(SUCCESS, OUTLINE), width=70,command=self.start_frame)
        b1.pack(side=TOP, padx=20, pady=40)
        self.root.mainloop()

    def start_frame(self):
        self.frame1.pack_forget()
        self.frame2.pack()
    def frame2_create(self):
        self.frame2 = ttk.Frame(self.root)
        ttk.Label(self.frame2, text="尝试").pack()


if __name__ == '__main__':
    ttk=Framework()