"""global && nonlocal"""

global_int = 1

def change():
	global global_int
	global_int = 5 
	temp_int = 2
	def change_inner():
		temp_int = 9
		nonlocal temp_int
		temp_int = 3
	change_inner()
	print(temp_int)

if __name__ == '__main__':
	change()
	print(global_int)

"""
python引用变量的顺序:
当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量
global关键字用来在函数或其他局部作用域中使用全局变量
nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
乱改其他域的变量是一种很烂的写法
全局变量也是一种很烂的写法
"""