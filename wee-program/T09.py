"""super的使用"""

class Father(object):
	def foo(self):
		print('foo message')

class Son(Father):
	def __init__(self):
		super(Son, self).foo() # 为什么要加self的参数, python 设计问题...

if __name__ == '__main__':
	son = Son()

"""
不了解这个 super 的话有些代码看不懂
"""