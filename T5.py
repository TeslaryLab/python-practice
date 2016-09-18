"""给出如下的矩阵，输入一个数判断这个矩阵中有没有这个数，没有返回-1"""
def matrix_find(matrix, aim):
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix[i])):
			if matrix[i][j] == aim:
				return "坐标{}行{}列".format(i+1,j+1)
	return -1
	
if __name__ == '__main__':
	matrix = [[1, 2, 3, 4, 5],
			  [2, 4, 5, 7, 9],
			  [4, 6, 7, 8, 10],
			  [5, 7, 9, 12, 17],
			  [7, 8, 11, 13, 18]]
	"""矩阵打印"""
	for i in matrix:
		for j in i:
			print(str(j)+'\t',end = '')
		print()
	"""aim为查询的参数"""
	aim = 5 # 可修改
	result = matrix_find(matrix, aim)
	print(result)
