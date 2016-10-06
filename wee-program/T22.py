"""lambda 表达式"""

def bar():return 'this is bar'

if __name__ == '__main__':
	foo = lambda x,y:'{}+{}={}'.format(x, y, x+y)
	print(foo(1,2))
	print(bar())


"""
lambda 调用的时候绕过函数的栈分配
"""
