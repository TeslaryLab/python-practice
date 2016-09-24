"""元编程"""

class Foo(object):
	def bar(self):
		print('foo-bar!')

class meta(object):
	Metaclass = type('FooChild', (Foo,), {'ip':'192.168.1.1'})
	Metaclass().bar()
	print(Metaclass().ip)

if __name__ == '__main__':
	meta()


"""
仅记录了简单使用方法
首先查看 metaclass 有没有定义
如果没有就查看父类
父类木有就查看 type

函数调用顺序
__prepare__
__new__(cls, name, parents, attrs)
cls代表调用__new__函数的class
name代表对象的__name__值，也就是名称
parents代表对象的父类元组
attrs代表类的属性字典 
"""