"""decorator"""
def logger(func):
	def inner(*args, **kvargs):
		print(func.__name__,\
				' called, arguments:',\
				args, kvargs)
	return inner

@logger
def foo(name = 'world'):
	print('hello,{}!'.format(name))

if __name__ == '__main__':
	foo('corals', name = 'python')


"""
 *args
 拓展参数
 **kwargs
 k-v拓展参数
"""