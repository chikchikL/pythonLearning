# Tkinter编写一个Gui版本的hello，world
from tkinter import *
import tkinter.messagebox as msgbox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        # pack函数将widget存入父容器
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or '什么'
        # 提示框
        msgbox.showinfo('信息', 'hello, %s' % name)


app = Application()
app.master.title('窗口标题')
app.mainloop()
