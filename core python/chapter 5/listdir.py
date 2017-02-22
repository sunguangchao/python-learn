# -*- coding:utf-8 -*-
import os
from time import sleep
from Tkinter import *

class DirList(object):
	def __init__(self, initdir=None):
		self.top = Tk()
		self.label = Label(self.top, text='Directory Lister v1.1')
		self.label.pack()
	
		self.cwd=StringVar(self.top) #cwd变量用于保存当前所在的目录名
	
		self.dirl = Label(self.top, fg='blue', font=('Helvatica', 12, 'bold'))
		self.dirl.pack() #显示当前目录名
	
		self.dirfm = Frame(self.top)
		self.dirsb = Scrollbar(self.dirfm)
		self.dirsb.pack(side=RIGHT, fill=Y)
		self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
		self.dirs.bind('<Double-1>', self.setDirAndGo) #bind函数使得Listbox的列表项可以与回调函数链接起来
		self.dirsb.config(command=self.dirs.yview)#Scrollbar通过Scrollbar.config方法与Listbox连接起来
		self.dirs.pack(side=LEFT, fill=BOTH)
		self.dirfm.pack()
	
		self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
		self.dirn.bind('<Return>', self.doLS)
		self.dirn.pack()
	
		self.bfm = Frame(self.top)#定义下侧的三个按钮
		self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white', activebackground='blue')
		self.ls = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white', activebackground='green')
		self.quit = Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white', activebackground='red')
		self.clr.pack(side=LEFT)
		self.ls.pack(side=LEFT)
		self.quit.pack(side=LEFT)
		self.bfm.pack()
	
		if initdir:
			self.cwd.set(os.curdir)
			self.doLS()

	def clrDir(self, en=None):#清空cwd变量
		self.cwd.set('')

	def setDirAndGo(self, en=None):#设置要遍历的目录
		self.last = self.cwd.get()
		self.dirs.config(selectbackground='red')
		check = self.dirs.get(self.dirs.curselection())
		if not check:
			check = os.curdir
		self.cwd.set(check)
		self.doLS()

	def doLS(self, en=None):
		error = ''
		tdir = self.cwd.get()
		if not tdir: tdir = os.curdir #如果发生错误，设置为当前目录

		if not os.path.exists(tdir):
			error = tdir + ':no such file'
		elif not os.path.isdir(tdir):
			error = tdir + ': not a directory'

		if error:
			self.cwd.set(error)
			self.top.update()
			sleep(2)
			if not (hasattr(self, 'last') and self.last):
				self.last = os.curdir
			self.cwd.set(self.last)
			self.dirs.config(selectbackground='LightSkyBlue')
			self.top.update()
			return

		self.cwd.set('FETCHING DIRECTORY CONTENTS...')
		self.top.update()
		dirlist = os.listdir(tdir)
		dirlist.sort()
		os.chdir(tdir)

		self.dirl.config(text=os.getcwd())
		self.dirs.delete(0, END)
		self.dirs.insert(END, os.curdir)
		self.dirs.insert(END, os.pardir)
		for eachFile in dirlist:
			self.dirs.insert(END, eachFile)
		self.cwd.set(os.curdir)
		self.dirs.config(selectbackground='LightSkyBlue')

def main():
	d = DirList(os.curdir)
	mainloop()#启动GUI程序

if __name__ == '__main__':
	main()


