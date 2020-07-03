#游戏属性界面
from tkinter import * #导入tk
from tkinter.messagebox import *
from gameLogin import *
import random

#游戏界面窗口
class GameGuide(object):
	global rolename
	global rivalname
	rolename = ' '
	rivalname = ' '
	def __init__(self, master = None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.gamepage()

	def gamepage(self):
		self.welcomePage = Frame(self.root, height=600, width=400)
		self.welcomePage.pack()
		Label(self.welcomePage, text='欢迎进入决斗1207大型格斗游戏！！').place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.welcomePage, text='继续', width=13, height=2, command=self.modeChoice).place(relx=0.5, rely=0.7, anchor=CENTER)



	#page1	模式选择solo和大乱斗
	def modeChoice(self):
		self.modepage = Frame(self.root, height=600, width=400)
		self.welcomePage.pack_forget()
		self.modepage.pack()
		Label(self.modepage, text='模式选择', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.modepage, text='单挑模式', width=13, height=2, command=self.modeChoiceResult1).place(relx=0.35, rely=0.7, anchor=CENTER)
		Button(self.modepage, text='生存模式', width=13, height=2, command=self.modeChoiceResult2).place(relx=0.65, rely=0.7, anchor=CENTER)

	def modeChoiceResult1(self):
		modeChoiceResult = ['单挑模式']
		self.modelevel()

	def modeChoiceResult2(self):
		modeChoiceResult = ['生存模式']
		showinfo(title='开发中', message='暂未开放，尽请期待。')


	def modelevel(self):		#难度模式选择
		self.modelevelpage = Frame(self.root, height=600, width=400)
		self.modepage.pack_forget()
		self.modelevelpage.pack()
		Label(self.modelevelpage, text='难度选择', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.modelevelpage, text='简单模式', width=13, height=2, command=self.modeLevelResult1).place(relx=0.35, rely=0.7, anchor=CENTER)
		Button(self.modelevelpage, text='极限模式', width=13, height=2, command=self.modeLevelResult2).place(relx=0.65, rely=0.7, anchor=CENTER)

	def modeLevelResult1(self):		#模式结果1
		modeLevelResult = ['简单模式']
		self.roleChoice()

	def modeLevelResult2(self):		#模式结果2
		modeLevelResult = ['极限模式']
		self.roleChoice()


	#人物选择
	def roleChoice(self):
		self.roleChoicepage = Frame(self.root, height=600, width=400)# 页面建立
		self.modelevelpage.pack_forget()
		self.roleChoicepage.pack()
		Label(self.roleChoicepage, text='我的角色', font=('微软雅黑', 16), width=10, height=5).place(relx=0.2, rely=0.25, anchor=CENTER)
		Label(self.roleChoicepage, text='对手角色', font=('微软雅黑', 16), width=10, height=5).place(relx=0.8, rely=0.25, anchor=CENTER)
		#人物列表
		roleall = ['刘厚瑚', '罗景宇', '曲泓', '任英辉', '王新喆', '王正']
		#选项设置
		self.role = Spinbox(self.roleChoicepage, value=roleall)
		self.role.place(relx=0.2, rely=0.55, width=100, anchor=CENTER)
		self.confirm = Button(self.roleChoicepage, text='确认', width=13, height=2, command=self.rolecheck)
		self.confirm.place(relx=0.2, rely=0.8, anchor=CENTER)
	

	def reroleChoice(self):
		self.roleChoicepage = Frame(self.root, height=600, width=400)# 页面建立
		self.roleChoicepage.pack()
		Label(self.roleChoicepage, text='我的角色', font=('微软雅黑', 16), width=10, height=5).place(relx=0.2, rely=0.25, anchor=CENTER)
		Label(self.roleChoicepage, text='对手角色', font=('微软雅黑', 16), width=10, height=5).place(relx=0.8, rely=0.25, anchor=CENTER)
		#人物列表
		roleall = ['刘厚瑚', '罗景宇', '曲泓', '任英辉', '王新喆', '王正']
		#选项设置
		self.role = Spinbox(self.roleChoicepage, value=roleall)
		self.role.place(relx=0.2, rely=0.55, width=100, anchor=CENTER)
		self.confirm = Button(self.roleChoicepage, text='确认', width=13, height=2, command=self.GameGuide.rolecheck)
		self.confirm.place(relx=0.2, rely=0.8, anchor=CENTER)


	def rolecheck(self):   #确认选择
		self.confirm.place_forget()
		self.role.place_forget()
		global rolename
		rolename = self.role.get()
		role = Label(self.roleChoicepage, text=rolename, font=('微软雅黑', 16), width=10, height=5)
		role.place(relx=0.2, rely=0.55, width=100, anchor=CENTER)
		self.rivalChoice()
		return rolename
		#确认完成

	def rivalChoice(self):    #对手选择
		roleall = ['刘厚瑚', '罗景宇', '曲泓', '任英辉', '王新喆', '王正']
		roleall.remove(rolename)
		self.rival = Spinbox(self.roleChoicepage, value=roleall)
		self.rival.place(relx=0.8, rely=0.55, width=100, anchor=CENTER)
		self.confirm2 = Button(self.roleChoicepage, text='确认', width=13, height=2, command=self.rivalcheck)
		self.confirm2.place(relx=0.8, rely=0.8, anchor=CENTER)

	def rivalcheck(self):   #对手确认选择
		self.confirm2.place_forget()
		self.rival.place_forget()
		global rivalname
		rivalname = self.rival.get()
		rival = Label(self.roleChoicepage, text=rivalname, font=('微软雅黑', 16), width=10, height=5)
		rival.place(relx=0.8, rely=0.55, width=100, anchor=CENTER)
		Button(self.roleChoicepage, text='下一步', width=8, height=2, command=self.sceneChoice).place(relx=0.5, rely=0.9, anchor=CENTER)
		return rivalname

	def sceneChoice(self):   #场景选择
		self.scenepage = Frame(self.root, height=600, width=400)
		self.roleChoicepage.pack_forget()
		self.scenepage.pack()
		Label(self.scenepage, text='场景地图选择', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.scenepage, text='青年湖边', width=13, height=2, command=self.scene1).place(relx=0.15, rely=0.7, anchor=CENTER)
		Button(self.scenepage, text='鹏翔宿舍', width=13, height=2, command=self.scene1).place(relx=0.5, rely=0.7, anchor=CENTER)
		Button(self.scenepage, text='设计教室', width=13, height=2, command=self.scene1).place(relx=0.85, rely=0.7, anchor=CENTER)


	def scene1(self):
		self.scenepage.destroy()
		Gamestart(self.root)




