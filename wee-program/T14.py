"""多线程"""
import threading
from time import ctime,sleep

def thread1(func):
	print('i am thread1')
	sleep(5)

def thread2(func):
	print('i am thread2')
	sleep(2)

thead_list = []
t1 = threading.Thread(target=thread1,args=('test',))
thead_list.append(t1)
t2 = threading.Thread(target=thread2,args=('test',))
thead_list.append(t2)

if __name__ == '__main__':
	for t in thead_list:
		t.setDaemon(True)
		t.start()

"""
python有GIL
所以多线程很鸡肋
I/O密集可以处理
"""