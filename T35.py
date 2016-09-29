"""利用 ConfigParser 读写配置文件"""
import configparser

cf = configparser.ConfigParser()
cf.read('./tool/init.conf', encoding = 'utf-8')

# section list
s = cf.sections()
# print("section:",s)

# 仅获得options list
config_list = cf.options("database")
# print(config_list)

# 获得items的kv-map
config_map = cf.items("database") 

# 直接获取某个配置属性
todo = cf.get("todolist", "todo")
# print(todo)

# 读写 config
if cf.has_section('test'):
	print('test already exist!')
else:
	cf.add_section('test')
	cf.set('test', 'option', 'startup')
	cf.set('test', 'option_to_del', 'del_me')
	cf.write(open('./tool/init.conf', 'w', encoding = 'utf-8'))
	print('write scuess')

# 删除 option
if cf.has_option('test', 'option_to_del'):
	cf.remove_option('test', 'option_to_del')
else:
	print('there is nothing to del.')


# 删除 section
if cf.has_section('test'):
	cf.remove_section('test')
	print('del test scuess')

# 更新值文件
cf.write(open('./tool/init.conf', 'w', encoding = 'utf-8'))
	
# 更新 option 值 --> 同 set

"""
可以对 config 文件进行增删改查
sections
items
"""