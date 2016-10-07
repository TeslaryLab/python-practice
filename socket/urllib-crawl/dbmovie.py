"""豆瓣电影top250"""
from urllib import request
import re, pprint
# pprint(排查问题用)


PATH = 'https://movie.douban.com/top250'
PATTERN = '<span class="title">(.*)</span>'


def get_html(url):
	'''
	获取网页数据
	'''
	with request.urlopen(url) as r:
		data = r.read()
	return data


def pick_data(data):
	'''
	提取电影标题
	'''
	items = re.findall(PATTERN, data)
	for item in items:
		pre = '&nbsp;/&nbsp;'
		pre_len = len(pre)
		if item.find(pre) != -1:
			item = item[pre_len:-1]
		save(item)



def save(message):
	'''
	存储到文件中
	'''
	with open('top50.txt','a+', encoding='utf-8') as f:
		f.write('{}\n'.format(message))



def mock():
	'''
	mock数据
	'''
	data = ''
	with open('mock.txt', 'r', newline='', encoding='utf-8') as f:
		data = f.read()
	print(pick_data(data))


if __name__ == '__main__':
	r = get_html(PATH)
	data = str(r, encoding='utf-8')
	items = pick_data(data)
