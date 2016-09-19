"""class的构造函数、继承"""

class Father(object):
	def __init__(self):
		# """self是对象自身的引用"""
		print("this is father's init-method!") # 构造函数

	def method(self):
		print("old method by fater!")

class Son(Father): # 通过()完成继承
	def __init__(self):
		Father.method(self) 
		print("this is son's init-method!")

	def method(self):
		print("new method by son!") # 覆盖了继承来的method方法

if __name__ == '__main__':
	father = Father()
	son = Son()
	son.method()