"""闭包"""
# 闭包就是函数里的函数

def foo():
	num = 1
	global x
	def bar(num):
		num += 6
		return num
	x = bar(num)
	return num

print(foo())
print(x)

"""
闭包可以访问外部变量
python闭包不能修改外部变量的值
即: 闭包可以保护变量
其实没啥用...
"""