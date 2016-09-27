"""解析 json """
import json

def read_json_from_str(json_str):
	data = json.loads(json_str)
	for key in data:
		print(data[key])

def read_json_from_file(file_path):
	with open(file_path, 'r', newline='', encoding='utf-8') as f:
		data = json.load(f)
	for key in data:
		print(data[key])
	with open('./tool/new_data.json', 'w') as f:
		json.dump(data, f)

if __name__ == '__main__':
	json_data = {'name' : 'ACME','shares' : 100, 'price' : 542.23}
	json_str = json.dumps(json_data)
	file_path = './tool/data.json'
	read_json_from_str(json_str)
	read_json_from_file(file_path)


"""
主要是熟悉接口
意识到有编码问题
"""
