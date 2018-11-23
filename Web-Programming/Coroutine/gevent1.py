'''
gevent 是对 greenlet的再次封装

'''

import gevent 
import time

from gevent import monkey

monkey.patch_all() # 把当前的代码所有的耗时的操作变成gevent.sleep()

def f1(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.1)

def f2(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.1)

def f3(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.1)

print('---1----')

g1 = gevent.spawn(f1, 5)
print('---2----')

g2 = gevent.spawn(f2, 5)
print('---3----')

g3 = gevent.spawn(f3, 5)
print('---4----')

g1.join()
g2.join()
g3.join()

"""
gevent.joinall([
gevent.spawn(function, args)
.....
.....])
"""
