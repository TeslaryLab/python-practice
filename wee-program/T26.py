"""快速排序"""

def quick_sort(array, start, end):
	if start >= end:
		return 
	i = start
	j = end
	pkey = array[start]
	while i < j:
		while i < j and array[j] >= pkey:
			j = j - 1
		if i < j:
			array[i] = array[j]
			i = i + 1
		while i < j and array[i] < pkey:
			i = i + 1
		if i < j:
			array[j] = array[i]
			j = j - 1
	array[j] = pkey
	mid = i
	quick_sort(array, start, mid-1)
	quick_sort(array, mid+1, end)
	

if __name__ == '__main__':
	array = [7,6,8,9,5,4,3,2,1]
	print('array:', array)
	quick_sort(array, 0, len(array)-1)
	print('sorted:', array)