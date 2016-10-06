"""Quine"""

s='s=%r;print(s%%s)';print(s%s)

"""
Quine 是一个能打印出自己的程序
%r = repr 打印时能够重现它所代表的对象
%s用str()方法处理对象
%%s转义
好像没啥用...
"""