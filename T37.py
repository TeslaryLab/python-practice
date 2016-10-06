"""各种字符串操作"""
# 顺手记录, 可以自动close
def open_file(filename):
	with open(filename,'w+') as f:
		for line in f:
			print(line)

# join 连接符号
':'.join(['12','42','23'])

'12:42:23'.split(':')
'12:42:23'.split(':', 0)

'hello,world'.find(',')