#队员
#职业，生命值，魔法值， 攻击力， 防御力， 敏捷度， 暴击率，暴击效果


#游戏过程
class Gamestart():
	def __init__(self, master):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.attribute()

	def attribute(self):
		self.liuhouhu = ['法师', 400, 300, 60, 5, 8, 0.2, 1.5]
		self.luojingyu = ['战士', 1000, 50, 25, 20, 2, 0.1, 2]
		self.quhong = ['刺客', 400, 100, 50, 8, 15, 0.15, 1.8]
		self.renyinghui = ['谋士', 200, 200, 100, 10, 30, 0.2, 1.8]
		self.wangxinzhe =['药师', 800, 300, 25, 60, 10, 0.1, 1.5]
		self.wangzheng = ['天才', 10, 10, 100000, 0, 80, 0.1, 1.5]
		self.comfirename()

	def comfirename(self):
		global HPA
		global HPB
		global attactA
		global defenseA
		global agilityA
		global attactB
		global defenseB
		global agilityB
		global boomrateA
		global boomrateB
		global boomhurtA
		global boomhurtB
		global n
		if rolename == '刘厚瑚':
			profileA =self.liuhouhu
			HPA = self.liuhouhu[1]
			attactA = self.liuhouhu[3]
			defenseA = self.liuhouhu[4]
			agilityA = self.liuhouhu[5]
			boomrateA = self.liuhouhu[6]
			boomhurtA = self.liuhouhu[7]
		if rolename == '罗景宇':
			profileA = self.luojingyu
			HPA = self.luojingyu[1]
			attactA = self.luojingyu[3]
			defenseA = self.luojingyu[4]
			agilityA = self.luojingyu[5]
			boomrateA = self.luojingyu[6]
			boomhurtA = self.luojingyu[7]
		if rolename == '曲泓':
			profileA = self.quhong
			HPA = self.quhong[1]
			attactA = self.quhong[3]
			defenseA = self.quhong[4]
			agilityA = self.quhong[5]
			boomrateA = self.quhong[6]
			boomhurtA = self.quhong[7]
		if rolename == '任英辉':
			profileA = slef.renyinghui
			HPA = slef.renyinghui[1]
			attactA = slef.renyinghui[3]
			defenseA = slef.renyinghui[4]
			agilityA = slef.renyinghui[5]
			boomrateA = slef.renyinghui[6]
			boomhurtA = slef.renyinghui[7]
		if rolename == '王新喆':
			profileA = self.wangxinzhe
			HPA = self.wangxinzhe[1]
			attactA = self.wangxinzhe[3]
			defenseA = self.wangxinzhe[4]
			agilityA = self.wangxinzhe[5]
			boomrateA = self.wangxinzhe[6]
			boomhurtA = self.wangxinzhe[7]
		if rolename == '王正':
			profileA = self.wangzheng
			HPA = self.wangzheng[1]
			attactA = self.wangzheng[3]
			defenseA = self.wangzheng[4]
			agilityA = self.wangzheng[5]
			boomrateA = self.wangzheng[6]
			boomhurtA = self.wangzheng[7]

		if rivalname == '刘厚瑚':
			profileB = self.liuhouhu
			HPB = self.liuhouhu[1]
			attactB = self.liuhouhu[3]
			defenseB = self.liuhouhu[4]
			agilityB = self.liuhouhu[5]
			boomrateB = self.liuhouhu[6]
			boomhurtB = self.liuhouhu[7]
		elif rivalname == '罗景宇':
			profileB = self.luojingyu
			HPB = self.luojingyu[1]
			attactB = self.luojingyu[3]
			defenseB = self.luojingyu[4]
			agilityB = self.luojingyu[5]
			boomrateB = self.luojingyu[6]
			boomhurtB = self.luojingyu[7]
		if rivalname == '曲泓':
			profileB = self.quhong
			HPB = self.quhong[1]
			attactB = self.quhong[3]
			defenseB = self.quhong[4]
			agilityB = self.quhong[5]
			boomrateB = self.quhong[6]
			boomhurtB = self.quhong[7]
		elif rivalname == '任英辉':
			profileB = self.renyinghui
			HPB = self.renyinghui[1]
			attactB = self.renyinghui[3]
			defenseB = self.renyinghui[4]
			agilityB = self.renyinghui[5]
			boomrateB = self.renyinghui[6]
			boomhurtB = self.renyinghui[7]
		if rivalname == '王新喆':
			profileB = self.wangxinzhe
			HPB = self.wangxinzhe[1]
			attactB = self.wangxinzhe[3]
			defenseB = self.wangxinzhe[4]
			agilityB = self.wangxinzhe[5]
			boomrateB = self.wangxinzhe[6]
			boomhurtB = self.wangxinzhe[7]
		elif rivalname == '王正':
			profileB = self.wangzheng
			HPB = self.wangzheng[1]
			attactB = self.wangzheng[3]
			defenseB = self.wangzheng[4]
			agilityB = self.wangzheng[5]
			boomrateB = self.wangzheng[6]
			boomhurtB = self.wangzheng[7]
		self.interface()


	def interface(self):
		self.facepage = Frame(self.root, height=600, width=400)
		self.facepage.pack()
		self.me = Label(self.facepage, text=rolename, font=('微软雅黑', 14), width=13, height=5)
		self.me.place(relx=0.1, rely=0.5, anchor=CENTER)
		self.rival = Label(self.facepage, text=rivalname, font=('微软雅黑', 14), width=13, height=5)
		self.rival.place(relx=0.9, rely=0.5, anchor=CENTER)
		Button(self.facepage, text='开始', width=13, height=2, command=self.beginning).place(relx=0.5, rely=0.8, anchor=CENTER)


	def beginning(self):
		print('%s 的生命值:  %s   ' % (rolename, HPA))
		print('%s 的生命值:  %s   ' % (rivalname, HPB))
		global n
		if agilityA > agilityB:
			n = 1
		else:
			n = 0
		if agilityA > agilityB:
			print('%s 首先发动攻击！' % rolename)
			self.roleattack()
		else:
			print('%s 首先发动攻击！' % rivalname)
			self.rivalattack()
		self.program()

	def program(self):
		while HPB > 0 and HPA > 0:
			global n
			if HPA > 0 and n % 2 == 1:
				self.roleattack()
				if HPB < 0:
					print('恭喜您，胜利。 您剩余生命值：  %s ' % (HPA))  
			if HPB > 0 and n % 2 == 0:
				self.rivalattack()
				if HPA < 0:
					print('很遗憾，失败。 %s 生命值剩余： %s  ' % (rivalname, HPB))
		else:
			#结束游戏重新开始
			print('restart')
			Button(self.facepage, text='重新开始', width=13, height=2, command=self.restart).place(relx=0.5, rely=0.9, anchor=CENTER)
			Button(self.facepage, text='选择角色', width=13, height=2, command=self.reselect).place(relx=0.2, rely=0.9, anchor=CENTER)
			

	def roleattack(self):
		#A先攻击,攻击成功
		global n
		n += 1
		temp = random.randint(0,100)
		global HPB
		if temp in range(0, agilityB):
			print('%s   攻击   %s   , MISS！！！造成伤害    0    ' % (rolename, rivalname))
			return HPB
		else:
			#计算伤害效果
			temp2 = random.uniform(0,1)
			if temp2 < boomrateA:
				hurtoB = attactA * boomhurtA - defenseB * float(random.uniform(0,1))
				HPB -= hurtoB
				print('%s   打出暴击！！！！！！！！！！！！！！！！！！！！！！，造成伤害   %.2f   ,    %s    剩余生命值：  %.2f   ' % (rolename, hurtoB, rivalname, HPB))
			else:
				hurtoB = attactA - defenseB * float(random.uniform(0,1))
				#B受伤害
				HPB -= hurtoB
				print('%s   攻击   %s   , 击中！！！造成伤害   %.2f   ,    %s    剩余生命值：  %.2f   ' % (rolename, rivalname, hurtoB, rivalname, HPB))
			return HPB	
		

	def rivalattack(self):
		#B攻击
		global n
		n += 1
		temp = random.randint(0,100)
		global HPA
		if temp in range(0, agilityA):
			print('%s   攻击   %s   , MISS！！！造成伤害    0    ' % (rivalname, rolename))
			return HPA
		else:
			#计算伤害效果
			temp2 = random.uniform(0,1)
			if temp2 < boomrateB:
				hurtoA = attactB * boomhurtB - defenseA * float(random.uniform(0,1))
				HPA -= hurtoA
				print('%s   打出暴击！！！！！！！！！！！！！！！！！！！！！！，造成伤害   %.2f   ,    %s    剩余生命值：  %.2f   ' % (rivalname, hurtoA, rolename, HPA))
			else:
			    hurtoA = attactB - defenseA * float(random.uniform(0, 1))
			    #B受伤害
			    HPA -= hurtoA

			    print('%s   攻击   %s   , 击中！！！造成伤害   %.2f   ,    %s    剩余生命值：  %.2f   ' % (rivalname, rolename, hurtoA, rolename, HPA))
			return HPA

	def restart(self):
		self.comfirename()
		self.beginning()

	def reselect(self):
		self.facepage.pack_forget()
		GameGuide.reroleChoice(self)









