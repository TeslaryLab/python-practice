"""输入一个字符串要求判断它里面有数字、大小写字母，并且长度是6-18"""
def str_check(password):
	# password = str(password) # 类型强转 如果遇到None
	if type(password) != type(str()):
		return False
	upper	= False
	lower 	= False
	number	= False
	if len(password) < 6 or len(password) > 18:
		return False
	for char in password:
		if char > 'A' and char < 'Z':
			upper = True
		if char > 'a' and char < 'z':
			lower = True
		if char > '0' and char < '9':
			number = True
	return upper and lower and number 

def test_case():
	"""以后要尝试自己写测试例子"""
	str1 = '123' # < 6
	str2 = 'fjslkxcnvkdfhuw2347SDHJK' # > 18
	str3 = '1234SFTsdkt' # 标准
	str4 = 'coralstr' # 纯英文
	str5 = '#$&()$#&*(_' # 特殊字符
	str6 = '' # 空字符
	str7 = 7463722 # 数字, 如果不处理这种情况会报错 参考line3
	str8 = None # 空
	assert str_check(str1) == False
	assert str_check(str2) == False
	assert str_check(str3) == True
	assert str_check(str4) == False
	assert str_check(str5) == False
	assert str_check(str6) == False
	assert str_check(str7) == False
	assert str_check(str8) == False
	print("测试全部通过")

if __name__ == '__main__':
	test_case()
	print('-----------------')
	password = input("输入字符串:\n")
	result = str_check(password)
	if result == True:
		print("通过校验")
	else:
		print("校验不通过")
