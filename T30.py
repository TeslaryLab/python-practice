"""二分查找"""
def search(array, number):
	length = len(array)
	start = 0
	end = length - 1
	while(start < end):
		mid = (start + end) // 2
		mid_value = array[mid]

		if mid_value < number:
			start = mid + 1
		elif mid_value > number:
			end = mid - 1
		else:
			return mid

	return -1

if __name__ == '__main__':
	array = [1,3,5,6,7,11,14,16,19]
	index = search(array, 5)
	print('number 5 index:', index)
