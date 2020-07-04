from tkinter import *
from gameLogin import *

#创建  
root = Tk()
root.title('决战1207')
root.geometry ('600x400')
root.resizable(width=False, height=False)
#登录模块
gameLogin(root) 


root.mainloop()