"""运算符重载"""

class Number(object):
	def __init__(self, value):
		self.data = value

	def __str__(self):
		return "my value is {}".format(self.data)

if __name__ == '__main__':
	num = Number(5)
	print(str(num))


"""
python提供的可重载的运算符

Method        	Overloads        	Call for
__init__        构造函数        	X=Class()
__del__        	析构函数        	对象销毁
__add__        	+                	X+Y,X+=Y
__or__        	|                	X|Y,X|=Y
__repr__        打印转换        	print X，repr(X)
__str__        	打印转换        	print X，str(X)
__call__        调用函数        	X()
__getattr_   	限制            	X.undefine
__setattr__    	取值            	X.any=value
__getitem__    	索引            	X[key]，
                            
__len__        	长度            	len(X)
__cmp__        	比较            	X==Y,X<Y
__lt__        	小于            	X<Y
__eq__        	等于            	X=Y
__radd__        Right-Side +        +X
__iadd__        +=                	X+=Y
__iter__        迭代            	For In 
"""