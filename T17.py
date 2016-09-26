"""文件读写"""

if __name__ == '__main__':
	file_url = './tool/file.txt'
	write_mode = 'w+'
	read_mode = 'r'
	buffer_size = -1
	file_data = open(file_url, write_mode, buffer_size)
	print("操作{}文件中...".format(file_data.name))
	file_data.write("hello, world!")
	file_data.close()
	file_data = open(file_url, read_mode, buffer_size)
	print("写入文件内容为\n{}".format(file_data.readline()))
	file_data.close()

"""
文件读写配合
mkdir 生成目录
chdir 切换目录
rmdir 删除目录
remove 删除文件
等方法配合使用
"""