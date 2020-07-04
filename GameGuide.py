#游戏属性界面
from tkinter import * #导入tk
from tkinter.messagebox import *
from gameLogin import *
import random

#游戏界面窗口
class GameGuide(object):
	rolename = 'wangenius'
	rivalname = ''
	#初始化窗口
	def __init__(self, master = None):
		self.root = master
		self.root.geometry('%dx%d' % (600, 400))
		self.firstact()


	def firstact(self):
		self.gamepage()
		self.modeChoice()
		self.roleChoice()
		self.modelevel()
		self.sceneChoice()


    #欢迎界面
	def gamepage(self):
		self.welcomePage = Frame(self.root, height=400, width=600)
		self.welcomePage.pack()
		Label(self.welcomePage, text='决斗 1207', font=('黑体', 28), width=400, height=1).place(relx=0.5, rely=0.4, anchor=CENTER)
		Label(self.welcomePage, text='2020 巨 制 格 斗 端 游', font=('微软雅黑', 12), width=400, height=1).place(relx=0.5, rely=0.5, anchor=CENTER)
		Button(self.welcomePage, text='继续', width=13, height=2, command=self.preparemode).place(relx=0.85, rely=0.9, anchor=CENTER)

	def preparemode(self):
		self.welcomePage.pack_forget()

	

	#模式选择solo和大乱斗
	def modeChoice(self):
		self.modepage = Frame(self.root, height=600, width=400)
		self.modepage.pack()
		Label(self.modepage, text='模式选择', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.modepage, text='单挑模式', width=14, height=2, command=self.modeChoiceResult1).place(relx=0.36, rely=0.7, anchor=CENTER)
		Button(self.modepage, text='生存模式', width=14, height=2, command=self.modeChoiceResult2).place(relx=0.64, rely=0.7, anchor=CENTER)
		Button(self.modepage, text='模式简介', width=30, height=2, command=self.modeChoiceResult3).place(relx=0.5, rely=0.805, anchor=CENTER)

	#solo模式
	def modeChoiceResult1(self):
		modeChoiceResult = ['单挑模式']
		self.modepage.pack_forget()

	#生存模式
	def modeChoiceResult2(self):
		modeChoiceResult = ['生存模式']
		showinfo(title='开发中', message='暂未开放，尽请期待。')

	def modeChoiceResult3(self):
		modeChoiceResult = ['jianjie']
		showinfo(title='模式简介', message='懂得都懂，没必要说')

	



	#人物选择
	def roleChoice(self):
		self.roleChoicepage = Frame(self.root, height=600, width=400)# 页面建立
		self.roleChoicepage.pack()
		Label(self.roleChoicepage, text='我的角色', font=('微软雅黑', 16), width=10, height=5).place(relx=0.2, rely=0.25, anchor=CENTER)
		Label(self.roleChoicepage, text='对手角色', font=('微软雅黑', 16), width=10, height=5).place(relx=0.8, rely=0.25, anchor=CENTER)
		#人物列表
		roleall = ['刘厚瑚', '罗景宇', '曲泓', '任英辉', '王新喆', '王正']
		#选项设置
		self.role = Spinbox(self.roleChoicepage, value=roleall, font=('微软雅黑', 16), width=4)
		self.role.place(relx=0.2, rely=0.55, width=100, anchor=CENTER)
		self.confirm = Button(self.roleChoicepage, text='确认', width=13, height=2, command=self.rolecheck)
		self.confirm.place(relx=0.2, rely=0.8, anchor=CENTER)
		self.heromenu = Button(self.roleChoicepage, text = '英雄简介', width=13, height=2, command=self.heromenuwin)
		self.heromenu.place(relx=0.5, rely=0.8, anchor=CENTER)

	def heromenuwin(self):
		showinfo(title='英雄简介', message='刘厚瑚：\n\n职业:法师\n生命值=400\n法力值=300\n攻击力=60\n防御力=5\n敏捷度=8\n暴击率=0.2\n暴击效果=1.5\n专属技能:辣味入侵\n技能特效：未开发\n\n罗景宇：\n\n职业:战士\n生命值=1000\n法力值=50\n攻击力=25\n防御力=20\n敏捷度=2\n暴击率=0.1\n暴击效果=2\n专属技能:进化球人\n技能特效：未开发\n\n曲泓：\n\n职业:刺客\n生命值=400\n法力值=100\n攻击力=50\n防御力=8\n敏捷度=15\n暴击率=0.15\n暴击效果=1.8\n专属技能:拔你网线\n技能特效：未开发\n\n任英辉：\n\n职业:谋士\n生命值=200\n法力值=200\n攻击力=100\n防御力=10\n敏捷度=30\n暴击率=0.2\n暴击效果=1.8\n专属技能:分数炸弹\n技能特效：未开发\n\n王新喆：\n\n职业:药师\n生命值=800\n法力值=300\n攻击力=250\n防御力=15\n敏捷度=10\n暴击率=0.1\n暴击效果=1.5\n专属技能:番剧治愈\n技能特效：未开发\n\n王正\n\n职业:天才\n生命值=10\n法力值=0\n攻击力=100000\n防御力=0\n敏捷度=50\n暴击率=0.1\n暴击效果=1.5\n专属技能:无')		
	
    #人物rolename确认
	def rolecheck(self):   #确认选择
		self.confirm.place_forget()
		self.role.place_forget()
		global rolename
		rolename = self.role.get()
		role = Label(self.roleChoicepage, text=rolename, font=('微软雅黑', 16), width=4)
		role.place(relx=0.2, rely=0.55, width=100, anchor=CENTER)
		self.rivalChoice()
		
		#确认完成

    #对手选择
	def rivalChoice(self):    #对手选择
		roleall = ['刘厚瑚', '罗景宇', '曲泓', '任英辉', '王新喆', '王正']
		roleall.remove(rolename)
		self.rival = Spinbox(self.roleChoicepage, value=roleall, font=('微软雅黑', 16))
		self.rival.place(relx=0.8, rely=0.55, width=100, anchor=CENTER)
		self.confirm2 = Button(self.roleChoicepage, text='确认', width=13, height=2, command=self.rivalcheck)
		self.confirm2.place(relx=0.8, rely=0.8, anchor=CENTER)

    #对手rivalname确认
	def rivalcheck(self):   #对手确认选择
		self.confirm2.place_forget()
		self.rival.place_forget()
		global rivalname
		rivalname = self.rival.get()
		rival = Label(self.roleChoicepage, text=rivalname, font=('微软雅黑', 16), width=10, height=5)
		rival.place(relx=0.8, rely=0.55, width=100, anchor=CENTER)
		self.heromenu.place_forget()
		Button(self.roleChoicepage, text='下一步', width=13, height=2, command=self.packname).place(relx=0.5, rely=0.8, anchor=CENTER)

	def packname(self):
		self.roleChoicepage.pack_forget()

    


    #难度选择
	def modelevel(self):
		self.modelevelpage = Frame(self.root, height=600, width=400)
		self.modelevelpage.pack()
		Label(self.modelevelpage, text='难度选择', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.modelevelpage, text='简单模式', width=13, height=2, command=self.modeLevelResult1).place(relx=0.35, rely=0.7, anchor=CENTER)
		Button(self.modelevelpage, text='极限模式', width=13, height=2, command=self.modeLevelResult2).place(relx=0.65, rely=0.7, anchor=CENTER)

	#简单模式
	def modeLevelResult1(self):
		self.modelevelpage.pack_forget()

	#极限模式
	def modeLevelResult2(self):
		modeLevelResult = ['极限模式']
		showinfo(title='开发中', message='暂未开放，尽请期待。')



    #场景选择
	def sceneChoice(self):   #场景选择
		self.scenepage = Frame(self.root, height=600, width=400)
		self.scenepage.pack()
		Label(self.scenepage, text='场景地图选择', font=('微软雅黑', 24), width=300, height=1).place(relx=0.5, rely=0.3, anchor=CENTER)
		Label(self.scenepage, text='   不同地图有不同地形特征、武器装备、协助人员，急救补药\n以及神秘机关副本等等，可能会影响比赛结果。', font=('微软雅黑', 8), width=400, height=2).place(relx=0.5, rely=0.4, anchor=N)
		Button(self.scenepage, text='青年湖边', width=13, height=2, command=self.scene1).place(relx=0.15, rely=0.7, anchor=CENTER)
		Button(self.scenepage, text='鹏翔宿舍', width=13, height=2, command=self.scene2).place(relx=0.5, rely=0.7, anchor=CENTER)
		Button(self.scenepage, text='设计教室', width=13, height=2, command=self.scene2).place(relx=0.85, rely=0.7, anchor=CENTER)

    #场景1选择确认
	def scene1(self):
		self.scenepage.pack_forget()
		self.attribute()
		
	def scene2(self):
		showinfo(title='开发中', message='暂未开放，尽请期待。')


	def resceneChoice(self):   #场景选择
		self.scenepage = Frame(self.root, height=600, width=400)
		self.scenepage.pack()
		Label(self.scenepage, text='场景地图选择', font=('微软雅黑', 24), width=300, height=5).place(relx=0.5, rely=0.3, anchor=CENTER)
		Button(self.scenepage, text='青年湖边', width=13, height=2, command=self.rescene1).place(relx=0.15, rely=0.7, anchor=CENTER)
		Button(self.scenepage, text='鹏翔宿舍', width=13, height=2, command=self.rescene2).place(relx=0.5, rely=0.7, anchor=CENTER)
		Button(self.scenepage, text='设计教室', width=13, height=2, command=self.rescene2).place(relx=0.85, rely=0.7, anchor=CENTER)

    #场景1选择确认
	def rescene1(self):
		self.scenepage.pack_forget()
		
	def rescene2(self):
		showinfo(title='开发中', message='暂未开放，尽请期待。')

    



    #游戏过程
    #职业，生命值，魔法值， 攻击力， 防御力， 敏捷度， 暴击率，暴击效果
	def attribute(self): 
		self.liuhouhu = ['法师', 400, 300, 60, 5, 8, 0.2, 1.5]
		self.luojingyu = ['战士', 1000, 50, 25, 20, 2, 0.1, 2]
		self.quhong = ['刺客', 400, 100, 50, 8, 15, 0.15, 1.8]
		self.renyinghui = ['谋士', 200, 200, 100, 10, 30, 0.2, 1.8]
		self.wangxinzhe =['药师', 800, 300, 25, 60, 10, 0.1, 1.5]
		self.wangzheng = ['天才', 10, 10, 100000, 0, 80, 0.1, 1.5]
		self.comfirename()

    #确定双方英雄
	def comfirename(self):
		global profileA
		global HPA
		global attactA
		global defenseA
		global agilityA
		global boomrateA
		global boomhurtA
		global profileB
		global HPB
		global attactB
		global defenseB
		global agilityB
		global boomrateB
		global boomhurtB
		global positionA
		global positionB
		if rolename == '刘厚瑚':
			positionA = self.liuhouhu[0]
			profileA =self.liuhouhu
			HPA = self.liuhouhu[1]
			attactA = self.liuhouhu[3]
			defenseA = self.liuhouhu[4]
			agilityA = self.liuhouhu[5]
			boomrateA = self.liuhouhu[6]
			boomhurtA = self.liuhouhu[7]
		if rolename == '罗景宇':
			positionA = self.luojingyu[0]
			profileA = self.luojingyu
			HPA = self.luojingyu[1]
			attactA = self.luojingyu[3]
			defenseA = self.luojingyu[4]
			agilityA = self.luojingyu[5]
			boomrateA = self.luojingyu[6]
			boomhurtA = self.luojingyu[7]
		if rolename == '曲泓':
			positionA = self.quhong[0]
			profileA = self.quhong
			HPA = self.quhong[1]
			attactA = self.quhong[3]
			defenseA = self.quhong[4]
			agilityA = self.quhong[5]
			boomrateA = self.quhong[6]
			boomhurtA = self.quhong[7]
		if rolename == '任英辉':
			positionA = self.renyinghui[0]
			profileA = slef.renyinghui
			HPA = slef.renyinghui[1]
			attactA = slef.renyinghui[3]
			defenseA = slef.renyinghui[4]
			agilityA = slef.renyinghui[5]
			boomrateA = slef.renyinghui[6]
			boomhurtA = slef.renyinghui[7]
		if rolename == '王新喆':
			positionA = self.wangxinzhe[0]
			profileA = self.wangxinzhe
			HPA = self.wangxinzhe[1]
			attactA = self.wangxinzhe[3]
			defenseA = self.wangxinzhe[4]
			agilityA = self.wangxinzhe[5]
			boomrateA = self.wangxinzhe[6]
			boomhurtA = self.wangxinzhe[7]
		if rolename == '王正':
			positionA = self.wangzheng[0]
			profileA = self.wangzheng
			HPA = self.wangzheng[1]
			attactA = self.wangzheng[3]
			defenseA = self.wangzheng[4]
			agilityA = self.wangzheng[5]
			boomrateA = self.wangzheng[6]
			boomhurtA = self.wangzheng[7]

		if rivalname == '刘厚瑚':
			positionB = self.liuhouhu[0]
			profileB = self.liuhouhu
			HPB = self.liuhouhu[1]
			attactB = self.liuhouhu[3]
			defenseB = self.liuhouhu[4]
			agilityB = self.liuhouhu[5]
			boomrateB = self.liuhouhu[6]
			boomhurtB = self.liuhouhu[7]
		elif rivalname == '罗景宇':
			positionB = self.luojingyu[0]
			profileB = self.luojingyu
			HPB = self.luojingyu[1]
			attactB = self.luojingyu[3]
			defenseB = self.luojingyu[4]
			agilityB = self.luojingyu[5]
			boomrateB = self.luojingyu[6]
			boomhurtB = self.luojingyu[7]
		if rivalname == '曲泓':
			positionB = self.quhong[0]
			profileB = self.quhong
			HPB = self.quhong[1]
			attactB = self.quhong[3]
			defenseB = self.quhong[4]
			agilityB = self.quhong[5]
			boomrateB = self.quhong[6]
			boomhurtB = self.quhong[7]
		elif rivalname == '任英辉':
			positionB = self.renyinghui[0]
			profileB = self.renyinghui
			HPB = self.renyinghui[1]
			attactB = self.renyinghui[3]
			defenseB = self.renyinghui[4]
			agilityB = self.renyinghui[5]
			boomrateB = self.renyinghui[6]
			boomhurtB = self.renyinghui[7]
		if rivalname == '王新喆':
			positionB = self.wangxinzhe[0]
			profileB = self.wangxinzhe
			HPB = self.wangxinzhe[1]
			attactB = self.wangxinzhe[3]
			defenseB = self.wangxinzhe[4]
			agilityB = self.wangxinzhe[5]
			boomrateB = self.wangxinzhe[6]
			boomhurtB = self.wangxinzhe[7]
		elif rivalname == '王正':
			positionB = self.wangzheng[0]
			profileB = self.wangzheng
			HPB = self.wangzheng[1]
			attactB = self.wangzheng[3]
			defenseB = self.wangzheng[4]
			agilityB = self.wangzheng[5]
			boomrateB = self.wangzheng[6]
			boomhurtB = self.wangzheng[7]
		self.interface()

	def recomfirename(self):
		global profileA
		global HPA
		global attactA
		global defenseA
		global agilityA
		global boomrateA
		global boomhurtA
		global profileB
		global HPB
		global attactB
		global defenseB
		global agilityB
		global boomrateB
		global boomhurtB
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
			profileA = self.renyinghui
			HPA = self.renyinghui[1]
			attactA = self.renyinghui[3]
			defenseA = self.renyinghui[4]
			agilityA = self.renyinghui[5]
			boomrateA = self.renyinghui[6]
			boomhurtA = self.renyinghui[7]
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
		
    #主打斗场景
	def interface(self):
		self.facepage = Frame(self.root, height=400, width=600)
		self.facepage.pack()
		self.buStart = Button(self.facepage, text='开始决斗', font=('微软雅黑', 14), width=20, height=10, command=self.beginning)
		self.buStart.place(relx=0.5, rely=0.5, anchor=CENTER)


    #决斗开始
	def beginning(self):
		self.buStart.place_forget()
		Label(self.facepage, text='我方英雄', font=('微软雅黑', 14), width=13, height=5).place(relx=0.1, rely=0.2, anchor=CENTER)
		Label(self.facepage, text='对方英雄', font=('微软雅黑', 14), width=13, height=5).place(relx=0.9, rely=0.2, anchor=CENTER)
		self.me = Label(self.facepage, text=rolename, font=('微软雅黑', 14), width=13, height=2)
		self.me.place(relx=0.1, rely=0.35, anchor=CENTER)
		self.rival = Label(self.facepage, text=rivalname, font=('微软雅黑', 14), width=13, height=2)
		self.rival.place(relx=0.9, rely=0.35, anchor=CENTER)
		self.roleattribute = Label(self.facepage, text=('职业 : %s\n总生命值 : %s\n攻击力 : %s\n防御力 : %s\n敏捷度 : %s\n暴击率 : %s\n暴击效果 : %s倍' % (positionA, HPA, attactA, defenseA, agilityA, boomrateA, boomhurtA)))
		self.rivalattribute = Label(self.facepage, text=('职业 : %s\n总生命值 : %s\n攻击力 : %s\n防御力 : %s\n敏捷度 : %s\n暴击率 : %s\n暴击效果 : %s倍' % (positionB, HPB, attactB, defenseB, agilityB, boomrateB, boomhurtB)))	
		self.roleattribute.place(relx=0.1, rely=0.55, anchor=CENTER)
		self.rivalattribute.place(relx=0.9, rely=0.55, anchor=CENTER)	
		self.text = Text(self.facepage, width=50, height=24)
		self.text.place(relx=0.5, rely=0.45, anchor=CENTER)
		self.text.insert(INSERT, ('%s 的生命值:  %s   \n' % (rolename, HPA)))
		self.text.insert(INSERT, ('%s 的生命值:  %s   \n' % (rivalname, HPB)))
		global n
		if agilityA > agilityB:
			n = 1
		else:
			n = 0
		if agilityA > agilityB:
			self.text.insert(INSERT,('%s 首先发动攻击！\n' % rolename))
			self.roleattack()
		else:
			self.text.insert(INSERT,('%s 首先发动攻击！\n' % rivalname))
			self.rivalattack()
		self.program()
		
    #决斗过程
	def program(self):
		while HPB > 0 and HPA > 0:
			self.text.update()
			global n
			if HPA > 0 and n % 2 == 1:
				self.roleattack()
				if HPB < 0:
					self.text.insert(INSERT,('恭喜您，胜利。 \n您剩余生命值：  %s \n' % (HPA)))  
			if HPB > 0 and n % 2 == 0:
				self.rivalattack()
				if HPA < 0:
					self.text.insert(INSERT,('很遗憾，失败。\n %s 生命值剩余： %s  \n' % (rivalname, HPB)))
			self.text.see(END)
			self.text.update()
		else:
			#结束游戏重新开始
			print('结束')
		self.destination()
			
    #修改方向
	def destination(self):
			self.restartbutton = Button(self.facepage, text='重新决斗', width=12, height=2, command=self.restart)
			self.restartbutton.place(relx=0.14, rely=0.9, anchor=CENTER)
			self.rerolechoose = Button(self.facepage, text='选择角色', width=12, height=2, command=self.reselect)
			self.rerolechoose.place(relx=0.5, rely=0.9, anchor=CENTER)
			self.resightchoose = Button(self.facepage, text='选择场景', width=12, height=2, command=self.resight)
			self.resightchoose.place(relx=0.86, rely=0.9, anchor=CENTER)
			self.remodechoose = Button(self.facepage, text='选择模式', width=12, height=2, command=self.remode)
			self.remodechoose.place(relx=0.32, rely=0.9, anchor=CENTER)
			self.relevelchoose = Button(self.facepage, text='选择难度', width=12, height=2, command=self.remodelevel)
			self.relevelchoose.place(relx=0.68, rely=0.9, anchor=CENTER)				

    #己方攻击时间
	def roleattack(self):
		#A先攻击,攻击成功
		global n
		n += 1
		temp = random.randint(0,100)
		global HPB
		if temp in range(0, agilityB):
			self.text.insert(INSERT,('%s   攻击   %s   ,   MISS！！！\n' % (rolename, rivalname)))
			return HPB
		else:
			#计算伤害效果
			temp2 = random.uniform(0,1)
			if temp2 < boomrateA:
				hurtoB = attactA * boomhurtA - defenseB * float(random.uniform(0,1))
				HPB -= hurtoB
				self.text.insert(INSERT,('%s   打出暴击！！！！！！！！\n造成伤害   %.2f   ,   %s   剩余生命值：   %.2f   \n' % (rolename, hurtoB, rivalname, HPB)))
			else:
				hurtoB = attactA - defenseB * float(random.uniform(0,1))
				#B受伤害
				HPB -= hurtoB
				self.text.insert(INSERT,('%s   攻击   %s   ,   击中！！！\n造成伤害   %.2f   ,    %s    剩余生命值：  %.2f   \n' % (rolename, rivalname, hurtoB, rivalname, HPB)))	
	
    #对方攻击时间
	def rivalattack(self):
		#B攻击
		global n
		n += 1
		temp = random.randint(0,100)
		global HPA
		if temp in range(0, agilityA):
			self.text.insert(INSERT,('%s   攻击   %s   ,   MISS！！！\n' % (rivalname, rolename)))
			return HPA
		else:
			#计算伤害效果
			temp2 = random.uniform(0,1)
			if temp2 < boomrateB:
				hurtoA = attactB * boomhurtB - defenseA * float(random.uniform(0,1))
				HPA -= hurtoA
				self.text.insert(INSERT,('%s   打出暴击！！！！！！！！\n造成伤害   %.2f   ,   %s   剩余生命值：   %.2f   \n' % (rivalname, hurtoA, rolename, HPA)))
			else:
			    hurtoA = attactB - defenseA * float(random.uniform(0, 1))
			    #B受伤害
			    HPA -= hurtoA
			    self.text.insert(INSERT,('%s   攻击   %s   \n击中！！！造成伤害   %.2f   ,   %s   剩余生命值：   %.2f   \n' % (rivalname, rolename, hurtoA, rolename, HPA)))

    #重新开始决斗
	def restart(self):
		self.recomfirename()
		self.text.delete(0.0, END)
		self.text.update()
		self.beginning()
		self.destination()

    #重新开始选择人物
	def reselect(self):
		self.facepage.destroy()
		self.roleChoice()
		self.recomfirename()
		self.interface()


	def resight(self):
		self.facepage.destroy()
		self.resceneChoice()
		self.recomfirename()
		self.interface()

	def remode(self):
		self.facepage.destroy()
		self.modeChoice()
		self.recomfirename()
		self.interface()

	def remodelevel(self):
		self.facepage.destroy()
		self.modelevel()
		self.recomfirename()
		self.interface()














