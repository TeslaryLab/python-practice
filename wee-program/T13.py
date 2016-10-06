"""多进程"""
import os
from multiprocessing import Process

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('sub-process',))
    print('Process will start.')
    p.start()
    p.join()
    print('Process end.')

"""进程通讯用 Queue / Pipes"""