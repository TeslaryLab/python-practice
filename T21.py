"""enumerate"""
info_list = ['姓名', '年龄', '年级', '班级', '成绩']
for index, item in enumerate(info_list, 0):
	print("序号:{}, 内容:{}".format(index, item))

"""
枚举方法
可以指定index
(index, item) = enumerate(list/str[, start_index])
"""