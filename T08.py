"""yield的使用 && 生成器generator"""

def plus(num):
	while num < 10:
		yield num*num
		num += 1

if __name__ == '__main__':
	func = plus(5) 
	"""
	for step in func:
		print(step)	
	"""
	print(func.__next__())
	print(func.__next__())
	print(func.__next__())
	print(func.__next__())
	print(func.__next__())
	# print(func.__next__()) # Exception : stopIteration

"""
yield 的原理是把函数变成一个 generator 对象
每次遇到 yield 都会返回一次值
通过调用 next 来进入下次调用
可以理解成把一个函数拆成一步步的函数
"""