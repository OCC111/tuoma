#coding=utf-8

'''
class Dog(object):
	__instance = None
	def __init__(self):
		pass
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls,*args,**kwargs)
			return cls.__instance
		else:
			return cls.__instance

a = Dog()
b = Dog()

print(a)
print(b)
'''

'''
class Animal(object):
	def __init__(self,name):
		self.name = name
	
	def run(self):
		print("Animal is runing...")

class Dog(Animal):
	def __init__(self,name):
		Animal.__init__(self,name)

	def printName(self):
		print("Name:%s"%self.name)

class Cat(Animal):
	def __init__(self,name):
		Animal.__init__(self,name)
	def PrintName(self):
		print("Name1:%s"%self.name)

class Python(Animal):
	def __init__(self,name):
		Animal.__init__(self,name)
	def PrintName1(self):
		print("Name2:%s"%self.name)


kk = Dog("Kity")
kk.printName()
kk.run()

t = Cat("tom")
t.PrintName()
t.run()

p = Python("jirl")
p.PrintName1()
p.run()
'''


'''
import re

#正则表达式
re.match("^1[0-9]\d{9}$","17319227441")
re.match("[0-9A-Za-z]{4,20}@qq|163|126.com","859899882@qq.com")
'''





def w1(fun):
	def inner():
		print("正在验证")
		fun()
	return inner

@w1
def Test():
	print("哈哈")

Test()

