"""have fun"""
def generate_number(tail = -1):
	files = ''
	def number2str(number,before='T',end='.py'):
		if number < 10:
			yield before+'0'+str(number)+end
		else:
			yield before+str(number)+end
	# 默认创建 40 个
	if tail == -1:
		files = [x for x in range(1,41)]
		files_name = []
		for i in map(number2str, files):
			files_name.append(i.__next__())
		print(files_name)
	else:
		files = [x for x in range(1,tail+1)]
		files_name = []
		for i in map(number2str, files):
			files_name.append(i.__next__())
		print(files_name)
	return files_name

new_files = generate_number(tail = 60)
for name in new_files:
	single = open(name, 'w')
	single.close()

"""
写的有点挫, 待review
"""