"""冒泡排序"""
def bubble(sort_list):
	list_length = len(sort_list)
	for i in range(0, list_length):
		for j in range(0, list_length-1):
			if sort_list[i] < sort_list[j]:
				sort_list[i],sort_list[j] = sort_list[j],sort_list[i]

if __name__ == '__main__':
	sort_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	print('排序前:{}'.format(sort_list))
	bubble(sort_list)
	print('排序后:{}'.format(sort_list))
