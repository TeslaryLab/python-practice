"""单向链表"""

class Node(object):

	def __init__(self, value, p = None):
		self.value = value
		self.next = p

class LinkList(object):

	def __init__(self):
		self.head = 0

	def append(self, item):
		q = Node(item.value)
		if self.head == 0:
			self.head = q
		else:
			p = self.head
			while p.next != None:
				p = p.next
			p.next = q

	def len(self):
		length = 0
		p = self.head
		while p != None:
			length += 1
			p = p.next
		return length

	def output(self):
		list_out = []
		p = self.head
		while p != None:
			list_out.append(p.value)
			p = p.next
		return list_out

if __name__ == '__main__':
	link_list = LinkList()
	item1 = Node(1)
	item2 = Node(2)
	item3 = Node(3)
	link_list.append(item1)
	link_list.append(item2)
	link_list.append(item3)
	print(link_list.output())
	print(link_list.len())

"""实现 添加/长度/输出 功能"""