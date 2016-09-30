"""八皇后问题"""
res = [0] * 8
count = 0

def check(index, value):
	for i in range(0, index):
		data = res[i]
		if value == data or i+data == index+value or i-data == index-value:
			return False
	return True

def queens(index):
	global count
	for value in range(0,8):
		if check(index, value):
			res[index] = value
			if index == 7:
				count += 1
				res[index] = 0
				return 
			queens(index+1)
			res[index] = 0

if __name__ == '__main__':
	queens(0)
	print(count)

"""
8x8相互不攻击
"""