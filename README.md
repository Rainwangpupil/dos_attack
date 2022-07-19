# Dos attack

<p align="center"><img src="https://img.shields.io/pypi/pyversions/Django.svg" ></img></p>

<p align="center">可以用来DOS攻击</p>

## 简单介绍

<p align="center"><b>本项目仅供渗透学习所用，请适当使用</b></p>

本项目可以进行DOS攻击，有一定的威力

## 安装教程

接下来为大家讲解安装方法

### Linux

```

$ sudo apt install git

......

$ sudo git clone https://github.com/rainwangpupil/dos_attack

......

$ dir

.....

$ cd dos_attack

$ sudo apt install python

$ cd dos_attack

.....

```

### Windows

```

C:\Users\Rainwang>E: #建议不要在C盘安装

D:\>git clone https://github.com/rainwangpupil/dos_attack #如果没有安装git，请去官网安装

......

D:\>cd dos_attack

```

### Termux

```

~$ pkg install git

......

~$ pkg install python

......

~$ git clone https://github.com/rainwangpupil/dos_attack

......

~$ cd dos_atack

~/dos_attack$ 

```

## 运行

只需要cd到程序目录然后输入以下命令

中国用户：

```

$ python -m dos_attack_Chinese #这是Python版

......

$ dos_attack_Chinese.exe #如果是Windows用户，可以用这个

```

除中国以外的其他用户:

```

$ python -m dos_attack_English

......

$ dos_attack_English.exe #如果是Windows用户，可以用这个

```

## 获取IP地址和端口

如果是攻击网站，那么我们需要获取IP地址

```

$ ping (网站名)

.......

```

返回的数据中，类似43.193.46.733这样的数据就是我们要的IP地址

返回的数据中，TTL就是端口，一般为80，23，443

Windows用户同理

## 使用并攻击

下面带来的是中国用户的攻击页面，外国用户类似

```

......

Dog_dos>set_ip  你的IP地址

Set IP address 你的IP地址

Dog_dos>set_port 你的端口 #默认80，如果端口不是80，才需要用这条命令调整

Set port 你的端口

Dog_dos>set_thread_num 线程数量 #视自己电脑硬件性能决定，默认为500，可以不用这条命令调整

Set thread num 线程数量

Dog_dos>attack #攻击

......(Y/N)y #这个是一条法律声明，意思是谨慎使用，如果退出写N，继续写Y

......

```

## 带来的效果

我不能说所有的设备，但是我攻击我家一台电脑后，查看任务管理器，CPU占有率是非常接近100%，看视频也比较卡

## 将来的版本有可能会增加的功能

本作者有可能在将来的0.0.2版本增加以下功能

- [ ] 用户能随意更改发送数据包，只要不超过规定范围

- [ ]  增加网站自动识别IP功能，新增set_ip_port_url命令，输入URL，即可获取IP地址

- [ ] 增加网站自动识别端口功能,也是用set_ip_port_url命令，输入URL，即可获取端口

- [ ] 可以根据电脑CPU核数，为你计算出合适的攻击线程数量

- [ ] 可以选择攻击程度，自动为你挑选攻击数据包，和，攻击线程数量

有可能会在1.0.0版本添加gui功能，当然，也不妨碍那些喜欢命令行的人，使用命令行攻击

## 结尾和法律声明

本工具仅限装逼和渗透学习使用，也可以做为渗透工作中的得力助手。

《刑法》第二百八十五条

- **违反国家规定，侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。**

- **违反国家规定，侵入前款规定以外的计算机信息系统或者采用其他技术手段，获取该计算机信息系统中存储、处理或者传输的数据，或者对该计算机信息系统实施非法控制，情节严重的，处三年以下有期徒刑或者拘役，并处或者单处罚金；情节特别严重的，处三年以上七年以下有期徒刑，并处罚金。**

希望大家合法使用，祝大家使用愉快，也别忘了点star+fork+watch哦，么么哒～(^з^)-☆
