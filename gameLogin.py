from tkinter import * #导入tk
from tkinter.messagebox import *
from GameGuide import *

class gameLogin():
	def __init__(self, master):
		self.root = master #定义内部变量root
		self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小 
		self.createPage()

	def createPage(self):
		self.page = Frame(self.root, height=600, width=400)
		self.page.pack()
		Label(self.page, text='决战1207', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.25, anchor=CENTER)
		Label(self.page, text='账户', font=('微软雅黑', 8)).place(relx=0.18, rely=0.48, anchor=N)
		Label(self.page, text='密码', font=('微软雅黑', 8)).place(relx=0.18, rely=0.58, anchor=N)
		self.username = Entry(self.page, show=None, font=(('微软雅黑', 14)))
		self.password = Entry(self.page, show='*', font=(('微软雅黑', 14)))
		self.username.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.password.place(relx=0.5, rely=0.6, anchor=CENTER)
		Button(self.page, text='登录', width=13, height=2, command=self.signIncheck).place(relx=0.36, rely=0.7, anchor=CENTER)
		Button(self.page, text='忘记密码', width=13, height=2, command=self.infotip1).place(relx=0.64, rely=0.7, anchor=CENTER)

	def signIncheck(self):
		#用户输入
		dict1207 = [['liuhouhu', 'liuhouhu1'], ['luojingyu', 'luojingyu2'], ['quhong', 'quhong3'], ['renyinghui', 'renyinghui4'], ['wangxinzhe', 'wangxinzhe5'], ['wangzheng', 'wangzheng6']]
		name = self.username.get()
		passpord = self.password.get()
		nameAndPass = [name, passpord]
		if nameAndPass in dict1207:
			#进入游戏界面
			self.page.pack_forget()
			GameGuide(self.root)
		else: #提示密码错误
			showwarning(title='Hi', message='用户名或密码错误！')



	def infotip1(self):
		self.infotiproot = Toplevel()
		self.infotiproot.geometry('300x200')
		self.infotiproot.title('tips')
		self.infotiproot.resizable(width=False, height=False)
		self.infotiproot.attributes("-toolwindow", True)
		self.infotiproot.attributes("-topmost", True)
		self.infotip = Frame(self.infotiproot, height=300, width=200)
		self.infotip.pack()
		Label(self.infotip, text='提示', font=('微软雅黑', 18), width=300, height=1).place(relx=0.5, rely=0.3, anchor=CENTER)
		Label(self.infotip, text='用户名为姓名拼音\n密码为用户名加床号', font=('微软雅黑', 12), width=400, height=2).place(relx=0.5, rely=0.55, anchor=CENTER)
		Button(self.infotip, text='确认', width=13, height=2, command=self.tipshutdown1).place(relx=0.5, rely=0.85, anchor=CENTER)


		self.infotiproot.mainloop()

	def tipshutdown1(self):
		self.infotiproot.withdraw()





	def signtip(self):
		showinfo(title='Hi', message='用户名为姓名拼音，密码为用户名加床号。')
