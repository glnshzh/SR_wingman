import threading

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.dialogs as dia
from gpt import gpt
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
        b1 = ttk.Button(self.frame1, text="chatgpt", bootstyle=(SUCCESS, OUTLINE), width=70,command=self.start_frame2_close_1)
        b1.pack(side=TOP, padx=20, pady=40)
        self.root.mainloop()

    def start_frame1_close_2(self):
        self.frame2.pack_forget()
        self.frame1.pack()
    def start_frame2_close_1(self):
        self.frame1.pack_forget()
        self.frame2.pack()


    def frame2_create(self):
        self.frame2 = ttk.Frame(self.root)
        self.ask_label=ttk.Label(self.frame2, text="请输入想要的问题",font=( 'Arial', 15)).grid(row=0,column=0,columnspan=2)
        self.ask_text=ttk.Text(self.frame2,height=8)
        self.ask_text.grid(row=1,column=0,columnspan=2)
        self.label1=ttk.Label(self.frame2, text="gpt生成答案",font=( 'Arial', 15))
        self.label1.grid(row=2,column=0,columnspan=2)
        self.gpt_content=ttk.Text(self.frame2, height=16)
        self.gpt_content.grid(row=3, column=0, columnspan=2)
        try:
            self.gpt_button1=ttk.Button(self.frame2,text="生成答案",command=self.start)
            self.gpt_button1.grid(row=4,column=0)
        except Exception as e:
            print(e)
            dia.Messagebox.show_error(title="提示", message="出现错误，请重新尝试", alert=False)
        finally:
            self.gpt_button1=ttk.Button(self.frame2,text="生成答案",command=self.start)
            self.gpt_button1.grid(row=4,column=0)
        self.gpt_button2= ttk.Button(self.frame2, text="返回",command=self.start_frame1_close_2).grid(row=4,column=1)
    def get_gpt(self):
        self.label1.configure(text="答案正在生成,请耐心等待")
        message = gpt.getChat(self.ask_text.get("1.0", "end"), api_key=gpt.get_api_key(), role="user")
        self.label1.configure(text="答案如下")
        self.gpt_content.insert(INSERT, message)
    def start(self):
        self.T = threading.Thread(target=self.get_gpt)  # 多线程
        self.T.Daemo=True # 线程守护，即主进程结束后，此线程也结束。否则主进程结束子进程不结束
        self.T.start()


if __name__ == '__main__':
    ttk=Framework()



