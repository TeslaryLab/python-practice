"""引用&拷贝"""
import copy

# 深拷贝
a = [1, 2, [3, 4]]
b = copy.copy(a)
c = copy.deepcopy(a)
b[2][1] = 5
c[2][0] = -1
print (a)
print (b)
print (c)
