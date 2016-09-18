"""使用python列表推导生成等差数列、等比数列"""

if __name__ == '__main__':
	diff_seq  = [x for x in range(1,15,2)] 
	scale_seq = [x**i for x in [5] for i in range(1,10)]
	print("等差数列{}".format(diff_seq))
	print("等比数列{}".format(scale_seq))
	
"""可以自己封装成函数使用"""